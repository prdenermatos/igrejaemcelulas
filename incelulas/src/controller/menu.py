from flask import render_template, flash, redirect, request, session, url_for
from app import app
#from src.service.authentication_service import AuthenticationService


cadastros = {
    'dener':'123'
}

#authentication = AuthenticationService()

@app.route("/novasenha")
def nova_senha():
    return render_template("novasenha.html")

@app.route("/pedir_senha", methods=["POST"])
def pedir_senha():
    flash("Em breve entraremos em contato com você, por e-mail!")
    return redirect("/")


@app.route('/menu')
def menu():
    return render_template('menu.html')
    

@app.route('/cadastraruser', methods=["POST", "GET"])
def cadastrar_user():
    #authentication.is_authenticate()
    return render_template('cadastraruser.html')

@app.route('/criaruser', methods=["POST"])
def criaruser():
    nome_completo = request.form['nome_completo']
    data_nascimento= request.form['data_nascimento']
    data_nascimento = request.form['email']
    rua_numero = request.form['rua-numero']
    bairro = request.form['bairro']
    celular = request.form['celular']
    nome_pais = request.form['pai-mae']
    contato_pais = request.form['contato-pais']
    celula = request.form['celula']
    nome_discipulador = request.form['discipulador']
    data_batismo = request.form['data-batismo']
    usuario = request.form['usuario']
    senha = request.form['senha']
    cadastros[usuario] = senha
    #checkbox:::
    encontro_vencedores = request.form['encontro_vencedores']
    acompanhamento_inicial = request.form['acompanhamento_inicial']
    batismo = request.form['batismo']
    membresia = request.form['membresia']
    dizimista = request.form['dizimista']
    celebração = request.form['celebração']
    celula = request.form['celula']
    tlc = request.form['tlc']
    renovo = request.form['renovo']
    auxiliar_celula = request.form['auxiliar_celula']
    sou_discipulado = request.form['sou_discipulado']
    servo = request.form['servo']
    tenho_discipulos = request.form['tenho_discipulos']
    aprovado = request.form['aprovado']


    flash('Bem vindo ao Comunidade Elo Esperança!')
    return redirect("/")
  
   

# ROTAS ADM

@app.route('/dash-adm')
def dash_adm():
    return render_template("dash_adm.html")
