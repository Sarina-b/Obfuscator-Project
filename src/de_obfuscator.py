
from ast_builder import ASTNode


class Deobfuscator:
    def __init__(self):
        self.rename_map = {}
        self.loop_names_pool = ["i", "j", "k", "m", "n"]
        self.local_names_counter = 1
        self.func_counter = 1

    def apply(self, ast: ASTNode):
        if ast is None:
            return None


        self._simplify_expressions(ast)

        used = self._collect_used_identifiers(ast)
        self._remove_dead_var_decls(ast, used)

        self._rename_identifiers_semantic(ast)

        return ast

    def _walk(self, node, fn):
        if node is None or not isinstance(node, ASTNode):
            return
        fn(node)
        for ch in node.children or []:
            self._walk(ch, fn)

    def _simplify_expressions(self, node):
        changed = True

        def is_unary_neg(n):
            return isinstance(n, ASTNode) and n.type in ("unop", "unary") and n.value == '-'

        def simplify_unary(n: ASTNode):
            nonlocal changed
            if not isinstance(n, ASTNode):
                return
            if n.type not in ("unop", "unary"):
                return
            if n.value != '-' or not n.children:
                return
            ch = n.children[0]
            if isinstance(ch, ASTNode) and ch.type == "int":
                n.type = "int"
                n.children = []
                n.value = -int(ch.value)
                changed = True
                return
            if isinstance(ch, ASTNode) and ch.type in ("unop", "unary") and ch.value == '-':
                inner = ch.children[0] if ch.children else None
                if isinstance(inner, ASTNode):
                    n.type = inner.type
                    n.value = inner.value
                    n.children = inner.children.copy() if inner.children else []
                    changed = True
                    simplify_unary(n)

        def simplify_binop(n: ASTNode):
            nonlocal changed
            if not isinstance(n, ASTNode) or n.type != "binop" or len(n.children) != 2:
                return
            left, right = n.children
            if isinstance(left, ASTNode):
                simplify_unary(left)
                simplify_binop(left)
            if isinstance(right, ASTNode):
                simplify_unary(right)
                simplify_binop(right)

            if n.value == '-' and is_unary_neg(right):
                inner = right
                while is_unary_neg(inner):
                    inner = inner.children[0] if inner.children else None
                if isinstance(inner, ASTNode):
                    n.value = '+'
                    n.children = [left, inner]
                    changed = True
                    simplify_binop(n)
                    return

            if isinstance(left, ASTNode) and isinstance(right, ASTNode):
                if left.type == "int" and right.type == "int":
                    a = int(left.value)
                    b = int(right.value)
                    if n.value == '+':
                        n.type, n.children, n.value = "int", [], a + b
                        changed = True
                        return
                    elif n.value == '-':
                        n.type, n.children, n.value = "int", [], a - b
                        changed = True
                        return
                    elif n.value == '*':
                        n.type, n.children, n.value = "int", [], a * b
                        changed = True
                        return

        def recurse(n: ASTNode):
            if n is None or not isinstance(n, ASTNode):
                return
            for ch in list(n.children or []):
                recurse(ch)
            if isinstance(n, ASTNode):
                if n.type in ("unop", "unary"):
                    simplify_unary(n)
                elif n.type == "binop":
                    simplify_binop(n)

        while changed:
            changed = False
            recurse(node)

    def _collect_used_identifiers(self, node):
        used = set()
        def visit(n: ASTNode):
            if n.type == "lvalue" and isinstance(n.value, str):
                name = n.value
                if '.' in name:
                    name = name.split('.')[0]
                used.add(name)
        self._walk(node, visit)
        return used

    def _remove_dead_var_decls(self, node, used):
        def visit(n: ASTNode):
            if n.type == "var_decl" and n.children and len(n.children) == 2:
                _, list_node = n.children
                if isinstance(list_node, ASTNode) and list_node.type == "var_list":
                    new_items = []
                    for item in list_node.children or []:
                        if not isinstance(item, ASTNode) or item.type != "var_item":
                            continue
                        if item.value in used:
                            new_items.append(item)
                    list_node.children = new_items
        self._walk(node, visit)

        def prune_empty(parent: ASTNode):
            if not parent.children: return
            pruned = []
            for ch in parent.children:
                if isinstance(ch, ASTNode) and ch.type == "var_decl":
                    var_list = ch.children[1] if len(ch.children) >= 2 else None
                    if isinstance(var_list, ASTNode) and var_list.type == "var_list" and len(var_list.children) == 0:
                        continue
                pruned.append(ch)
            parent.children = pruned

        self._walk(node, prune_empty)
    def _rename_identifiers_semantic(self, node: ASTNode):
        funcs = []
        params_per_func = {}
        locals_per_func = {}

        current_func = None

        def collect(n: ASTNode):
            nonlocal current_func
            if n.type == "function_decl":
                fname = f"func{self.func_counter}"
                self.func_counter += 1
                self.rename_map[n.value] = fname
                n.value = fname
                current_func = fname
                funcs.append(fname)

                params = []
                if n.children and len(n.children) >= 2:
                    params_node = n.children[1]
                    if isinstance(params_node, ASTNode) and params_node.type == "params":
                        for p in params_node.children or []:
                            if isinstance(p, ASTNode) and p.type == "param":
                                params.append(p.value)
                params_per_func[fname] = params

            elif n.type == "var_item" and current_func:
                locals_per_func.setdefault(current_func, []).append(n.value)

        self._walk(node, collect)

        if funcs:
            last_func = funcs[-1]
            self.rename_map[last_func] = "main"

        for f in funcs:
            for idx, p in enumerate(params_per_func.get(f, []), start=1):
                if p and p not in self.rename_map:
                    self.rename_map[p] = f"arg{idx}"

            local_counter = 1
            for loc in locals_per_func.get(f, []):
                if loc and loc not in self.rename_map:
                    self.rename_map[loc] = f"x{local_counter}"
                    local_counter += 1

        def apply_map(n: ASTNode):
            if n.type in ("var_item", "param", "lvalue", "call", "function_decl"):
                if isinstance(n.value, str) and n.value in self.rename_map:
                    n.value = self.rename_map[n.value]

        self._walk(node, apply_map)

