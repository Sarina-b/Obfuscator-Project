import random
import string
from ast_builder import ASTNode


class Obfuscator:
    def __init__(self):
        self.name_map = {}

    def random_name(self):
        return ''.join(random.choices(string.ascii_lowercase, k=6))

    def rename_identifiers(self, node):
        if node is None or not isinstance(node, ASTNode):
            return


        if node.type == 'function_decl':
            if node.value and node.value not in self.name_map:
                self.name_map[node.value] = self.random_name()
            node.value = self.name_map.get(node.value, node.value)

        elif node.type == 'param':
            if node.value and node.value not in self.name_map:
                self.name_map[node.value] = self.random_name()
            node.value = self.name_map.get(node.value, node.value)

        elif node.type == 'var_item':
            if node.value and node.value not in self.name_map:
                self.name_map[node.value] = self.random_name()
            node.value = self.name_map.get(node.value, node.value)

        elif node.type == 'lvalue':
            if node.value in self.name_map:
                node.value = self.name_map[node.value]

        elif node.type == 'call':
            if node.value in self.name_map:
                node.value = self.name_map[node.value]

        for child in node.children or []:
            self.rename_identifiers(child)

    def insert_dead_code(self, node):
        if node is None or not isinstance(node, ASTNode):
            return

        if node.type == 'block':
            dead_var = self.random_name()
            decl = ASTNode("var_decl", [
                ASTNode("type", [], "int"),
                ASTNode("var_list", [
                    ASTNode("var_item", [], dead_var)
                ])
            ])
            node.children.insert(0, decl)

        for child in node.children or []:
            self.insert_dead_code(child)

    def expression_equivalence(self, node):
        if node is None or not isinstance(node, ASTNode):
            return

        if node.type == 'binop' and node.value == '+':
            if len(node.children) == 2:
                left, right = node.children
                if right and right.type == 'int' and isinstance(right.value, int):
                    node.value = '-'
                    node.children = [left, ASTNode("int", [], -right.value)]

        for child in node.children or []:
            self.expression_equivalence(child)

    def control_flow_flattening(self, node):
        if node is None or not isinstance(node, ASTNode):
            return

        if node.type == 'function_decl':
            label = ASTNode('label', [], self.random_name())
            node.children.append(label)

        for child in node.children or []:
            self.control_flow_flattening(child)

    def apply(self, ast):
        self.rename_identifiers(ast)
        self.insert_dead_code(ast)
        self.expression_equivalence(ast)
        self.control_flow_flattening(ast)
        return ast
