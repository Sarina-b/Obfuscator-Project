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


