# Generated from /grammars/MiniC.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .MiniCParser import MiniCParser
else:
    from MiniCParser import MiniCParser

# This class defines a complete listener for a parse tree produced by MiniCParser.
class MiniCListener(ParseTreeListener):

    # Enter a parse tree produced by MiniCParser#program.
    def enterProgram(self, ctx:MiniCParser.ProgramContext):
        pass

    # Exit a parse tree produced by MiniCParser#program.
    def exitProgram(self, ctx:MiniCParser.ProgramContext):
        pass


    # Enter a parse tree produced by MiniCParser#functionDecl.
    def enterFunctionDecl(self, ctx:MiniCParser.FunctionDeclContext):
        pass

    # Exit a parse tree produced by MiniCParser#functionDecl.
    def exitFunctionDecl(self, ctx:MiniCParser.FunctionDeclContext):
        pass


    # Enter a parse tree produced by MiniCParser#structDecl.
    def enterStructDecl(self, ctx:MiniCParser.StructDeclContext):
        pass

    # Exit a parse tree produced by MiniCParser#structDecl.
    def exitStructDecl(self, ctx:MiniCParser.StructDeclContext):
        pass


    # Enter a parse tree produced by MiniCParser#varDecl.
    def enterVarDecl(self, ctx:MiniCParser.VarDeclContext):
        pass

    # Exit a parse tree produced by MiniCParser#varDecl.
    def exitVarDecl(self, ctx:MiniCParser.VarDeclContext):
        pass


    # Enter a parse tree produced by MiniCParser#varDeclList.
    def enterVarDeclList(self, ctx:MiniCParser.VarDeclListContext):
        pass

    # Exit a parse tree produced by MiniCParser#varDeclList.
    def exitVarDeclList(self, ctx:MiniCParser.VarDeclListContext):
        pass


    # Enter a parse tree produced by MiniCParser#varDeclItem.
    def enterVarDeclItem(self, ctx:MiniCParser.VarDeclItemContext):
        pass

    # Exit a parse tree produced by MiniCParser#varDeclItem.
    def exitVarDeclItem(self, ctx:MiniCParser.VarDeclItemContext):
        pass


    # Enter a parse tree produced by MiniCParser#typ.
    def enterTyp(self, ctx:MiniCParser.TypContext):
        pass

    # Exit a parse tree produced by MiniCParser#typ.
    def exitTyp(self, ctx:MiniCParser.TypContext):
        pass


    # Enter a parse tree produced by MiniCParser#baseType.
    def enterBaseType(self, ctx:MiniCParser.BaseTypeContext):
        pass

    # Exit a parse tree produced by MiniCParser#baseType.
    def exitBaseType(self, ctx:MiniCParser.BaseTypeContext):
        pass


    # Enter a parse tree produced by MiniCParser#pointerType.
    def enterPointerType(self, ctx:MiniCParser.PointerTypeContext):
        pass

    # Exit a parse tree produced by MiniCParser#pointerType.
    def exitPointerType(self, ctx:MiniCParser.PointerTypeContext):
        pass


    # Enter a parse tree produced by MiniCParser#paramList.
    def enterParamList(self, ctx:MiniCParser.ParamListContext):
        pass

    # Exit a parse tree produced by MiniCParser#paramList.
    def exitParamList(self, ctx:MiniCParser.ParamListContext):
        pass


    # Enter a parse tree produced by MiniCParser#param.
    def enterParam(self, ctx:MiniCParser.ParamContext):
        pass

    # Exit a parse tree produced by MiniCParser#param.
    def exitParam(self, ctx:MiniCParser.ParamContext):
        pass


    # Enter a parse tree produced by MiniCParser#block.
    def enterBlock(self, ctx:MiniCParser.BlockContext):
        pass

    # Exit a parse tree produced by MiniCParser#block.
    def exitBlock(self, ctx:MiniCParser.BlockContext):
        pass


    # Enter a parse tree produced by MiniCParser#statement.
    def enterStatement(self, ctx:MiniCParser.StatementContext):
        pass

    # Exit a parse tree produced by MiniCParser#statement.
    def exitStatement(self, ctx:MiniCParser.StatementContext):
        pass


    # Enter a parse tree produced by MiniCParser#assignStat.
    def enterAssignStat(self, ctx:MiniCParser.AssignStatContext):
        pass

    # Exit a parse tree produced by MiniCParser#assignStat.
    def exitAssignStat(self, ctx:MiniCParser.AssignStatContext):
        pass


    # Enter a parse tree produced by MiniCParser#lvalue.
    def enterLvalue(self, ctx:MiniCParser.LvalueContext):
        pass

    # Exit a parse tree produced by MiniCParser#lvalue.
    def exitLvalue(self, ctx:MiniCParser.LvalueContext):
        pass


    # Enter a parse tree produced by MiniCParser#pointerDereference.
    def enterPointerDereference(self, ctx:MiniCParser.PointerDereferenceContext):
        pass

    # Exit a parse tree produced by MiniCParser#pointerDereference.
    def exitPointerDereference(self, ctx:MiniCParser.PointerDereferenceContext):
        pass


    # Enter a parse tree produced by MiniCParser#ifStat.
    def enterIfStat(self, ctx:MiniCParser.IfStatContext):
        pass

    # Exit a parse tree produced by MiniCParser#ifStat.
    def exitIfStat(self, ctx:MiniCParser.IfStatContext):
        pass


    # Enter a parse tree produced by MiniCParser#whileStat.
    def enterWhileStat(self, ctx:MiniCParser.WhileStatContext):
        pass

    # Exit a parse tree produced by MiniCParser#whileStat.
    def exitWhileStat(self, ctx:MiniCParser.WhileStatContext):
        pass


    # Enter a parse tree produced by MiniCParser#forStat.
    def enterForStat(self, ctx:MiniCParser.ForStatContext):
        pass

    # Exit a parse tree produced by MiniCParser#forStat.
    def exitForStat(self, ctx:MiniCParser.ForStatContext):
        pass


    # Enter a parse tree produced by MiniCParser#returnStat.
    def enterReturnStat(self, ctx:MiniCParser.ReturnStatContext):
        pass

    # Exit a parse tree produced by MiniCParser#returnStat.
    def exitReturnStat(self, ctx:MiniCParser.ReturnStatContext):
        pass


    # Enter a parse tree produced by MiniCParser#funcCall.
    def enterFuncCall(self, ctx:MiniCParser.FuncCallContext):
        pass

    # Exit a parse tree produced by MiniCParser#funcCall.
    def exitFuncCall(self, ctx:MiniCParser.FuncCallContext):
        pass


    # Enter a parse tree produced by MiniCParser#argumentList.
    def enterArgumentList(self, ctx:MiniCParser.ArgumentListContext):
        pass

    # Exit a parse tree produced by MiniCParser#argumentList.
    def exitArgumentList(self, ctx:MiniCParser.ArgumentListContext):
        pass


    # Enter a parse tree produced by MiniCParser#ioStat.
    def enterIoStat(self, ctx:MiniCParser.IoStatContext):
        pass

    # Exit a parse tree produced by MiniCParser#ioStat.
    def exitIoStat(self, ctx:MiniCParser.IoStatContext):
        pass


    # Enter a parse tree produced by MiniCParser#expressionList.
    def enterExpressionList(self, ctx:MiniCParser.ExpressionListContext):
        pass

    # Exit a parse tree produced by MiniCParser#expressionList.
    def exitExpressionList(self, ctx:MiniCParser.ExpressionListContext):
        pass


    # Enter a parse tree produced by MiniCParser#expression.
    def enterExpression(self, ctx:MiniCParser.ExpressionContext):
        pass

    # Exit a parse tree produced by MiniCParser#expression.
    def exitExpression(self, ctx:MiniCParser.ExpressionContext):
        pass


    # Enter a parse tree produced by MiniCParser#unaryOp.
    def enterUnaryOp(self, ctx:MiniCParser.UnaryOpContext):
        pass

    # Exit a parse tree produced by MiniCParser#unaryOp.
    def exitUnaryOp(self, ctx:MiniCParser.UnaryOpContext):
        pass


    # Enter a parse tree produced by MiniCParser#literal.
    def enterLiteral(self, ctx:MiniCParser.LiteralContext):
        pass

    # Exit a parse tree produced by MiniCParser#literal.
    def exitLiteral(self, ctx:MiniCParser.LiteralContext):
        pass



del MiniCParser