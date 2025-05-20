def generate_code(node, indent=0):
    space = '    '      *
    if node.type == 'program':
        return '\n'.join(generate_code(child, indent) for child in node.children)
    elif node.type == 'function_def':
        header = f"int {node.value}()"  # فرض بر نوع int بدون پارامتر
        body = generate_code(node.children[1], indent)
        return f"{header} {{\n{body}\n}}"
    elif node.type == 'block':
        return '\n'.join(generate_code(child, indent + 1) for child in node.children)
    elif node.type == 'var_decl':
        typ, name = node.value
        return f"{space}{typ} {name};"
    elif node.type == 'return':
        expr = generate_code(node.children[0], 0) if node.children else ''
        return f"{space}return {expr};"
    elif node.type == 'assign':
        left = generate_code(node.children[0], 0)
        right = generate_code(node.children[1], 0)
        return f"{space}{left} = {right};"
    elif node.type == 'binop':
        left = generate_code(node.children[0], 0)
        right = generate_code(node.children[1], 0)
        return f"({left} {node.value} {right})"
    elif node.type == 'id':
        return node.value
    elif node.type == 'int':
        return str(node.value)
    elif node.type == 'expr_stmt':
        expr = generate_code(node.children[0], 0) if node.children else ''
        return f"{space}{expr};"
    elif node.type == 'if':
        cond = generate_code(node.children[0], 0)
        then_stmt = generate_code(node.children[1], indent)
        code = f"{space}if ({cond}) {then_stmt}"
        if len(node.children) > 2:
            else_stmt = generate_code(node.children[2], indent)
            code += f" else {else_stmt}"
        return code
    elif node.type == 'switch_block':
        return f"{space}// control flow flattened"
    elif node.type == 'label':
        return f"{space}// label: {node.value}"
    else:
        return f"{space}// unknown node: {node.type}"