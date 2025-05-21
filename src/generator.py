def generate_code(node, indent=0):
    space = '    ' * indent
    if node is None:
        return ''

    if isinstance(node, list):
        return '\n'.join(generate_code(child, indent) for child in node if child)

    if node is not None:
        t = node.type
        c = node.children
        v = node.value
    else:
        t = c = v = None

    if t == "program":
        return '\n\n'.join(generate_code(child, indent) for child in c)

    elif t == "function_decl":
        typename = generate_code(c[0])
        params = generate_code(c[1])
        body = generate_code(c[2], indent)
        return f"{typename} {v}({params}) {{\n{body}\n}}"

    elif t == "params":
        return ', '.join(generate_code(child) for child in c)

    elif t == "param":
        typename = generate_code(c[0])
        return f"{typename} {v}"

    elif t == "type":
        return v + '*' * len(c)

    elif t == "struct_decl":
        fields = '\n'.join(generate_code(field, indent + 1) for field in c)
        return f"struct {v} {{\n{fields}\n}};"

    elif t == "var_decl":
        typename = generate_code(c[0])
        varlist = generate_code(c[1])
        return f"{space}{typename} {varlist};"

    elif t == "var_list":
        return ', '.join(generate_code(child) for child in c)

    elif t == "var_item":
        return f"{v} = {generate_code(c[0])}" if c else v

    elif t == "block":
        return '\n'.join(generate_code(stmt, indent + 1) for stmt in c)

    elif t == "assign":
        return f"{space}{generate_code(c[0])} = {generate_code(c[1])};"

    elif t == "return":
        return f"{space}return {generate_code(c[0])};" if c else f"{space}return;"

    elif t == "if":
        cond = generate_code(c[0])
        then_ = generate_code(c[1], indent + 1)
        code = f"{space}if ({cond}) {{\n{then_}\n{space}}}"
        if len(c) == 3:
            else_ = generate_code(c[2], indent + 1)
            code += f" else {{\n{else_}\n{space}}}"
        return code

    elif t == "while":
        cond = generate_code(c[0])
        body = generate_code(c[1], indent + 1)
        return f"{space}while ({cond}) {{\n{body}\n{space}}}"

    elif t == "for":
        init = generate_code(c[0]) if c[0] else ''
        cond = generate_code(c[1]) if c[1] else ''
        update = generate_code(c[2]) if c[2] else ''
        body = generate_code(c[3], indent + 1)
        return f"{space}for ({init} {cond}; {update}) {{\n{body}\n{space}}}"

    elif t == "call":
        args = ', '.join(generate_code(arg) for arg in c)
        return f"{space}{v}({args});"

    elif t == "lvalue":
        return v

    elif t == "binop":
        return f"({generate_code(c[0])} {v} {generate_code(c[1])})"

    elif t == "unop":
        return f"({v}{generate_code(c[0])})"

    elif t == "int":
        return str(v)

    elif t == "char":
        return v

    elif t == "bool":
        return v.lower()

    elif t == "args":
        return ', '.join(generate_code(arg) for arg in c)

    elif t == "io":
        args = ', '.join(generate_code(arg) for arg in c)
        return f"{space}{v}({args});"

    else:
        return f"{space}// [unhandled: {t}]"