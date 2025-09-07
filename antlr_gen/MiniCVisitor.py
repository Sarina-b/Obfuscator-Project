# Generated from MiniC.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MiniCParser import MiniCParser
else:
    from MiniCParser import MiniCParser

# This class defines a complete generic visitor for a parse tree produced by MiniCParser.

class MiniCVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MiniCParser#program.
    def visitProgram(self, ctx:MiniCParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#functionDecl.
    def visitFunctionDecl(self, ctx:MiniCParser.FunctionDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#structDecl.
    def visitStructDecl(self, ctx:MiniCParser.StructDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#varDecl.
    def visitVarDecl(self, ctx:MiniCParser.VarDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#varDeclList.
    def visitVarDeclList(self, ctx:MiniCParser.VarDeclListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#varDeclItem.
    def visitVarDeclItem(self, ctx:MiniCParser.VarDeclItemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#typ.
    def visitTyp(self, ctx:MiniCParser.TypContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#baseType.
    def visitBaseType(self, ctx:MiniCParser.BaseTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#pointerType.
    def visitPointerType(self, ctx:MiniCParser.PointerTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#paramList.
    def visitParamList(self, ctx:MiniCParser.ParamListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#param.
    def visitParam(self, ctx:MiniCParser.ParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#block.
    def visitBlock(self, ctx:MiniCParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#statement.
    def visitStatement(self, ctx:MiniCParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#assignStat.
    def visitAssignStat(self, ctx:MiniCParser.AssignStatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#lvalue.
    def visitLvalue(self, ctx:MiniCParser.LvalueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#pointerDereference.
    def visitPointerDereference(self, ctx:MiniCParser.PointerDereferenceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#ifStat.
    def visitIfStat(self, ctx:MiniCParser.IfStatContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by MiniCParser#whileStat.
    def visitWhileStat(self, ctx:MiniCParser.WhileStatContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by MiniCParser#forStat.
    def visitForStat(self, ctx:MiniCParser.ForStatContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by MiniCParser#returnStat.
    def visitReturnStat(self, ctx:MiniCParser.ReturnStatContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by MiniCParser#funcCall.
    def visitFuncCall(self, ctx:MiniCParser.FuncCallContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by MiniCParser#argumentList.
    def visitArgumentList(self, ctx:MiniCParser.ArgumentListContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by MiniCParser#ioStat.
    def visitIoStat(self, ctx:MiniCParser.IoStatContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by MiniCParser#expressionList.
    def visitExpressionList(self, ctx:MiniCParser.ExpressionListContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by MiniCParser#expression.
    def visitExpression(self, ctx:MiniCParser.ExpressionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by MiniCParser#unaryOp.
    def visitUnaryOp(self, ctx:MiniCParser.UnaryOpContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by MiniCParser#literal.
    def visitLiteral(self, ctx:MiniCParser.LiteralContext):
        return self.visitChildren(ctx)



del MiniCParser