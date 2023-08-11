from flask import Flask, render_template

app = Flask(__name__)

# criar a 1º página do site
# route -> caminho da página
# função -> o que você quer exibir naquela página
# template

@app.route("/")
def homepage():
    return render_template("homepage.html")

@app.route("/contatos")
def contatos():
    return render_template("contatos.html")

@app.route("/usuarios/<nome_usuario>")
def usuarios(nome_usuario):
    return nome_usuario

#colocar o site no ar
if __name__ == "__main__":
    app.run(debug=True) # Usamod o debug=True para não precisar ficar parando o programa para aplicar alterações no código.

