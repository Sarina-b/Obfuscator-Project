# Generated from MiniCParser.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,39,292,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,1,0,1,0,1,0,5,0,64,8,0,10,0,12,0,67,
        9,0,1,0,1,0,1,1,1,1,1,1,1,1,5,1,75,8,1,10,1,12,1,78,9,1,1,1,1,1,
        1,1,1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,3,3,3,91,8,3,1,3,1,3,1,4,1,4,1,
        4,1,4,3,4,99,8,4,1,4,1,4,1,4,1,5,1,5,1,5,5,5,107,8,5,10,5,12,5,110,
        9,5,1,6,1,6,1,6,1,7,1,7,5,7,117,8,7,10,7,12,7,120,9,7,1,7,1,7,1,
        8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,3,8,132,8,8,1,9,3,9,135,8,9,1,9,1,
        9,1,10,1,10,1,10,1,10,1,10,1,10,1,10,3,10,146,8,10,1,11,1,11,1,11,
        1,11,1,11,1,11,1,12,1,12,1,12,3,12,157,8,12,1,12,1,12,3,12,161,8,
        12,1,12,1,12,3,12,165,8,12,1,12,1,12,1,12,1,13,1,13,3,13,172,8,13,
        1,13,1,13,1,14,1,14,1,14,1,14,1,14,5,14,181,8,14,10,14,12,14,184,
        9,14,1,14,1,14,1,14,1,15,1,15,1,16,1,16,1,16,3,16,194,8,16,1,17,
        1,17,1,17,5,17,199,8,17,10,17,12,17,202,9,17,1,18,1,18,1,18,5,18,
        207,8,18,10,18,12,18,210,9,18,1,19,1,19,1,19,5,19,215,8,19,10,19,
        12,19,218,9,19,1,20,1,20,1,20,5,20,223,8,20,10,20,12,20,226,9,20,
        1,21,1,21,1,21,5,21,231,8,21,10,21,12,21,234,9,21,1,22,1,22,1,22,
        5,22,239,8,22,10,22,12,22,242,9,22,1,23,3,23,245,8,23,1,23,1,23,
        1,24,1,24,1,24,5,24,252,8,24,10,24,12,24,255,9,24,1,25,1,25,1,25,
        1,25,1,25,1,25,1,25,1,25,3,25,265,8,25,1,26,1,26,1,26,1,26,3,26,
        271,8,26,1,26,5,26,274,8,26,10,26,12,26,277,9,26,1,27,1,27,1,28,
        1,28,1,28,1,29,5,29,285,8,29,10,29,12,29,288,9,29,1,29,1,29,1,29,
        0,0,30,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,
        42,44,46,48,50,52,54,56,58,0,6,1,0,14,15,1,0,18,19,1,0,20,23,1,0,
        24,25,1,0,26,27,2,0,25,26,28,29,301,0,65,1,0,0,0,2,70,1,0,0,0,4,
        82,1,0,0,0,6,86,1,0,0,0,8,94,1,0,0,0,10,103,1,0,0,0,12,111,1,0,0,
        0,14,114,1,0,0,0,16,131,1,0,0,0,18,134,1,0,0,0,20,138,1,0,0,0,22,
        147,1,0,0,0,24,153,1,0,0,0,26,169,1,0,0,0,28,175,1,0,0,0,30,188,
        1,0,0,0,32,190,1,0,0,0,34,195,1,0,0,0,36,203,1,0,0,0,38,211,1,0,
        0,0,40,219,1,0,0,0,42,227,1,0,0,0,44,235,1,0,0,0,46,244,1,0,0,0,
        48,248,1,0,0,0,50,264,1,0,0,0,52,270,1,0,0,0,54,278,1,0,0,0,56,280,
        1,0,0,0,58,286,1,0,0,0,60,64,3,2,1,0,61,64,3,6,3,0,62,64,3,8,4,0,
        63,60,1,0,0,0,63,61,1,0,0,0,63,62,1,0,0,0,64,67,1,0,0,0,65,63,1,
        0,0,0,65,66,1,0,0,0,66,68,1,0,0,0,67,65,1,0,0,0,68,69,5,0,0,1,69,
        1,1,0,0,0,70,71,5,1,0,0,71,72,5,1,0,0,72,76,5,2,0,0,73,75,3,4,2,
        0,74,73,1,0,0,0,75,78,1,0,0,0,76,74,1,0,0,0,76,77,1,0,0,0,77,79,
        1,0,0,0,78,76,1,0,0,0,79,80,5,3,0,0,80,81,5,4,0,0,81,3,1,0,0,0,82,
        83,3,52,26,0,83,84,3,58,29,0,84,85,5,4,0,0,85,5,1,0,0,0,86,87,3,
        52,26,0,87,90,3,58,29,0,88,89,5,5,0,0,89,91,3,30,15,0,90,88,1,0,
        0,0,90,91,1,0,0,0,91,92,1,0,0,0,92,93,5,4,0,0,93,7,1,0,0,0,94,95,
        3,52,26,0,95,96,5,1,0,0,96,98,5,6,0,0,97,99,3,10,5,0,98,97,1,0,0,
        0,98,99,1,0,0,0,99,100,1,0,0,0,100,101,5,7,0,0,101,102,3,14,7,0,
        102,9,1,0,0,0,103,108,3,12,6,0,104,105,5,8,0,0,105,107,3,12,6,0,
        106,104,1,0,0,0,107,110,1,0,0,0,108,106,1,0,0,0,108,109,1,0,0,0,
        109,11,1,0,0,0,110,108,1,0,0,0,111,112,3,52,26,0,112,113,3,58,29,
        0,113,13,1,0,0,0,114,118,5,2,0,0,115,117,3,16,8,0,116,115,1,0,0,
        0,117,120,1,0,0,0,118,116,1,0,0,0,118,119,1,0,0,0,119,121,1,0,0,
        0,120,118,1,0,0,0,121,122,5,3,0,0,122,15,1,0,0,0,123,132,3,14,7,
        0,124,132,3,6,3,0,125,132,3,18,9,0,126,132,3,20,10,0,127,132,3,22,
        11,0,128,132,3,24,12,0,129,132,3,26,13,0,130,132,3,28,14,0,131,123,
        1,0,0,0,131,124,1,0,0,0,131,125,1,0,0,0,131,126,1,0,0,0,131,127,
        1,0,0,0,131,128,1,0,0,0,131,129,1,0,0,0,131,130,1,0,0,0,132,17,1,
        0,0,0,133,135,3,30,15,0,134,133,1,0,0,0,134,135,1,0,0,0,135,136,
        1,0,0,0,136,137,5,4,0,0,137,19,1,0,0,0,138,139,5,9,0,0,139,140,5,
        6,0,0,140,141,3,30,15,0,141,142,5,7,0,0,142,145,3,16,8,0,143,144,
        5,10,0,0,144,146,3,16,8,0,145,143,1,0,0,0,145,146,1,0,0,0,146,21,
        1,0,0,0,147,148,5,11,0,0,148,149,5,6,0,0,149,150,3,30,15,0,150,151,
        5,7,0,0,151,152,3,16,8,0,152,23,1,0,0,0,153,154,5,12,0,0,154,156,
        5,6,0,0,155,157,3,30,15,0,156,155,1,0,0,0,156,157,1,0,0,0,157,158,
        1,0,0,0,158,160,5,4,0,0,159,161,3,30,15,0,160,159,1,0,0,0,160,161,
        1,0,0,0,161,162,1,0,0,0,162,164,5,4,0,0,163,165,3,30,15,0,164,163,
        1,0,0,0,164,165,1,0,0,0,165,166,1,0,0,0,166,167,5,7,0,0,167,168,
        3,16,8,0,168,25,1,0,0,0,169,171,5,13,0,0,170,172,3,30,15,0,171,170,
        1,0,0,0,171,172,1,0,0,0,172,173,1,0,0,0,173,174,5,4,0,0,174,27,1,
        0,0,0,175,176,7,0,0,0,176,177,5,6,0,0,177,182,5,5,0,0,178,179,5,
        8,0,0,179,181,3,30,15,0,180,178,1,0,0,0,181,184,1,0,0,0,182,180,
        1,0,0,0,182,183,1,0,0,0,183,185,1,0,0,0,184,182,1,0,0,0,185,186,
        5,7,0,0,186,187,5,4,0,0,187,29,1,0,0,0,188,189,3,32,16,0,189,31,
        1,0,0,0,190,193,3,34,17,0,191,192,5,5,0,0,192,194,3,32,16,0,193,
        191,1,0,0,0,193,194,1,0,0,0,194,33,1,0,0,0,195,200,3,36,18,0,196,
        197,5,16,0,0,197,199,3,36,18,0,198,196,1,0,0,0,199,202,1,0,0,0,200,
        198,1,0,0,0,200,201,1,0,0,0,201,35,1,0,0,0,202,200,1,0,0,0,203,208,
        3,38,19,0,204,205,5,17,0,0,205,207,3,38,19,0,206,204,1,0,0,0,207,
        210,1,0,0,0,208,206,1,0,0,0,208,209,1,0,0,0,209,37,1,0,0,0,210,208,
        1,0,0,0,211,216,3,40,20,0,212,213,7,1,0,0,213,215,3,40,20,0,214,
        212,1,0,0,0,215,218,1,0,0,0,216,214,1,0,0,0,216,217,1,0,0,0,217,
        39,1,0,0,0,218,216,1,0,0,0,219,224,3,42,21,0,220,221,7,2,0,0,221,
        223,3,42,21,0,222,220,1,0,0,0,223,226,1,0,0,0,224,222,1,0,0,0,224,
        225,1,0,0,0,225,41,1,0,0,0,226,224,1,0,0,0,227,232,3,44,22,0,228,
        229,7,3,0,0,229,231,3,44,22,0,230,228,1,0,0,0,231,234,1,0,0,0,232,
        230,1,0,0,0,232,233,1,0,0,0,233,43,1,0,0,0,234,232,1,0,0,0,235,240,
        3,46,23,0,236,237,7,4,0,0,237,239,3,46,23,0,238,236,1,0,0,0,239,
        242,1,0,0,0,240,238,1,0,0,0,240,241,1,0,0,0,241,45,1,0,0,0,242,240,
        1,0,0,0,243,245,7,5,0,0,244,243,1,0,0,0,244,245,1,0,0,0,245,246,
        1,0,0,0,246,247,3,48,24,0,247,47,1,0,0,0,248,253,3,50,25,0,249,250,
        5,30,0,0,250,252,5,1,0,0,251,249,1,0,0,0,252,255,1,0,0,0,253,251,
        1,0,0,0,253,254,1,0,0,0,254,49,1,0,0,0,255,253,1,0,0,0,256,265,5,
        2,0,0,257,265,5,3,0,0,258,265,5,4,0,0,259,265,5,1,0,0,260,261,5,
        6,0,0,261,262,3,30,15,0,262,263,5,7,0,0,263,265,1,0,0,0,264,256,
        1,0,0,0,264,257,1,0,0,0,264,258,1,0,0,0,264,259,1,0,0,0,264,260,
        1,0,0,0,265,51,1,0,0,0,266,271,5,31,0,0,267,271,5,32,0,0,268,271,
        5,33,0,0,269,271,3,56,28,0,270,266,1,0,0,0,270,267,1,0,0,0,270,268,
        1,0,0,0,270,269,1,0,0,0,271,275,1,0,0,0,272,274,3,54,27,0,273,272,
        1,0,0,0,274,277,1,0,0,0,275,273,1,0,0,0,275,276,1,0,0,0,276,53,1,
        0,0,0,277,275,1,0,0,0,278,279,5,26,0,0,279,55,1,0,0,0,280,281,5,
        1,0,0,281,282,5,1,0,0,282,57,1,0,0,0,283,285,3,54,27,0,284,283,1,
        0,0,0,285,288,1,0,0,0,286,284,1,0,0,0,286,287,1,0,0,0,287,289,1,
        0,0,0,288,286,1,0,0,0,289,290,5,1,0,0,290,59,1,0,0,0,28,63,65,76,
        90,98,108,118,131,134,145,156,160,164,171,182,193,200,208,216,224,
        232,240,244,253,264,270,275,286
    ]

