from flask import render_template, flash, redirect, request, session
from app import app


cadastros = {
    'dener':'123'
}

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('Usuário deslogado!')
    return redirect("/")

@app.route('/autenticar', methods=["POST",])
def autenticar():
    if request.method == "POST":
        if request.form['senha'] in cadastros.values() and request.form['usuario'] in cadastros.keys():
            session['usuario_logado'] = request.form['usuario']
            flash(request.form['usuario'] + '! Logado com sucesso') 
            return redirect('/menu')
        else:
            flash('Suas informações não estão corretas, ou não possui cadastro')
            return redirect('/')