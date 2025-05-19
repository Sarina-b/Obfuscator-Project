import random
import string


class Obfuscator:
    def __init__(self):
        self.name_map = {}

    def random_name(self):
        return ''.join(random.choices(string.ascii_lowercase, k=6))

    def rename_identifiers(self, node):
        if node.type in ('var_decl', 'param', 'id') and isinstance(node.value, tuple):
            typename, name = node.value
            if name not in self.name_map:
                self.name_map[name] = self.random_name()
            node.value = (typename, self.name_map[name])
        elif node.type == 'id':
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
