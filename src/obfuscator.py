# obfuscator.py
import random
import string


class Obfuscator:
    def __init__(self, ast_root):
        self.ast_root = ast_root
        self.variable_map = {}  # For renaming
        self.function_map = {}  # For renaming
        self.used_names = set()

    def _generate_random_name(self, length=5):
        name = ''.join(random.choice(string.ascii_lowercase) for _ in range(length))
        while name in self.used_names:  # Ensure uniqueness
            name = ''.join(random.choice(string.ascii_lowercase) for _ in range(length))
        self.used_names.add(name)
        return name

    def obfuscate(self):
        # Apply techniques in order or selectively
        self._rename_identifiers(self.ast_root)
        self._insert_dead_code(self.ast_root)
        self._flatten_control_flow(self.ast_root)  # This is complex
        self._apply_equivalent_expressions(self.ast_root)
        return self.ast_root

    def _rename_identifiers(self, node):
        # Traverse AST. When FunctionDeclarationNode or VariableDeclarationNode is found,
        # map original name to a new random name.
        # When IdentifierNode (usage of var/func) is found, replace its name with mapped name.
        # Needs careful scope management if you have nested scopes.
        # For simplicity, one global map for functions, and per-function maps for vars.
        if isinstance(node, FunctionDeclarationNode):
            original_name = node.name
            if original_name not in self.function_map and original_name != "main":  # Don't rename main usually
                self.function_map[original_name] = self._generate_random_name()
            node.name = self.function_map.get(original_name, original_name)
            # Rename parameters
            for param in node.params:
                original_param_name = param.name
                # param_map per function scope
                # param.name = new_param_name
            self._rename_identifiers(node.body)  # Recurse

        elif isinstance(node, VariableDeclarationNode):
            original_name = node.name
            # Use a scope-specific map if you implement scopes
            if original_name not in self.variable_map:  # Simplified: one map for demo
                self.variable_map[original_name] = self._generate_random_name()
            node.name = self.variable_map[original_name]
            if node.initializer:
                self._rename_identifiers(node.initializer)

        elif isinstance(node, IdentifierNode):  # When using a variable
            if node.name in self.variable_map:
                node.name = self.variable_map[node.name]

        elif isinstance(node, FunctionCallNode):
            if node.name in self.function_map:
                node.name = self.function_map[node.name]
            for arg in node.args:
                self._rename_identifiers(arg)

        # ... recurse for other node types that contain identifiers or sub-nodes
        elif hasattr(node, 'children'):  # Generic traversal for composite nodes
            for child in node.children:
                self._rename_identifiers(child)
        elif isinstance(node, ProgramNode):
            for item in node.declarations_and_functions:
                self._rename_identifiers(item)
        # ... (add more specific traversals for other node types)

    def _insert_dead_code(self, node):
        # Traverse AST. In suitable places (e.g., beginning of blocks),
        # insert new AST nodes for dead code (e.g., VariableDeclarationNode for an unused var).
        if isinstance(node, BlockNode):  # Assuming BlockNode has a 'statements' list
            dead_var_name = self._generate_random_name(prefix="unused_")
            dead_code_decl = VariableDeclarationNode('int', dead_var_name, LiteralNode(random.randint(100, 1000)))
            node.statements.insert(0, dead_code_decl)  # Insert at the beginning

        # Recurse for other nodes
        # ...

    def _flatten_control_flow(self, node):
        # This is complex. Identify sequences of statements or simple control structures.
        # Transform them into a state machine using a while loop and switch statement.
        # Example: Transform a function's body.
        if isinstance(node, FunctionDeclarationNode) and node.name == "main":  # Example: flatten main
            # 1. Create a state variable (e.g., 'selector_var')
            # 2. Enclose original body statements in a while(selector_var > 0) { switch(selector_var) {...} }
            # 3. Each original block/statement becomes a case.
            # 4. Update selector_var to control flow.
            # This requires significant AST restructuring.
            pass  # Placeholder for complex logic

    def _apply_equivalent_expressions(self, node):
        # Traverse AST. Find BinaryOpNode.
        # Replace expressions like 'a + b' with 'a - (-b)' or 'a * 1' with 'a * (c/c)'.
        if isinstance(node, BinaryOpNode):
            if node.operator == '+':
                # Example: a + b -> a - (-b)
                # Ensure 'b' (node.right) can be negated.
                # This might require type information or assumptions.
                # For simplicity, assume int for now.
                # node.operator = '-'
                # node.right = UnaryOpNode('-', node.right) # Need UnaryOpNode in AST
                pass  # Placeholder for this transformation
            # Add more transformations:
            # a = b + 1  =>  a = b - (-1)
            # a == b     =>  !(a != b)
            # a * 2      =>  a << 1 (if integers)

        # Recurse for other nodes
        # ...