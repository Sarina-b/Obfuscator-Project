from antlr_gen.MiniCVisitor import MiniCVisitor

class ASTNode:
    def __init__(self, type_, children=None, value=None):
        self.type = type_
        self.children = children or []
        self.value = value

    def __repr__(self, level=0):
        indent = "  " * level
        if self.value is None:
            rep = f"{indent}{self.type}\n"
        else:
            rep = f"{indent}{self.type}({self.value})\n"
        for child in self.children:
            if isinstance(child, ASTNode):
                rep += child.__repr__(level + 1)
            else:
                rep += f"{indent}  {repr(child)}\n"
        return rep

class ASTBuilder(MiniCVisitor):
    def __init__(self):
        super().__init__()

    def visit(self, ctx):
        print(f"Visiting node type: {type(ctx).__name__}")
        method_name = 'visit' + type(ctx).__name__.replace('Context', '')
        visitor = getattr(self, method_name, self.generic_visit)
        return visitor(ctx)

    def generic_visit(self, ctx):
        print(f"Generic visit for {type(ctx).__name__}")
        return self.visitChildren(ctx)

    def visitProgram(self, ctx):
        children = []
        for func_ctx in ctx.functionDecl():
            print(f"Visiting functionDecl: {func_ctx.getText()[:50]}")
            func_ast = self.visit(func_ctx)
            if func_ast:
                children.append(func_ast)
        ast_node = ASTNode("program", children)
        return ast_node

    def visitFunctionDecl(self, ctx):
        # فرض می‌کنیم ساختار تو اینه: typ ID '(' paramList? ')' block
        name = ctx.ID().getText()
        typename = self.visit(ctx.typ())
        params = self.visit(ctx.paramList()) if ctx.paramList() else ASTNode("params", [])
        body = self.visit(ctx.block())
        print(f"Visiting FunctionDecl: {name}")
        return ASTNode("function_decl", [typename, params, body], name)

    def visitTyp(self, ctx):
        # typ -> baseType pointerType*
        base = self.visit(ctx.baseType())
        pointers = [ASTNode("pointer") for _ in ctx.pointerType()]
        return ASTNode("type", pointers, base.value)

    def visitBaseType(self, ctx):
        return ASTNode("base_type", [], ctx.getText())

    def visitParamList(self, ctx):
        params = [self.visit(param) for param in ctx.param()]
        return ASTNode("params", params)

    def visitParam(self, ctx):
        typename = self.visit(ctx.typ())
        name = ctx.ID().getText()
        return ASTNode("param", [typename], name)

    def visitBlock(self, ctx):
        stmts = []
        for stmt in ctx.statement():
            node = self.safe_visit(stmt)
            if node is not None:
                stmts.append(node)
        return ASTNode("block", stmts)

    def visitVarDecl(self, ctx):
        typename = self.visit(ctx.typ())
        var_list = self.visit(ctx.varDeclList())
        return ASTNode("var_decl", [typename, var_list])

    def visitVarDeclList(self, ctx):
        items = [self.visit(item) for item in ctx.varDeclItem()]
        return ASTNode("var_list", items)

    def visitVarDeclItem(self, ctx):
        name = ctx.ID().getText()
        expr = self.visit(ctx.expression()) if ctx.expression() else None
        children = [expr] if expr else []
        return ASTNode("var_item", children, name)

    def visitExpression(self, ctx):
        # چک کردن باینری اپراتورها
        if len(ctx.expression()) == 2:
            left = self.visit(ctx.expression(0))
            right = self.visit(ctx.expression(1))
            op = ctx.getChild(1).getText()
            return ASTNode("binop", [left, right], op)
        elif len(ctx.expression()) == 1 and ctx.unaryOp():
            expr = self.visit(ctx.expression(0))
            op = ctx.unaryOp().getText()
            return ASTNode("unop", [expr], op)
        elif ctx.literal():
            return self.visit(ctx.literal())
        elif ctx.funcCall():
            return self.visit(ctx.funcCall())
        elif ctx.lvalue():
            return self.visit(ctx.lvalue())
        elif ctx.getChildCount() == 3 and ctx.getChild(0).getText() == '(':
            return self.visit(ctx.expression(0))
        else:
            return ASTNode("unknown", [], ctx.getText())

    def visitLiteral(self, ctx):
        if ctx.INT():
            return ASTNode("int", [], int(ctx.INT().getText()))
        elif ctx.CHAR():
            return ASTNode("char", [], ctx.CHAR().getText())
        elif ctx.BOOL():
            return ASTNode("bool", [], ctx.BOOL().getText())

    def visitLvalue(self, ctx):
        return ASTNode("lvalue", [], ctx.getText())

    def visitAssignStat(self, ctx):
        target = self.visit(ctx.lvalue())
        expr = self.visit(ctx.expression())
        return ASTNode("assign", [target, expr])

    def safe_visit(self, ctx):
        if ctx is None:
            return None
        node = self.visit(ctx)
        return node

    def visitIfStat(self, ctx):
        cond = self.safe_visit(ctx.expression())
        then_stmt = self.safe_visit(ctx.statement(0))
        else_stmt = self.safe_visit(ctx.statement(1)) if ctx.statement(1) else None

        children = []
        if cond is not None:
            children.append(cond)
        if then_stmt is not None:
            children.append(then_stmt)
        if else_stmt is not None:
            children.append(else_stmt)

        return ASTNode("if", children)

    def visitReturnStat(self, ctx):
        expr = self.safe_visit(ctx.expression()) if ctx.expression() else None
        children = [expr] if expr is not None else []
        return ASTNode("return", children)

    def visitWhileStat(self, ctx):
        cond = self.visit(ctx.expression())
        body = self.visit(ctx.statement())
        return ASTNode("while", [cond, body])

    def visitForStat(self, ctx):
        init = self.safe_visit(ctx.varDecl()) if ctx.varDecl() else None
        if not init and ctx.assignStat():
            init = self.safe_visit(ctx.assignStat())

        cond = self.safe_visit(ctx.expression(0)) if ctx.expression(0) else None
        update = self.safe_visit(ctx.expression(1)) if ctx.expression(1) else None
        body = self.safe_visit(ctx.statement())

        children = []
        for node in [init, cond, update, body]:
            if node is not None:
                children.append(node)

        return ASTNode("for", children)

    def visitStructDecl(self, ctx):
        name = ctx.ID().getText()
        fields = []
        for var_decl_ctx in ctx.varDecl():
            field_node = self.visit(var_decl_ctx)
            if field_node is not None:
                fields.append(field_node)
        return ASTNode("struct_decl", fields, name)

    def visitFuncCall(self, ctx):
        name = ctx.ID().getText()
        args = self.visit(ctx.argumentList()) if ctx.argumentList() else ASTNode("args", [])
        return ASTNode("call", args.children, name)

    def visitArgumentList(self, ctx):
        args = [self.visit(expr) for expr in ctx.expression()]
        return ASTNode("args", args)

    def visitIoStat(self, ctx):
        op = ctx.start.text
        exprs = []
        if ctx.ID():
            exprs.append(ASTNode("id", [], ctx.ID().getText()))
        if ctx.expressionList():
            exprs.extend([self.visit(e) for e in ctx.expressionList().expression()])
        return ASTNode("io", exprs, op)

    def visitStatement(self, ctx):
        if ctx.varDecl():
            return self.visit(ctx.varDecl())
        elif ctx.assignStat():
            return self.visit(ctx.assignStat())
        elif ctx.ifStat():
            return self.visit(ctx.ifStat())
        elif ctx.returnStat():
            return self.visit(ctx.returnStat())
        elif ctx.block():
            return self.visit(ctx.block())
        elif ctx.forStat():
            return self.visit(ctx.forStat())
        elif ctx.whileStat():
            return self.visit(ctx.whileStat())
        elif ctx.ioStat():
            return self.visit(ctx.ioStat())
        else:
            print("Unknown statement:", ctx.getText())
            return None

