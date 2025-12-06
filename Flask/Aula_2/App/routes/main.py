from flask import Blueprint,jsonify

main_bp = Blueprint('main.bp', __name__)

@main_bp.route('/')
def index():
    return jsonify({'Mensagem':'Bem vindo a StyleSync'})

@main_bp.route('/Produtos'):
def get_produtos():
    return jsonify({'Mensagem':'Essa é a rota de listagem dos produtos.'})

@main_bp.route('/login', methods = ['POST'])
def login():
    return jsonify({'Mensagem':'Essa é a rota de listagem dos produtos.'})
