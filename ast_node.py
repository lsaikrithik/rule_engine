class Node:
    def __init__(self, type, left=None, right=None, value=None):
        self.type = type  
        self.left = left  
        self.right = right 
        self.value = value 

def create_rule(rule_string):
    def parse_expression(expression):
        expression = expression.strip()
        if expression.startswith('('):
            expression = expression[1:-1].strip()
        
        if 'AND' in expression:
            left, right = expression.split('AND', 1)
            return Node(type="operator", left=parse_expression(left), right=parse_expression(right), value="AND")
        elif 'OR' in expression:
            left, right = expression.split('OR', 1)
            return Node(type="operator", left=parse_expression(left), right=parse_expression(right), value="OR")
        else:
            return Node(type="operand", value=expression.strip())

    return parse_expression(rule_string)

def combine_rules(rules):
    if not rules:
        return None
    combined_ast = create_rule(rules[0])
    for rule in rules[1:]:
        combined_ast = Node(type="operator", left=combined_ast, right=create_rule(rule), value="OR")
    return combined_ast

def evaluate_rule(ast, data):
    if ast.type == "operand":
        condition = ast.value
        return eval(condition.replace(">", " > ").replace("<", " < ").replace("=", " == "), {}, data)
    elif ast.type == "operator":
        left_result = evaluate_rule(ast.left, data)
        right_result = evaluate_rule(ast.right, data)
        if ast.value == "AND":
            return left_result and right_result
        elif ast.value == "OR":
            return left_result or right_result
    return False