class MiniCParserParser ( Parser ):

    grammarFileName = "MiniCParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'struct'", "'{'", "'}'", "';'", "'='", 
                     "'('", "')'", "','", "'if'", "'else'", "'while'", "'for'", 
                     "'return'", "'printf'", "'scanf'", "'||'", "'&&'", 
                     "'=='", "'!='", "'<'", "'>'", "'<='", "'>='", "'+'", 
                     "'-'", "'*'", "'/'", "'!'", "'&'", "'.'", "'int'", 
                     "'char'", "'bool'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "LBRACE", "RBRACE", "SEMI", 
                      "COMMA", "WS", "COMMENT" ]

    RULE_program = 0
    RULE_structDecl = 1
    RULE_structMember = 2
    RULE_declaration = 3
    RULE_functionDef = 4
    RULE_parameters = 5
    RULE_parameter = 6
    RULE_block = 7
    RULE_statement = 8
    RULE_expressionStatement = 9
    RULE_ifStatement = 10
    RULE_whileStatement = 11
    RULE_forStatement = 12
    RULE_returnStatement = 13
    RULE_ioStatement = 14
    RULE_expression = 15
    RULE_assignment = 16
    RULE_logicOr = 17
    RULE_logicAnd = 18
    RULE_equality = 19
    RULE_relational = 20
    RULE_additive = 21
    RULE_multiplicative = 22
    RULE_unary = 23
    RULE_postfix = 24
    RULE_primary = 25
    RULE_type = 26
    RULE_pointer = 27
    RULE_structType = 28
    RULE_declarator = 29

    ruleNames =  [ "program", "structDecl", "structMember", "declaration", 
                   "functionDef", "parameters", "parameter", "block", "statement", 
                   "expressionStatement", "ifStatement", "whileStatement", 
                   "forStatement", "returnStatement", "ioStatement", "expression", 
                   "assignment", "logicOr", "logicAnd", "equality", "relational", 
                   "additive", "multiplicative", "unary", "postfix", "primary", 
                   "type", "pointer", "structType", "declarator" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    T__19=20
    T__20=21
    T__21=22
    T__22=23
    T__23=24
    T__24=25
    T__25=26
    T__26=27
    T__27=28
    T__28=29
    T__29=30
    T__30=31
    T__31=32
    T__32=33
    ID=1
    INT_LITERAL=2
    CHAR_LITERAL=3
    BOOL_LITERAL=4
    STRING_LITERAL=5
    STRUCT=6
    IF=7
    ELSE=8
    WHILE=9
    FOR=10
    RETURN=11
    PRINTF=12
    SCANF=13
    INT=14
    CHAR=15
    BOOL=16
    PLUS=17
    MINUS=18
    STAR=19
    DIV=20
    ASSIGN=21
    EQUAL=22
    NOTEQUAL=23
    LT=24
    GT=25
    LE=26
    GE=27
    AND=28
    OR=29
    NOT=30
    DOT=31
    LPAREN=32
    RPAREN=33
    LBRACE=34
    RBRACE=35
    SEMI=36
    COMMA=37
    WS=38
    COMMENT=39

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(MiniCParserParser.EOF, 0)

        def structDecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniCParserParser.StructDeclContext)
            else:
                return self.getTypedRuleContext(MiniCParserParser.StructDeclContext,i)


        def declaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniCParserParser.DeclarationContext)
            else:
                return self.getTypedRuleContext(MiniCParserParser.DeclarationContext,i)


        def functionDef(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniCParserParser.FunctionDefContext)
            else:
                return self.getTypedRuleContext(MiniCParserParser.FunctionDefContext,i)


        def getRuleIndex(self):
            return MiniCParserParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = MiniCParserParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 65
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 15032385538) != 0):
                self.state = 63
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
                if la_ == 1:
                    self.state = 60
                    self.structDecl()
                    pass

                elif la_ == 2:
                    self.state = 61
                    self.declaration()
                    pass

                elif la_ == 3:
                    self.state = 62
                    self.functionDef()
                    pass


                self.state = 67
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 68
            self.match(MiniCParserParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StructDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniCParserParser.ID, 0)

        def structMember(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniCParserParser.StructMemberContext)
            else:
                return self.getTypedRuleContext(MiniCParserParser.StructMemberContext,i)


        def getRuleIndex(self):
            return MiniCParserParser.RULE_structDecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStructDecl" ):
                listener.enterStructDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStructDecl" ):
                listener.exitStructDecl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStructDecl" ):
                return visitor.visitStructDecl(self)
            else:
                return visitor.visitChildren(self)




    def structDecl(self):

        localctx = MiniCParserParser.StructDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_structDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 70
            self.match(MiniCParserParser.T__0)
            self.state = 71
            self.match(MiniCParserParser.T__0)
            self.state = 72
            self.match(MiniCParserParser.T__1)
            self.state = 76
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 15032385538) != 0):
                self.state = 73
                self.structMember()
                self.state = 78
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 79
            self.match(MiniCParserParser.T__2)
            self.state = 80
            self.match(MiniCParserParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StructMemberContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_(self):
            return self.getTypedRuleContext(MiniCParserParser.TypeContext,0)


        def declarator(self):
            return self.getTypedRuleContext(MiniCParserParser.DeclaratorContext,0)


        def getRuleIndex(self):
            return MiniCParserParser.RULE_structMember

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStructMember" ):
                listener.enterStructMember(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStructMember" ):
                listener.exitStructMember(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStructMember" ):
                return visitor.visitStructMember(self)
            else:
                return visitor.visitChildren(self)




    def structMember(self):

        localctx = MiniCParserParser.StructMemberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_structMember)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 82
            self.type_()
            self.state = 83
            self.declarator()
            self.state = 84
            self.match(MiniCParserParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_(self):
            return self.getTypedRuleContext(MiniCParserParser.TypeContext,0)


        def declarator(self):
            return self.getTypedRuleContext(MiniCParserParser.DeclaratorContext,0)


        def expression(self):
            return self.getTypedRuleContext(MiniCParserParser.ExpressionContext,0)


        def getRuleIndex(self):
            return MiniCParserParser.RULE_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaration" ):
                listener.enterDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaration" ):
                listener.exitDeclaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaration" ):
                return visitor.visitDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def declaration(self):

        localctx = MiniCParserParser.DeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 86
            self.type_()
            self.state = 87
            self.declarator()
            self.state = 90
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==5:
                self.state = 88
                self.match(MiniCParserParser.T__4)
                self.state = 89
                self.expression()


            self.state = 92
            self.match(MiniCParserParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionDefContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_(self):
            return self.getTypedRuleContext(MiniCParserParser.TypeContext,0)


        def ID(self):
            return self.getToken(MiniCParserParser.ID, 0)

        def block(self):
            return self.getTypedRuleContext(MiniCParserParser.BlockContext,0)


        def parameters(self):
            return self.getTypedRuleContext(MiniCParserParser.ParametersContext,0)


        def getRuleIndex(self):
            return MiniCParserParser.RULE_functionDef

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionDef" ):
                listener.enterFunctionDef(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionDef" ):
                listener.exitFunctionDef(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionDef" ):
                return visitor.visitFunctionDef(self)
            else:
                return visitor.visitChildren(self)




    def functionDef(self):

        localctx = MiniCParserParser.FunctionDefContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_functionDef)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 94
            self.type_()
            self.state = 95
            self.match(MiniCParserParser.T__0)
            self.state = 96
            self.match(MiniCParserParser.T__5)
            self.state = 98
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 15032385538) != 0):
                self.state = 97
                self.parameters()


            self.state = 100
            self.match(MiniCParserParser.T__6)
            self.state = 101
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParametersContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def parameter(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniCParserParser.ParameterContext)
            else:
                return self.getTypedRuleContext(MiniCParserParser.ParameterContext,i)


        def getRuleIndex(self):
            return MiniCParserParser.RULE_parameters

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParameters" ):
                listener.enterParameters(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParameters" ):
                listener.exitParameters(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParameters" ):
                return visitor.visitParameters(self)
            else:
                return visitor.visitChildren(self)




    def parameters(self):

        localctx = MiniCParserParser.ParametersContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_parameters)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 103
            self.parameter()
            self.state = 108
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==8:
                self.state = 104
                self.match(MiniCParserParser.T__7)
                self.state = 105
                self.parameter()
                self.state = 110
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParameterContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_(self):
            return self.getTypedRuleContext(MiniCParserParser.TypeContext,0)


        def declarator(self):
            return self.getTypedRuleContext(MiniCParserParser.DeclaratorContext,0)


        def getRuleIndex(self):
            return MiniCParserParser.RULE_parameter

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParameter" ):
                listener.enterParameter(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParameter" ):
                listener.exitParameter(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParameter" ):
                return visitor.visitParameter(self)
            else:
                return visitor.visitChildren(self)




    def parameter(self):

        localctx = MiniCParserParser.ParameterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_parameter)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 111
            self.type_()
            self.state = 112
            self.declarator()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniCParserParser.StatementContext)
            else:
                return self.getTypedRuleContext(MiniCParserParser.StatementContext,i)


        def getRuleIndex(self):
            return MiniCParserParser.RULE_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock" ):
                listener.enterBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock" ):
                listener.exitBlock(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock" ):
                return visitor.visitBlock(self)
            else:
                return visitor.visitChildren(self)




    def block(self):

        localctx = MiniCParserParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_block)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 114
            self.match(MiniCParserParser.T__1)
            self.state = 118
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,6,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 115
                    self.statement() 
                self.state = 120
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

            self.state = 121
            self.match(MiniCParserParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def block(self):
            return self.getTypedRuleContext(MiniCParserParser.BlockContext,0)


        def declaration(self):
            return self.getTypedRuleContext(MiniCParserParser.DeclarationContext,0)


        def expressionStatement(self):
            return self.getTypedRuleContext(MiniCParserParser.ExpressionStatementContext,0)


        def ifStatement(self):
            return self.getTypedRuleContext(MiniCParserParser.IfStatementContext,0)


        def whileStatement(self):
            return self.getTypedRuleContext(MiniCParserParser.WhileStatementContext,0)


        def forStatement(self):
            return self.getTypedRuleContext(MiniCParserParser.ForStatementContext,0)


        def returnStatement(self):
            return self.getTypedRuleContext(MiniCParserParser.ReturnStatementContext,0)


        def ioStatement(self):
            return self.getTypedRuleContext(MiniCParserParser.IoStatementContext,0)


        def getRuleIndex(self):
            return MiniCParserParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = MiniCParserParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_statement)
        try:
            self.state = 131
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 123
                self.block()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 124
                self.declaration()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 125
                self.expressionStatement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 126
                self.ifStatement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 127
                self.whileStatement()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 128
                self.forStatement()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 129
                self.returnStatement()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 130
                self.ioStatement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(MiniCParserParser.ExpressionContext,0)


        def getRuleIndex(self):
            return MiniCParserParser.RULE_expressionStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpressionStatement" ):
                listener.enterExpressionStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpressionStatement" ):
                listener.exitExpressionStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpressionStatement" ):
                return visitor.visitExpressionStatement(self)
            else:
                return visitor.visitChildren(self)




    def expressionStatement(self):

        localctx = MiniCParserParser.ExpressionStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_expressionStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 134
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.state = 133
                self.expression()


            self.state = 136
            self.match(MiniCParserParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(MiniCParserParser.ExpressionContext,0)


        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniCParserParser.StatementContext)
            else:
                return self.getTypedRuleContext(MiniCParserParser.StatementContext,i)


        def getRuleIndex(self):
            return MiniCParserParser.RULE_ifStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfStatement" ):
                listener.enterIfStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfStatement" ):
                listener.exitIfStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfStatement" ):
                return visitor.visitIfStatement(self)
            else:
                return visitor.visitChildren(self)




    def ifStatement(self):

        localctx = MiniCParserParser.IfStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_ifStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 138
            self.match(MiniCParserParser.T__8)
            self.state = 139
            self.match(MiniCParserParser.T__5)
            self.state = 140
            self.expression()
            self.state = 141
            self.match(MiniCParserParser.T__6)
            self.state = 142
            self.statement()
            self.state = 145
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.state = 143
                self.match(MiniCParserParser.T__9)
                self.state = 144
                self.statement()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WhileStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(MiniCParserParser.ExpressionContext,0)


        def statement(self):
            return self.getTypedRuleContext(MiniCParserParser.StatementContext,0)


        def getRuleIndex(self):
            return MiniCParserParser.RULE_whileStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhileStatement" ):
                listener.enterWhileStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhileStatement" ):
                listener.exitWhileStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhileStatement" ):
                return visitor.visitWhileStatement(self)
            else:
                return visitor.visitChildren(self)




    def whileStatement(self):

        localctx = MiniCParserParser.WhileStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_whileStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 147
            self.match(MiniCParserParser.T__10)
            self.state = 148
            self.match(MiniCParserParser.T__5)
            self.state = 149
            self.expression()
            self.state = 150
            self.match(MiniCParserParser.T__6)
            self.state = 151
            self.statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self):
            return self.getTypedRuleContext(MiniCParserParser.StatementContext,0)


        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniCParserParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MiniCParserParser.ExpressionContext,i)


        def getRuleIndex(self):
            return MiniCParserParser.RULE_forStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForStatement" ):
                listener.enterForStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForStatement" ):
                listener.exitForStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForStatement" ):
                return visitor.visitForStatement(self)
            else:
                return visitor.visitChildren(self)




    def forStatement(self):

        localctx = MiniCParserParser.ForStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_forStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 153
            self.match(MiniCParserParser.T__11)
            self.state = 154
            self.match(MiniCParserParser.T__5)
            self.state = 156
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.state = 155
                self.expression()


            self.state = 158
            self.match(MiniCParserParser.T__3)
            self.state = 160
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.state = 159
                self.expression()


            self.state = 162
            self.match(MiniCParserParser.T__3)
            self.state = 164
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 905969758) != 0):
                self.state = 163
                self.expression()


            self.state = 166
            self.match(MiniCParserParser.T__6)
            self.state = 167
            self.statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturnStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(MiniCParserParser.ExpressionContext,0)


        def getRuleIndex(self):
            return MiniCParserParser.RULE_returnStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReturnStatement" ):
                listener.enterReturnStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReturnStatement" ):
                listener.exitReturnStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturnStatement" ):
                return visitor.visitReturnStatement(self)
            else:
                return visitor.visitChildren(self)




    def returnStatement(self):

        localctx = MiniCParserParser.ReturnStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_returnStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 169
            self.match(MiniCParserParser.T__12)
            self.state = 171
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.state = 170
                self.expression()


            self.state = 173
            self.match(MiniCParserParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IoStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING_LITERAL(self):
            return self.getToken(MiniCParserParser.STRING_LITERAL, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniCParserParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MiniCParserParser.ExpressionContext,i)


        def getRuleIndex(self):
            return MiniCParserParser.RULE_ioStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIoStatement" ):
                listener.enterIoStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIoStatement" ):
                listener.exitIoStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIoStatement" ):
                return visitor.visitIoStatement(self)
            else:
                return visitor.visitChildren(self)




    def ioStatement(self):

        localctx = MiniCParserParser.IoStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_ioStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 175
            _la = self._input.LA(1)
            if not(_la==14 or _la==15):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 176
            self.match(MiniCParserParser.T__5)
            self.state = 177
            self.match(MiniCParserParser.T__4)
            self.state = 182
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==8:
                self.state = 178
                self.match(MiniCParserParser.T__7)
                self.state = 179
                self.expression()
                self.state = 184
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 185
            self.match(MiniCParserParser.T__6)
            self.state = 186
            self.match(MiniCParserParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignment(self):
            return self.getTypedRuleContext(MiniCParserParser.AssignmentContext,0)


        def getRuleIndex(self):
            return MiniCParserParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)




    def expression(self):

        localctx = MiniCParserParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 188
            self.assignment()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def logicOr(self):
            return self.getTypedRuleContext(MiniCParserParser.LogicOrContext,0)


        def assignment(self):
            return self.getTypedRuleContext(MiniCParserParser.AssignmentContext,0)


        def getRuleIndex(self):
            return MiniCParserParser.RULE_assignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment" ):
                listener.enterAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment" ):
                listener.exitAssignment(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment" ):
                return visitor.visitAssignment(self)
            else:
                return visitor.visitChildren(self)




    def assignment(self):

        localctx = MiniCParserParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_assignment)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 190
            self.logicOr()
            self.state = 193
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==5:
                self.state = 191
                self.match(MiniCParserParser.T__4)
                self.state = 192
                self.assignment()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LogicOrContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def logicAnd(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniCParserParser.LogicAndContext)
            else:
                return self.getTypedRuleContext(MiniCParserParser.LogicAndContext,i)


        def getRuleIndex(self):
            return MiniCParserParser.RULE_logicOr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLogicOr" ):
                listener.enterLogicOr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLogicOr" ):
                listener.exitLogicOr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogicOr" ):
                return visitor.visitLogicOr(self)
            else:
                return visitor.visitChildren(self)




    def logicOr(self):

        localctx = MiniCParserParser.LogicOrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_logicOr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 195
            self.logicAnd()
            self.state = 200
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==16:
                self.state = 196
                self.match(MiniCParserParser.T__15)
                self.state = 197
                self.logicAnd()
                self.state = 202
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LogicAndContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def equality(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniCParserParser.EqualityContext)
            else:
                return self.getTypedRuleContext(MiniCParserParser.EqualityContext,i)


        def getRuleIndex(self):
            return MiniCParserParser.RULE_logicAnd

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLogicAnd" ):
                listener.enterLogicAnd(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLogicAnd" ):
                listener.exitLogicAnd(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogicAnd" ):
                return visitor.visitLogicAnd(self)
            else:
                return visitor.visitChildren(self)




    def logicAnd(self):

        localctx = MiniCParserParser.LogicAndContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_logicAnd)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 203
            self.equality()
            self.state = 208
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==17:
                self.state = 204
                self.match(MiniCParserParser.T__16)
                self.state = 205
                self.equality()
                self.state = 210
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EqualityContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def relational(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniCParserParser.RelationalContext)
            else:
                return self.getTypedRuleContext(MiniCParserParser.RelationalContext,i)


        def getRuleIndex(self):
            return MiniCParserParser.RULE_equality

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEquality" ):
                listener.enterEquality(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEquality" ):
                listener.exitEquality(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEquality" ):
                return visitor.visitEquality(self)
            else:
                return visitor.visitChildren(self)




    def equality(self):

        localctx = MiniCParserParser.EqualityContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_equality)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 211
            self.relational()
            self.state = 216
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==18 or _la==19:
                self.state = 212
                _la = self._input.LA(1)
                if not(_la==18 or _la==19):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 213
                self.relational()
                self.state = 218
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RelationalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def additive(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniCParserParser.AdditiveContext)
            else:
                return self.getTypedRuleContext(MiniCParserParser.AdditiveContext,i)


        def getRuleIndex(self):
            return MiniCParserParser.RULE_relational

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRelational" ):
                listener.enterRelational(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRelational" ):
                listener.exitRelational(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRelational" ):
                return visitor.visitRelational(self)
            else:
                return visitor.visitChildren(self)




    def relational(self):

        localctx = MiniCParserParser.RelationalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_relational)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 219
            self.additive()
            self.state = 224
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 15728640) != 0):
                self.state = 220
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 15728640) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 221
                self.additive()
                self.state = 226
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AdditiveContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def multiplicative(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniCParserParser.MultiplicativeContext)
            else:
                return self.getTypedRuleContext(MiniCParserParser.MultiplicativeContext,i)


        def getRuleIndex(self):
            return MiniCParserParser.RULE_additive

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAdditive" ):
                listener.enterAdditive(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAdditive" ):
                listener.exitAdditive(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAdditive" ):
                return visitor.visitAdditive(self)
            else:
                return visitor.visitChildren(self)




    def additive(self):

        localctx = MiniCParserParser.AdditiveContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_additive)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 227
            self.multiplicative()
            self.state = 232
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==24 or _la==25:
                self.state = 228
                _la = self._input.LA(1)
                if not(_la==24 or _la==25):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 229
                self.multiplicative()
                self.state = 234
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MultiplicativeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def unary(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniCParserParser.UnaryContext)
            else:
                return self.getTypedRuleContext(MiniCParserParser.UnaryContext,i)


        def getRuleIndex(self):
            return MiniCParserParser.RULE_multiplicative

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMultiplicative" ):
                listener.enterMultiplicative(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMultiplicative" ):
                listener.exitMultiplicative(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMultiplicative" ):
                return visitor.visitMultiplicative(self)
            else:
                return visitor.visitChildren(self)




    def multiplicative(self):

        localctx = MiniCParserParser.MultiplicativeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_multiplicative)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 235
            self.unary()
            self.state = 240
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==26 or _la==27:
                self.state = 236
                _la = self._input.LA(1)
                if not(_la==26 or _la==27):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 237
                self.unary()
                self.state = 242
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UnaryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def postfix(self):
            return self.getTypedRuleContext(MiniCParserParser.PostfixContext,0)


        def getRuleIndex(self):
            return MiniCParserParser.RULE_unary

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnary" ):
                listener.enterUnary(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnary" ):
                listener.exitUnary(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnary" ):
                return visitor.visitUnary(self)
            else:
                return visitor.visitChildren(self)




    def unary(self):

        localctx = MiniCParserParser.UnaryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_unary)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 244
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 905969664) != 0):
                self.state = 243
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 905969664) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()


            self.state = 246
            self.postfix()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PostfixContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primary(self):
            return self.getTypedRuleContext(MiniCParserParser.PrimaryContext,0)


        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(MiniCParserParser.ID)
            else:
                return self.getToken(MiniCParserParser.ID, i)

        def getRuleIndex(self):
            return MiniCParserParser.RULE_postfix

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPostfix" ):
                listener.enterPostfix(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPostfix" ):
                listener.exitPostfix(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPostfix" ):
                return visitor.visitPostfix(self)
            else:
                return visitor.visitChildren(self)




    def postfix(self):

        localctx = MiniCParserParser.PostfixContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_postfix)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 248
            self.primary()
            self.state = 253
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==30:
                self.state = 249
                self.match(MiniCParserParser.T__29)
                self.state = 250
                self.match(MiniCParserParser.T__0)
                self.state = 255
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrimaryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT_LITERAL(self):
            return self.getToken(MiniCParserParser.INT_LITERAL, 0)

        def CHAR_LITERAL(self):
            return self.getToken(MiniCParserParser.CHAR_LITERAL, 0)

        def BOOL_LITERAL(self):
            return self.getToken(MiniCParserParser.BOOL_LITERAL, 0)

        def ID(self):
            return self.getToken(MiniCParserParser.ID, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniCParserParser.ExpressionContext,0)


        def getRuleIndex(self):
            return MiniCParserParser.RULE_primary

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrimary" ):
                listener.enterPrimary(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrimary" ):
                listener.exitPrimary(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimary" ):
                return visitor.visitPrimary(self)
            else:
                return visitor.visitChildren(self)




    def primary(self):

        localctx = MiniCParserParser.PrimaryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_primary)
        try:
            self.state = 264
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2]:
                self.enterOuterAlt(localctx, 1)
                self.state = 256
                self.match(MiniCParserParser.T__1)
                pass
            elif token in [3]:
                self.enterOuterAlt(localctx, 2)
                self.state = 257
                self.match(MiniCParserParser.T__2)
                pass
            elif token in [4]:
                self.enterOuterAlt(localctx, 3)
                self.state = 258
                self.match(MiniCParserParser.T__3)
                pass
            elif token in [1]:
                self.enterOuterAlt(localctx, 4)
                self.state = 259
                self.match(MiniCParserParser.T__0)
                pass
            elif token in [6]:
                self.enterOuterAlt(localctx, 5)
                self.state = 260
                self.match(MiniCParserParser.T__5)
                self.state = 261
                self.expression()
                self.state = 262
                self.match(MiniCParserParser.T__6)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def structType(self):
            return self.getTypedRuleContext(MiniCParserParser.StructTypeContext,0)


        def pointer(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniCParserParser.PointerContext)
            else:
                return self.getTypedRuleContext(MiniCParserParser.PointerContext,i)


        def getRuleIndex(self):
            return MiniCParserParser.RULE_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterType" ):
                listener.enterType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitType" ):
                listener.exitType(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitType" ):
                return visitor.visitType(self)
            else:
                return visitor.visitChildren(self)




    def type_(self):

        localctx = MiniCParserParser.TypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 270
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [31]:
                self.state = 266
                self.match(MiniCParserParser.T__30)
                pass
            elif token in [32]:
                self.state = 267
                self.match(MiniCParserParser.T__31)
                pass
            elif token in [33]:
                self.state = 268
                self.match(MiniCParserParser.T__32)
                pass
            elif token in [1]:
                self.state = 269
                self.structType()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 275
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,26,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 272
                    self.pointer() 
                self.state = 277
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,26,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PointerContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MiniCParserParser.RULE_pointer

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPointer" ):
                listener.enterPointer(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPointer" ):
                listener.exitPointer(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPointer" ):
                return visitor.visitPointer(self)
            else:
                return visitor.visitChildren(self)




    def pointer(self):

        localctx = MiniCParserParser.PointerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_pointer)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 278
            self.match(MiniCParserParser.T__25)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StructTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniCParserParser.ID, 0)

        def getRuleIndex(self):
            return MiniCParserParser.RULE_structType

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStructType" ):
                listener.enterStructType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStructType" ):
                listener.exitStructType(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStructType" ):
                return visitor.visitStructType(self)
            else:
                return visitor.visitChildren(self)




    def structType(self):

        localctx = MiniCParserParser.StructTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_structType)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 280
            self.match(MiniCParserParser.T__0)
            self.state = 281
            self.match(MiniCParserParser.T__0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclaratorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniCParserParser.ID, 0)

        def pointer(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniCParserParser.PointerContext)
            else:
                return self.getTypedRuleContext(MiniCParserParser.PointerContext,i)


        def getRuleIndex(self):
            return MiniCParserParser.RULE_declarator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclarator" ):
                listener.enterDeclarator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclarator" ):
                listener.exitDeclarator(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclarator" ):
                return visitor.visitDeclarator(self)
            else:
                return visitor.visitChildren(self)




    def declarator(self):

        localctx = MiniCParserParser.DeclaratorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_declarator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 286
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==26:
                self.state = 283
                self.pointer()
                self.state = 288
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 289
            self.match(MiniCParserParser.T__0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





