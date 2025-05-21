def generate_code(node, indent=0):
    space = '    ' * indent

    if node is None:
        return ""

    if isinstance(node, list):
        return '\n'.join(generate_code(child, indent) for child in node if child is not None)

    children = getattr(node, 'children', [])
    value = getattr(node, 'value', None)
    node_type = getattr(node, 'type', None)

    if node_type == 'program':
        return '\n'.join(generate_code(child, indent) for child in children)

    elif node_type == 'function_def':
        params = generate_code(children[0]) if len(children) > 0 else ''
        body = generate_code(children[1], indent + 1) if len(children) > 1 else ''
        return f"{space}int {value}({params}) {{\n{body}\n{space}}}"

    elif node_type == 'params':
        return ', '.join(generate_code(child) for child in children)

    elif node_type == 'param':
        if isinstance(value, tuple):
            typename, name = value
            return f"{typename} {name}"
        return ""

    elif node_type == 'var_decl':
        if isinstance(value, tuple):
            typename, name = value
            return f"{space}{typename} {name};"
        return ""

    elif node_type == 'block':
        return '\n'.join(generate_code(child, indent) for child in children)

    elif node_type == 'return':
        if children:
            return f"{space}return {generate_code(children[0])};"
        return f"{space}return;"

    elif node_type == 'expr_stmt':
        if children:
            return f"{space}{generate_code(children[0])};"
        return f"{space};"

    elif node_type == 'assign':
        left = generate_code(children[0]) if len(children) > 0 else ''
        right = generate_code(children[1]) if len(children) > 1 else ''
        return f"{left} = {right}"

    elif node_type == 'binop':
        left = generate_code(children[0]) if len(children) > 0 else ''
        right = generate_code(children[1]) if len(children) > 1 else ''
        return f"({left} {value} {right})"

    elif node_type == 'id':
        return str(value)

    elif node_type == 'int':
        return str(value)

    elif node_type == 'char':
        return repr(value)

    elif node_type == 'bool':
        return str(value).lower()

    elif node_type == 'if':
        cond = generate_code(children[0]) if len(children) > 0 else ''
        then_branch = generate_code(children[1], indent + 1) if len(children) > 1 else ''
        result = f"{space}if ({cond}) {{\n{then_branch}\n{space}}}"
        if len(children) > 2:
            else_branch = generate_code(children[2], indent + 1)
            result += f" else {{\n{else_branch}\n{space}}}"
        return result

    elif node_type == 'label':
        return f"{space}label: // {value}"

    elif node_type == 'switch_block':
        return f"{space}// control flow flattening placeholder"

    else:
        return f"{space}// unhandled: {node_type}"
