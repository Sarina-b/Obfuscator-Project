import random
import string
from .ast_builder import ASTNode


class Obfuscator:
    def __init__(self):
        self.name_map = {}

    def random_name(self):
        return ''.join(random.choices(string.ascii_lowercase, k=6))

    def rename_identifiers(self, node):
        if node is None:
            return

        # Fix: Separate 'id' cases when node.value is tuple or not
        if node.type in ('var_decl', 'param') and isinstance(node.value, tuple):
            typename, name = node.value
            if name not in self.name_map:
                self.name_map[name] = self.random_name()
            node.value = (typename, self.name_map[name])
        elif node.type == 'id' and isinstance(node.value, str):
            name = node.value
            if name not in self.name_map:
                self.name_map[name] = self.random_name()
            node.value = self.name_map[name]
        elif node.type == 'function_def':
            if node.value not in self.name_map:
                self.name_map[node.value] = self.random_name()
            node.value = self.name_map[node.value]

        for child in node.children:
            self.rename_identifiers(child)

    def insert_dead_code(self, node):
        if node is None:
            return
        if node.type == 'block':
            dead_var = self.random_name()
            node.children.insert(0, ASTNode("var_decl", [], ("int", dead_var)))
        for child in node.children:
            self.insert_dead_code(child)

    def expression_equivalence(self, node):
        if node is None:
            return
        if node.type == 'binop' and node.value == '+':
            left, right = node.children
            right_neg = ASTNode("int", [], -right.value) if right.type == "int" else right
            node.type = 'binop'
            node.value = '-'
            node.children = [left, right_neg]
        for child in node.children:
            self.expression_equivalence(child)

    def control_flow_flattening(self, node):
        if node is None:
            return
        if node.type == 'function_def':
            label1 = ASTNode('label', [], 'L1')
            label2 = ASTNode('label', [], 'L2')
            node.children.append(ASTNode('switch_block', [label1, label2]))
        for child in node.children:
            self.control_flow_flattening(child)

    def apply(self, ast):
        self.rename_identifiers(ast)
        self.insert_dead_code(ast)
        self.expression_equivalence(ast)
        self.control_flow_flattening(ast)
        return ast
