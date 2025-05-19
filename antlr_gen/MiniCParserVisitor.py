# Generated from MiniCParser.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .MiniCParserParser import MiniCParserParser
else:
    from MiniCParserParser import MiniCParserParser

# This class defines a complete generic visitor for a parse tree produced by MiniCParserParser.

class MiniCParserVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MiniCParserParser#program.
    def visitProgram(self, ctx:MiniCParserParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParserParser#structDecl.
    def visitStructDecl(self, ctx:MiniCParserParser.StructDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParserParser#structMember.
    def visitStructMember(self, ctx:MiniCParserParser.StructMemberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParserParser#declaration.
    def visitDeclaration(self, ctx:MiniCParserParser.DeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParserParser#functionDef.
    def visitFunctionDef(self, ctx:MiniCParserParser.FunctionDefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParserParser#parameters.
    def visitParameters(self, ctx:MiniCParserParser.ParametersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParserParser#parameter.
    def visitParameter(self, ctx:MiniCParserParser.ParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParserParser#block.
    def visitBlock(self, ctx:MiniCParserParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParserParser#statement.
    def visitStatement(self, ctx:MiniCParserParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParserParser#expressionStatement.
    def visitExpressionStatement(self, ctx:MiniCParserParser.ExpressionStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParserParser#ifStatement.
    def visitIfStatement(self, ctx:MiniCParserParser.IfStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParserParser#whileStatement.
    def visitWhileStatement(self, ctx:MiniCParserParser.WhileStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParserParser#forStatement.
    def visitForStatement(self, ctx:MiniCParserParser.ForStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParserParser#returnStatement.
    def visitReturnStatement(self, ctx:MiniCParserParser.ReturnStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParserParser#ioStatement.
    def visitIoStatement(self, ctx:MiniCParserParser.IoStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParserParser#expression.
    def visitExpression(self, ctx:MiniCParserParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParserParser#assignment.
    def visitAssignment(self, ctx:MiniCParserParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParserParser#logicOr.
    def visitLogicOr(self, ctx:MiniCParserParser.LogicOrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParserParser#logicAnd.
    def visitLogicAnd(self, ctx:MiniCParserParser.LogicAndContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParserParser#equality.
    def visitEquality(self, ctx:MiniCParserParser.EqualityContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParserParser#relational.
    def visitRelational(self, ctx:MiniCParserParser.RelationalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParserParser#additive.
    def visitAdditive(self, ctx:MiniCParserParser.AdditiveContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParserParser#multiplicative.
    def visitMultiplicative(self, ctx:MiniCParserParser.MultiplicativeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParserParser#unary.
    def visitUnary(self, ctx:MiniCParserParser.UnaryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParserParser#postfix.
    def visitPostfix(self, ctx:MiniCParserParser.PostfixContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParserParser#primary.
    def visitPrimary(self, ctx:MiniCParserParser.PrimaryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParserParser#type.
    def visitType(self, ctx:MiniCParserParser.TypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParserParser#pointer.
    def visitPointer(self, ctx:MiniCParserParser.PointerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParserParser#structType.
    def visitStructType(self, ctx:MiniCParserParser.StructTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParserParser#declarator.
    def visitDeclarator(self, ctx:MiniCParserParser.DeclaratorContext):
        return self.visitChildren(ctx)



del MiniCParserParser