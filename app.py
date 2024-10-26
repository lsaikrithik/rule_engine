from flask import Flask, request, jsonify, render_template
from ast_node import create_rule, combine_rules, evaluate_rule, Node
from flask_pymongo import PyMongo
from dotenv import load_dotenv
import os


load_dotenv()

MONGO_URI = os.getenv('MONGO_URI')  
DB_NAME = os.getenv('DB_NAME') 

app = Flask(__name__)

app.config["MONGO_URI"] = MONGO_URI + DB_NAME
mongo = PyMongo(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/create_rule', methods=['POST'])
def create_rule_api():
    try:
        rule_string = request.json['rule_string']
        ast = create_rule(rule_string)

        ast_serialized = ast_to_dict(ast)

        mongo.db.rules.insert_one({'rule_string': rule_string})
        return jsonify({'ast': ast_serialized})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/combine_rules', methods=['POST'])
def combine_rules_api():
    try:
        rules = request.json['rules']
        ast = combine_rules(rules)

        ast_serialized = ast_to_dict(ast)
        return jsonify({'ast': ast_serialized})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/evaluate_rule', methods=['POST'])
def evaluate_rule_api():
    try:
        data = request.json['data']
        ast_data = request.json['ast']

        ast = dict_to_ast(ast_data)
        result = evaluate_rule(ast, data)
        return jsonify({'result': result})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

def ast_to_dict(node):
    """Serialize the AST node to a dictionary for JSON response."""
    return {
        'type': node.type,
        'value': node.value,
        'left': ast_to_dict(node.left) if node.left else None,
        'right': ast_to_dict(node.right) if node.right else None
    }

def dict_to_ast(data):
    """Deserialize the dictionary back to an AST node."""
    return Node(data['type'], 
                left=dict_to_ast(data['left']) if data['left'] else None,
                right=dict_to_ast(data['right']) if data['right'] else None,
                value=data['value'])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
