# generator.py

class CodeGenerator:  # Could also be an AST Visitor
    def generate(self, node):
        if isinstance(node, ProgramNode):
            return "\n".join(self.generate(item) for item in node.declarations_and_functions)

        elif isinstance(node, FunctionDeclarationNode):
            params_str = ", ".join(f"{p.type} {p.name}" for p in node.params)  # Assuming ParamNode has type and name
            body_str = self.generate(node.body)
            return f"{node.return_type} {node.name}({params_str}) {body_str}"

        elif isinstance(node, BlockNode):  # Assuming BlockNode has 'statements' list
            stmts_str = "\n  ".join(self.generate(stmt) + ";" for stmt in node.statements)
            return f"{{\n  {stmts_str}\n}}"

        elif isinstance(node, VariableDeclarationNode):
            init_str = ""
            if node.initializer:
                init_str = f" = {self.generate(node.initializer)}"
            return f"{node.var_type} {node.name}{init_str}"

        elif isinstance(node, AssignmentNode):
            return f"{self.generate(node.identifier)} = {self.generate(node.expression)}"

        elif isinstance(node, IdentifierNode):
            return node.name

        elif isinstance(node, LiteralNode):  # Assuming LiteralNode has 'value'
            # Handle different types of literals (int, char, bool) appropriately
            if isinstance(node.value, str) and node.type == 'char':  # Example for char
                return f"'{node.value}'"
            return str(node.value)

        elif isinstance(node, BinaryOpNode):
            return f"({self.generate(node.left)} {node.operator} {self.generate(node.right)})"

        elif isinstance(node, PrintfNode):  # Assuming PrintfNode has format_string and args
            args_str = ", ".join(self.generate(arg) for arg in node.args)
            return f'printf("{node.format_string}", {args_str})'

        # ... implement generate methods for all your AST node types
        # (IfStatementNode, WhileStatementNode, ForStatementNode, ReturnStatementNode, etc.)

        else:
            raise TypeError(f"Cannot generate code for AST node of type: {type(node)}")