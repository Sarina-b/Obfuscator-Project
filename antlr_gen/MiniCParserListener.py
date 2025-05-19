# Generated from MiniCParser.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .MiniCParserParser import MiniCParserParser
else:
    from MiniCParserParser import MiniCParserParser

# This class defines a complete listener for a parse tree produced by MiniCParserParser.
class MiniCParserListener(ParseTreeListener):

    # Enter a parse tree produced by MiniCParserParser#program.
    def enterProgram(self, ctx:MiniCParserParser.ProgramContext):
        pass

    # Exit a parse tree produced by MiniCParserParser#program.
    def exitProgram(self, ctx:MiniCParserParser.ProgramContext):
        pass


    # Enter a parse tree produced by MiniCParserParser#structDecl.
    def enterStructDecl(self, ctx:MiniCParserParser.StructDeclContext):
        pass

    # Exit a parse tree produced by MiniCParserParser#structDecl.
    def exitStructDecl(self, ctx:MiniCParserParser.StructDeclContext):
        pass


    # Enter a parse tree produced by MiniCParserParser#structMember.
    def enterStructMember(self, ctx:MiniCParserParser.StructMemberContext):
        pass

    # Exit a parse tree produced by MiniCParserParser#structMember.
    def exitStructMember(self, ctx:MiniCParserParser.StructMemberContext):
        pass


    # Enter a parse tree produced by MiniCParserParser#declaration.
    def enterDeclaration(self, ctx:MiniCParserParser.DeclarationContext):
        pass

    # Exit a parse tree produced by MiniCParserParser#declaration.
    def exitDeclaration(self, ctx:MiniCParserParser.DeclarationContext):
        pass


    # Enter a parse tree produced by MiniCParserParser#functionDef.
    def enterFunctionDef(self, ctx:MiniCParserParser.FunctionDefContext):
        pass

    # Exit a parse tree produced by MiniCParserParser#functionDef.
    def exitFunctionDef(self, ctx:MiniCParserParser.FunctionDefContext):
        pass


    # Enter a parse tree produced by MiniCParserParser#parameters.
    def enterParameters(self, ctx:MiniCParserParser.ParametersContext):
        pass

    # Exit a parse tree produced by MiniCParserParser#parameters.
    def exitParameters(self, ctx:MiniCParserParser.ParametersContext):
        pass


    # Enter a parse tree produced by MiniCParserParser#parameter.
    def enterParameter(self, ctx:MiniCParserParser.ParameterContext):
        pass

    # Exit a parse tree produced by MiniCParserParser#parameter.
    def exitParameter(self, ctx:MiniCParserParser.ParameterContext):
        pass


    # Enter a parse tree produced by MiniCParserParser#block.
    def enterBlock(self, ctx:MiniCParserParser.BlockContext):
        pass

    # Exit a parse tree produced by MiniCParserParser#block.
    def exitBlock(self, ctx:MiniCParserParser.BlockContext):
        pass


    # Enter a parse tree produced by MiniCParserParser#statement.
    def enterStatement(self, ctx:MiniCParserParser.StatementContext):
        pass

    # Exit a parse tree produced by MiniCParserParser#statement.
    def exitStatement(self, ctx:MiniCParserParser.StatementContext):
        pass


    # Enter a parse tree produced by MiniCParserParser#expressionStatement.
    def enterExpressionStatement(self, ctx:MiniCParserParser.ExpressionStatementContext):
        pass

    # Exit a parse tree produced by MiniCParserParser#expressionStatement.
    def exitExpressionStatement(self, ctx:MiniCParserParser.ExpressionStatementContext):
        pass


    # Enter a parse tree produced by MiniCParserParser#ifStatement.
    def enterIfStatement(self, ctx:MiniCParserParser.IfStatementContext):
        pass

    # Exit a parse tree produced by MiniCParserParser#ifStatement.
    def exitIfStatement(self, ctx:MiniCParserParser.IfStatementContext):
        pass


    # Enter a parse tree produced by MiniCParserParser#whileStatement.
    def enterWhileStatement(self, ctx:MiniCParserParser.WhileStatementContext):
        pass

    # Exit a parse tree produced by MiniCParserParser#whileStatement.
    def exitWhileStatement(self, ctx:MiniCParserParser.WhileStatementContext):
        pass


    # Enter a parse tree produced by MiniCParserParser#forStatement.
    def enterForStatement(self, ctx:MiniCParserParser.ForStatementContext):
        pass

    # Exit a parse tree produced by MiniCParserParser#forStatement.
    def exitForStatement(self, ctx:MiniCParserParser.ForStatementContext):
        pass


    # Enter a parse tree produced by MiniCParserParser#returnStatement.
    def enterReturnStatement(self, ctx:MiniCParserParser.ReturnStatementContext):
        pass

    # Exit a parse tree produced by MiniCParserParser#returnStatement.
    def exitReturnStatement(self, ctx:MiniCParserParser.ReturnStatementContext):
        pass


    # Enter a parse tree produced by MiniCParserParser#ioStatement.
    def enterIoStatement(self, ctx:MiniCParserParser.IoStatementContext):
        pass

    # Exit a parse tree produced by MiniCParserParser#ioStatement.
    def exitIoStatement(self, ctx:MiniCParserParser.IoStatementContext):
        pass


    # Enter a parse tree produced by MiniCParserParser#expression.
    def enterExpression(self, ctx:MiniCParserParser.ExpressionContext):
        pass

    # Exit a parse tree produced by MiniCParserParser#expression.
    def exitExpression(self, ctx:MiniCParserParser.ExpressionContext):
        pass


    # Enter a parse tree produced by MiniCParserParser#assignment.
    def enterAssignment(self, ctx:MiniCParserParser.AssignmentContext):
        pass

    # Exit a parse tree produced by MiniCParserParser#assignment.
    def exitAssignment(self, ctx:MiniCParserParser.AssignmentContext):
        pass


    # Enter a parse tree produced by MiniCParserParser#logicOr.
    def enterLogicOr(self, ctx:MiniCParserParser.LogicOrContext):
        pass

    # Exit a parse tree produced by MiniCParserParser#logicOr.
    def exitLogicOr(self, ctx:MiniCParserParser.LogicOrContext):
        pass


    # Enter a parse tree produced by MiniCParserParser#logicAnd.
    def enterLogicAnd(self, ctx:MiniCParserParser.LogicAndContext):
        pass

    # Exit a parse tree produced by MiniCParserParser#logicAnd.
    def exitLogicAnd(self, ctx:MiniCParserParser.LogicAndContext):
        pass


    # Enter a parse tree produced by MiniCParserParser#equality.
    def enterEquality(self, ctx:MiniCParserParser.EqualityContext):
        pass

    # Exit a parse tree produced by MiniCParserParser#equality.
    def exitEquality(self, ctx:MiniCParserParser.EqualityContext):
        pass


    # Enter a parse tree produced by MiniCParserParser#relational.
    def enterRelational(self, ctx:MiniCParserParser.RelationalContext):
        pass

    # Exit a parse tree produced by MiniCParserParser#relational.
    def exitRelational(self, ctx:MiniCParserParser.RelationalContext):
        pass


    # Enter a parse tree produced by MiniCParserParser#additive.
    def enterAdditive(self, ctx:MiniCParserParser.AdditiveContext):
        pass

    # Exit a parse tree produced by MiniCParserParser#additive.
    def exitAdditive(self, ctx:MiniCParserParser.AdditiveContext):
        pass


    # Enter a parse tree produced by MiniCParserParser#multiplicative.
    def enterMultiplicative(self, ctx:MiniCParserParser.MultiplicativeContext):
        pass

    # Exit a parse tree produced by MiniCParserParser#multiplicative.
    def exitMultiplicative(self, ctx:MiniCParserParser.MultiplicativeContext):
        pass


    # Enter a parse tree produced by MiniCParserParser#unary.
    def enterUnary(self, ctx:MiniCParserParser.UnaryContext):
        pass

    # Exit a parse tree produced by MiniCParserParser#unary.
    def exitUnary(self, ctx:MiniCParserParser.UnaryContext):
        pass


    # Enter a parse tree produced by MiniCParserParser#postfix.
    def enterPostfix(self, ctx:MiniCParserParser.PostfixContext):
        pass

    # Exit a parse tree produced by MiniCParserParser#postfix.
    def exitPostfix(self, ctx:MiniCParserParser.PostfixContext):
        pass


    # Enter a parse tree produced by MiniCParserParser#primary.
    def enterPrimary(self, ctx:MiniCParserParser.PrimaryContext):
        pass

    # Exit a parse tree produced by MiniCParserParser#primary.
    def exitPrimary(self, ctx:MiniCParserParser.PrimaryContext):
        pass


    # Enter a parse tree produced by MiniCParserParser#type.
    def enterType(self, ctx:MiniCParserParser.TypeContext):
        pass

    # Exit a parse tree produced by MiniCParserParser#type.
    def exitType(self, ctx:MiniCParserParser.TypeContext):
        pass


    # Enter a parse tree produced by MiniCParserParser#pointer.
    def enterPointer(self, ctx:MiniCParserParser.PointerContext):
        pass

    # Exit a parse tree produced by MiniCParserParser#pointer.
    def exitPointer(self, ctx:MiniCParserParser.PointerContext):
        pass


    # Enter a parse tree produced by MiniCParserParser#structType.
    def enterStructType(self, ctx:MiniCParserParser.StructTypeContext):
        pass

    # Exit a parse tree produced by MiniCParserParser#structType.
    def exitStructType(self, ctx:MiniCParserParser.StructTypeContext):
        pass


    # Enter a parse tree produced by MiniCParserParser#declarator.
    def enterDeclarator(self, ctx:MiniCParserParser.DeclaratorContext):
        pass

    # Exit a parse tree produced by MiniCParserParser#declarator.
    def exitDeclarator(self, ctx:MiniCParserParser.DeclaratorContext):
        pass



del MiniCParserParser