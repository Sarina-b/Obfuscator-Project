from ast_builder import ASTNode


class Deobfuscator:
    def __init__(self):
        self.rename_map = {}
        self.loop_names_pool = ["i", "j", "k", "m", "n"]
        self.local_names_counter = 1
        self.func_counter = 1