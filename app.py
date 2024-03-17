from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__) # Cria uma instância do Flask. 


# Define rota da página principal
@app.route('/')
def index():
    return render_template('index.html') # Renderiza o template index.html, localizado na pasta templates

@app.route("/choraviola")
def choraviola():
 return "plem plem plem"

#dá pra fazer funções, por exemplo:
@app.route("/nome/<nome>")
def fala_galera(nome):
   return f'oi, tudo bem, {nome}?'

@app.route("/gptmjd", methods = ['POST', 'GET'])
def gptmjd(): #dá pra copiar o código do notebook e colocar o chatgpt aqui, por exemplo
   pergunta = request.form.get("texto")
   print(pergunta)
   return "legal" 

#sofisticando mais (criei o html falagalera)
#@app.route("/fala/<pessoa>")
#def fala_galera(pessoa):
#   turma = ["Elsa", "Sumaia", "João"]
#   return render_template ("falagalera.html",pessoa=pessoa, turma=turma)

#os 3 juntos não funciona não sei pq

if __name__ == '__main__':
  app.run(port=5000, debug=True) # Inicia o servidor na porta 5000. "Debug" é uma configuração para facilitar o desenvolvimento.
 