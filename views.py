from flask import render_template, request, redirect, session, flash, url_for, send_from_directory
from jogoteca import app, db
from models import Jogos, Usuarios
from helpers import recupera_imagem, deleta_arquivo, FormularioJogo, FormularioUsuario
import time
import os
from flask_bcrypt import check_password_hash
from flask_bcrypt import generate_password_hash
from helpers import FormularioCadastroUsuario



@app.route('/')
def index():
    lista = Jogos.query.order_by(Jogos.id)
    return render_template('lista.html', titulo='Jogos', jogos=lista)

@app.route('/novo')
def novo():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login', proxima=url_for('novo')))
    form=FormularioJogo()
    return render_template('novo.html', titulo='Novo Jogo',form=form)

@app.route('/criar', methods=['POST'])
def criar():
    form = FormularioJogo()

    if not form.validate_on_submit():
        for campo, erros in form.errors.items():
            for erro in erros:
                flash(f'Erro no campo "{campo}": {erro}')
        return render_template('novo.html', titulo='Novo Jogo', form=form)
    nome = form.nome.data
    categoria = form.categoria.data
    console = form.console.data

    jogo = Jogos.query.filter_by(nome=nome).first()

    if jogo:
        flash('Jogo já existente!')
        return redirect(url_for('index'))

    novo_jogo = Jogos(nome=nome, categoria=categoria, console=console)
    db.session.add(novo_jogo)
    db.session.commit()

    arquivo = request.files['arquivo']
    upload_path = app.config['UPLOAD_PATH']
    timestamp = time.time()
    arquivo.save(f'{upload_path}/capa{novo_jogo.id}-{timestamp}.jpg')

    return redirect(url_for('index'))

@app.route('/editar/<int:id>')
def editar(id):
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login', proxima=url_for('editar', id=id)))
    jogo = Jogos.query.filter_by(id=id).first()
    form = FormularioJogo()
    form.nome.data = jogo.nome
    form.categoria.data = jogo.categoria
    form.console.data = jogo.console
    capa_jogo = recupera_imagem(id)
    return render_template('editar.html', titulo='Editando Jogo', id=id, capa_jogo=capa_jogo,form = form)

@app.route('/atualizar', methods=['POST'])
def atualizar():
    form = FormularioJogo()

    if form.validate_on_submit():
        jogo = Jogos.query.filter_by(id=request.form['id']).first()

        if not jogo:
            flash('Jogo não encontrado.')
            return redirect(url_for('index'))

        jogo.nome = form.nome.data
        jogo.categoria = form.categoria.data
        jogo.console = form.console.data

        db.session.commit()

        arquivo = request.files['arquivo']
        if arquivo and arquivo.filename != '':
            upload_path = app.config['UPLOAD_PATH']
            timestamp = time.time()

            # Remove a capa antiga
            deleta_arquivo(jogo.id)

            # Salva nova capa
            nome_arquivo = f'capa{jogo.id}-{timestamp}.jpg'
            caminho_completo = os.path.join(upload_path, nome_arquivo)
            arquivo.save(caminho_completo)

        flash('Jogo atualizado com sucesso!')
        return redirect(url_for('index'))

    # Caso o formulário não seja válido
    flash('Erro ao atualizar jogo. Verifique os dados informados.')
    return redirect(url_for('editar', id=request.form['id']))

@app.route('/deletar/<int:id>')
def deletar(id):
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login'))

    Jogos.query.filter_by(id=id).delete()
    db.session.commit()
    flash('Jogo deletado com sucesso!')

    return redirect(url_for('index'))

@app.route('/login')
def login():
    proxima = request.args.get('proxima')
    form = FormularioUsuario()
    return render_template('login.html', proxima=proxima, form=form)

@app.route('/autenticar', methods=['POST',])
def autenticar():
    form = FormularioUsuario(request.form)
    usuario = Usuarios.query.filter_by(nickname=form.nickname.data).first()
    senha = check_password_hash(usuario.senha, form.senha.data)
    if usuario and senha:
            session['usuario_logado'] = usuario.nickname
            flash(usuario.nickname + ' logado com sucesso!')
            proxima_pagina = request.form['proxima']
            return redirect(proxima_pagina)
    else:
        flash('Usuário não logado.')
        return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('Logout efetuado com sucesso!')
    return redirect(url_for('index'))


@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    form = FormularioCadastroUsuario()

    if form.validate_on_submit():
        nome = form.nome.data
        nickname = form.nickname.data
        senha = generate_password_hash(form.senha.data).decode('utf-8')

        # Verifica se já existe
        usuario_existente = Usuarios.query.filter_by(nickname=nickname).first()
        if usuario_existente:
            flash('Nickname já está em uso!')
            return render_template('cadastro.html', form=form)

        novo_usuario = Usuarios(nome=nome, nickname=nickname, senha=senha)
        db.session.add(novo_usuario)
        db.session.commit()

        flash('Usuário cadastrado com sucesso! Faça login.')
        return redirect(url_for('login'))

    return render_template('cadastro.html', form=form)

@app.route('/uploads/<nome_arquivo>')
def imagem(nome_arquivo):
    return send_from_directory('uploads', nome_arquivo)