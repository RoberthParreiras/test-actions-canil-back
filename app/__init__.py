from flask import Flask

app = Flask(__name__)

@app.route('/')
def test_back():
    return {"msg": "Deu tudo certo!"}
