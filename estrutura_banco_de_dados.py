from flask import Flask         #pussibilita criar o API
from flask_sqlalchemy import SQLAlchemy         #pussibilita criar o Bando de Dados

#Criar um API flask
app = Flask(__name__)           #recebe o nome do arquivo que está sendo executado naquele momento

#Criar uma instância de SQLAlchemy      (Definir informações importantes do Bando de Dados)
app.config['SECRET_KEY'] = 'FSD2323f#$!SAH'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'

db = SQLAlchemy(app)            #instanciar o SQLAlchemy passa a aplicação que acabou de criar 'app'
db:SQLAlchemy                   #especificar sera tipa SQLAlchemy

#Definir a estrutura da tabela Postagem
#toda postagem deve possuir um id_postagem,  titulo, autor
class Postagem(db.Model):               #db.Model instanciar todas as estruturas e funcionalidades herdas de db.model
    __tablename__ = 'postagem'
    id_postagem = db.Column(db.Integer, primary_key=True)       #tipo inteiro
    titulo = db.Column(db.String)
    id_autor = db.Column(db.Integer, db.ForeignKey('autor.id_autor'))  #linkar com o nome da TABELA e nome da propried.

#Definir a estrutura da tabela Autor 
#id_autor, nome, email, senha, admin, postagens
class Autor(db.Model):
    __tablename__ = 'autor'
    id_autor = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String)
    email = db.Column(db.String)
    senha = db.Column(db.String)
    admin = db.Column(db.Boolean)
    postagens = db.relationship('Postagem')     #passa o nome da CLASSE que irá se relacionar 

#Executar o comando para criar o banco de dados 
def inicializar_banco():
    with app.app_context():
        db.drop_all()               #irá apagar qualquer estrutura prévia que possa existir (rodar 1 vez quando está criando a tabela)
        db.create_all()             #iram permitir criar todas as tabelas que estão anexadas ao db
        autor = Autor(nome='Fernanda',email='fernanda@email.com', senha='123456', admin=True)   #Criar usuários administradores
        db.session.add(autor)       #adicionar o autor
        db.session.commit()         #salvar os dados

#a função só será rodada quando este arquivo for executado DIRETAMENTE 
if __name__ == '__main__':
    inicializar_banco()