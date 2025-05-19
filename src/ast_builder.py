from antlr_gen.MiniCParserVisitor import MiniCParserVisitor
from antlr_gen.MiniCParserParser import *

class ASTNode:
    def __init__(self, type_, children=None, value=None):
        self.type = type_
        self.children = children or []
        self.value = value

    def __repr__(self):
        return f"{self.type}({self.value}) -> {self.children}"


class ASTBuilder(MiniCParserVisitor):
    def visitProgram(self, ctx):
        children = [self.visit(child) for child in ctx.children if child.getText() != '<EOF>']
        return ASTNode("program", children)

    def visitDeclaration(self, ctx):
        typename = ctx.type_().getText()
        name = ctx.declarator().ID().getText()
        return ASTNode("var_decl", [], (typename, name))

    def visitFunctionDef(self, ctx):
        typename = ctx.type_().getText()
        name = ctx.ID().getText()
        params = self.visit(ctx.parameters()) if ctx.parameters() else ASTNode("params", [])
        body = self.visit(ctx.block())
        return ASTNode("function_def", [params, body], name)

    def visitParameters(self, ctx):
        return ASTNode("params", [self.visit(p) for p in ctx.parameter()])

    def visitParameter(self, ctx):
        typename = ctx.type_().getText()
        name = ctx.declarator().ID().getText()
        return ASTNode("param", [], (typename, name))

    def visitBlock(self, ctx):
        stmts = [self.visit(stmt) for stmt in ctx.statement()]
        return ASTNode("block", stmts)

    def visitReturnStatement(self, ctx):
        expr = self.visit(ctx.expression()) if ctx.expression() else None
        return ASTNode("return", [expr] if expr else [])

    def visitIfStatement(self, ctx):
        cond = self.visit(ctx.expression())
        then_stmt = self.visit(ctx.statement(0))
        else_stmt = self.visit(ctx.statement(1)) if ctx.ELSE() else None
        return ASTNode("if", [cond, then_stmt] + ([else_stmt] if else_stmt else []))

    def visitExpressionStatement(self, ctx):
        expr = self.visit(ctx.expression()) if ctx.expression() else None
        return ASTNode("expr_stmt", [expr] if expr else [])

    def visitAssignment(self, ctx):
        if ctx.getChildCount() == 3:
            left = self.visit(ctx.logicOr())
            right = self.visit(ctx.assignment())
            return ASTNode("assign", [left, right])
        else:
            return self.visit(ctx.logicOr())

    def visitAdditive(self, ctx):
        if len(ctx.children) == 3:
            left = self.visit(ctx.getChild(0))
            op = ctx.getChild(1).getText()
            right = self.visit(ctx.getChild(2))
            return ASTNode("binop", [left, right], op)
        else:
            return self.visit(ctx.getChild(0))


