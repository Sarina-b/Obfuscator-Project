from antlr_gen.MiniCVisitor import MiniCVisitor

class ASTNode:
    def __init__(self, type_, children=None, value=None):
        self.type = type_
        self.children = children or []
        self.value = value

    def __repr__(self):
        return f"{self.type}({self.value}) -> {self.children}"


class ASTBuilder(MiniCVisitor):
    def visitProgram(self, ctx):
        print(f"[DEBUG] Visiting Program")
        for child in ctx.children:
            print(f"Child type: {type(child)}, Text: {child.getText()}")
        children = [self.visit(child) for child in ctx.children if child.getText() != '<EOF>']
        return ASTNode("program", children)

    def visitFunctionDecl(self, ctx):
        print("[DEBUG] visiting FunctionDecl")
        name = ctx.ID().getText()
        typename = self.visit(ctx.typ())
        params = self.visit(ctx.paramList()) if ctx.paramList() else ASTNode("params", [])
        body = self.visit(ctx.block())
        return ASTNode("function_decl", [params, body], name)

    def visitTyp(self, ctx):
        base = self.visit(ctx.baseType())
        pointers = [self.visit(p) for p in ctx.pointerType()]
        return ASTNode("type", pointers, base.value)

    def visitBaseType(self, ctx):
        return ASTNode("base_type", [], ctx.getText())

    def visitPointerType(self, ctx):
        return ASTNode("pointer", [])

    def visitVarDecl(self, ctx):
        typename = self.visit(ctx.typ())
        var_list = self.visit(ctx.varDeclList())
        return ASTNode("var_decl", [typename, var_list])

    def visitVarDeclList(self, ctx):
        return ASTNode("var_list", [self.visit(item) for item in ctx.varDeclItem()])

    def visitVarDeclItem(self, ctx):
        name = ctx.ID().getText()
        expr = self.visit(ctx.expression()) if ctx.expression() else None
        return ASTNode("var_item", [expr] if expr else [], name)

    def visitParamList(self, ctx):
        return ASTNode("params", [self.visit(p) for p in ctx.param()])

    def visitParam(self, ctx):
        typename = self.visit(ctx.typ())
        name = ctx.ID().getText()
        return ASTNode("param", [typename], name)

    def visitBlock(self, ctx):
        stmts = [self.visit(stmt) for stmt in ctx.statement()]
        return ASTNode("block", stmts)

    def visitAssignStat(self, ctx):
        target = self.visit(ctx.lvalue())
        expr = self.visit(ctx.expression())
        return ASTNode("assign", [target, expr])

    def visitReturnStat(self, ctx):
        expr = self.visit(ctx.expression()) if ctx.expression() else None
        return ASTNode("return", [expr] if expr else [])

    def visitIfStat(self, ctx):
        cond = self.visit(ctx.expression())
        then_stmt = self.visit(ctx.statement(0))
        else_stmt = self.visit(ctx.statement(1)) if ctx.statement(1) else None
        return ASTNode("if", [cond, then_stmt] + ([else_stmt] if else_stmt else []))

    def visitWhileStat(self, ctx):
        cond = self.visit(ctx.expression())
        body = self.visit(ctx.statement())
        return ASTNode("while", [cond, body])

    def visitForStat(self, ctx):
        init = self.visit(ctx.varDecl()) if ctx.varDecl() else (self.visit(ctx.assignStat()) if ctx.assignStat() else None)
        cond = self.visit(ctx.expression(0)) if ctx.expression(0) else None
        update = self.visit(ctx.expression(1)) if ctx.expression(1) else None
        body = self.visit(ctx.statement())
        return ASTNode("for", [init, cond, update, body])

    def visitFuncCall(self, ctx):
        name = ctx.ID().getText()
        args = self.visit(ctx.argumentList()) if ctx.argumentList() else []
        return ASTNode("call", args.children if isinstance(args, ASTNode) else [], name)

    def visitArgumentList(self, ctx):
        return ASTNode("args", [self.visit(e) for e in ctx.expression()])

    def visitLvalue(self, ctx):
        return ASTNode("lvalue", [], ctx.getText())

    def visitLiteral(self, ctx):
        if ctx.INT():
            return ASTNode("int", [], int(ctx.INT().getText()))
        elif ctx.CHAR():
            return ASTNode("char", [], ctx.CHAR().getText())
        elif ctx.BOOL():
            return ASTNode("bool", [], ctx.BOOL().getText())

    def visitExpression(self, ctx):
        if ctx.getChildCount() == 3 and ctx.getChild(1).getText() in ['+', '-', '*', '/', '%', '==', '!=', '<', '<=', '>', '>=', '&&', '||']:
            left = self.visit(ctx.getChild(0))
            op = ctx.getChild(1).getText()
            right = self.visit(ctx.getChild(2))
            return ASTNode("binop", [left, right], op)
        elif ctx.getChildCount() == 2 and ctx.getChild(0).getText() in ['-', '!']:
            op = ctx.getChild(0).getText()
            expr = self.visit(ctx.getChild(1))
            return ASTNode("unop", [expr], op)
        elif ctx.getChildCount() == 3 and ctx.getChild(0).getText() == '(':
            return self.visit(ctx.getChild(1))
        else:
            return self.visit(ctx.getChild(0))

    def visitChildren(self, node):
        return [self.visit(child) for child in node.getChildren()]