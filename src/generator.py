def generate_code(node, indent=0):
    space = '    ' * indent

    if node.type == 'program':
        return '\n'.join(generate_code(child, indent) for child in node.children)

    elif node.type == 'var_decl':
        typename, name = node.value
        return f"{space}{typename} {name};"

    elif node.type == 'function_def':
        name = node.value
        params = generate_code(node.children[0])
        body = generate_code(node.children[1], indent)
        return f"{space}int {name}({params}) {{\n{body}\n{space}}}"

    elif node.type == 'params':
        return ', '.join(generate_code(child) for child in node.children)

    elif node.type == 'param':
        typename, name = node.value
        return f"{typename} {name}"

    elif node.type == 'block':
        return '\n'.join(generate_code(child, indent + 1) for child in node.children)

    elif node.type == 'return':
        if node.children:
            expr = generate_code(node.children[0])
            return f"{space}return {expr};"
        else:
            return f"{space}return;"

    elif node.type == 'if':
        cond = generate_code(node.children[0])
        then_stmt = generate_code(node.children[1], indent)
        if len(node.children) > 2:
            else_stmt = generate_code(node.children[2], indent)
            return f"{space}if ({cond}) {{\n{then_stmt}\n{space}}} else {{\n{else_stmt}\n{space}}}"
        else:
            return f"{space}if ({cond}) {{\n{then_stmt}\n{space}}}"

    elif node.type == 'expr_stmt':
        if node.children:
            expr = generate_code(node.children[0])
            return f"{space}{expr};"
        else:
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
        return 'true' if node.value else 'false'

    elif node.type == 'label':
        return f"{space}// label: {node.value}"

    elif node.type == 'switch_block':
        label1, label2 = node.children
        return f"""{space}int selector = 1;
{space}while (selector > 0) {{
{space}    switch (selector) {{
{space}        case 1:
{space}            selector = 2;
{space}            break;
{space}        case 2:
{space}            selector = 0;
{space}            break;
{space}    }}
}}"""

    else:
        return f"{space}// [UNHANDLED NODE: {node.type}]"
