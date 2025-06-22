import os

from wtforms.fields.simple import SubmitField

from jogoteca import app
from flask_wtf import  FlaskForm
from wtforms import StringField, validators, SubmitField, PasswordField
from wtforms.validators import DataRequired, Length



class FormularioJogo(FlaskForm):
    nome = StringField('Nome do Jogo', [validators.DataRequired(), validators.Length(min=1,max=50)])
    categoria = StringField('Nome do Jogo', [validators.DataRequired(), validators.Length(min=1,max=40)])
    console = StringField('Console', [validators.DataRequired(), validators.Length(min=1, max=20)])
    salvar = SubmitField('Salvar')


class FormularioUsuario(FlaskForm):
    nickname = StringField('Nickname', [validators.DataRequired(), validators.Length(min=1,max=8)])
    senha = PasswordField('Senha', [validators.DataRequired(), validators.Length(min=1,max=100)])
    login = SubmitField('Login')

class FormularioCadastroUsuario(FlaskForm):
    nome = StringField('Nome', validators=[DataRequired(), Length(min=1, max=20)])
    nickname = StringField('Nickname', validators=[DataRequired(), Length(min=1, max=8)])
    senha = PasswordField('Senha', validators=[DataRequired(), Length(min=3, max=100)])
    cadastrar = SubmitField('Cadastrar')

def recupera_imagem(id):
    for nome_arquivo in os.listdir(app.config['UPLOAD_PATH']):
        if f'capa{id}' in nome_arquivo:
            return nome_arquivo

    return 'capa_padrao.jpg'

def deleta_arquivo(id):
    arquivo = recupera_imagem(id)
    if arquivo != 'capa_padrao.jpg':
        caminho_completo = os.path.join(app.config['UPLOAD_PATH'], arquivo)
        if os.path.exists(caminho_completo):
            os.remove(caminho_completo)
