from modelos.FilmeController import FilmeController

from importlib.resources import Resource
from flask import Flask, abort, jsonify, request, render_template

class App:
    def __init__(self):
        self.app = Flask(__name__)
        self.setup_routes()

    def setup_routes(self):
        @self.app.route('/')
        def index():
            return render_template('index.html')

        @self.app.route('/search', methods=['GET'])
        def search():
            search_term = request.args.get('term', '')
            results = FilmeController.select_like(search_term)
            return jsonify(results)

        @self.app.route('/insert', methods=['POST'])
        def insert():
            data = request.json
            titulo = data.get('titulo')
            genero = data.get('genero')
            
            if not titulo or not genero:
                return jsonify({'status': 'error', 'message': 'Campos titulo e genero são obrigatórios'}), 400
            
            FilmeController.insert_filme(titulo, genero)
            return jsonify({'status': 'success'})

        @self.app.route('/update', methods=['PUT'])
        def update():
            data = request.json
            idfilme = data.get('idfilme')
            
            if idfilme is None:
                return jsonify({'status': 'error', 'message': 'Campo idfilme é obrigatório'}), 400
            
            titulo = data.get('titulo')
            genero = data.get('genero')
            assistido = data.get('assistido')
            FilmeController.update_filme(idfilme, titulo, genero, assistido)
            return jsonify({'status': 'success'})
                
        @self.app.route('/delete', methods=['DELETE'])
        def delete():
            data = request.json
            idfilme = data.get('idfilme')
            
            if idfilme is None:
                return jsonify({'status': 'error', 'message': 'Campo idfilme é obrigatório'}), 400
            
            FilmeController.delete_filme(idfilme)
            return jsonify({'status': 'success'})

    def run(self):
        self.app.run(debug=True)

if __name__ == '__main__':
    app = App()
    app.run()