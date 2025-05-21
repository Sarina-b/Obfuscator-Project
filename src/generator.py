def generate_code(node, indent=0):
    space = '    ' * indent

    if node.type == 'program':
        return '\n'.join(generate_code(child, indent) for child in node.children)

    elif node.type == 'function_def':
        params = generate_code(node.children[0])
        body = generate_code(node.children[1], indent + 1)
        return f"{space}int {node.value}({params}) {{\n{body}\n{space}}}"

    elif node.type == 'params':
        return ', '.join(generate_code(child) for child in node.children)

    elif node.type == 'param':
        typename, name = node.value
        return f"{typename} {name}"

    elif node.type == 'var_decl':
        typename, name = node.value
        return f"{space}{typename} {name};"

    elif node.type == 'block':
        return '\n'.join(generate_code(child, indent) for child in node.children)

    elif node.type == 'return':
        if node.children:
            return f"{space}return {generate_code(node.children[0])};"
        return f"{space}return;"

    elif node.type == 'expr_stmt':
        if node.children:
            return f"{space}{generate_code(node.children[0])};"
        return f"{space};"

    elif node.type == 'assign':
        left = generate_code(node.children[0])
        right = generate_code(node.children[1])
        return f"{left} = {right}"

    elif node.type == 'binop':
        left = generate_code(node.children[0])
        right = generate_code(node.children[1])
        return f"({left} {node.value} {right})"

    elif node.type == 'id':
        return node.value

    elif node.type == 'int':
        return str(node.value)

    elif node.type == 'char':
        return node.value

    elif node.type == 'bool':
        return node.value

    elif node.type == 'if':
        cond = generate_code(node.children[0])
        then_branch = generate_code(node.children[1], indent + 1)
        result = f"{space}if ({cond}) {{\n{then_branch}\n{space}}}"
        if len(node.children) > 2:
            else_branch = generate_code(node.children[2], indent + 1)
            result += f" else {{\n{else_branch}\n{space}}}"
        return result

    elif node.type == 'label':
        return f"{space}label: // {node.value}"

    elif node.type == 'switch_block':
        # Placeholder output
        return f"{space}// control flow flattening placeholder"

    else:
        return f"{space}// unhandled: {node.type}"
