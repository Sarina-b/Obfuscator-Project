# Generated from /grammars/MiniC.g4 by ANTLR 4.13.1
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
        4,1,45,286,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        1,0,1,0,1,0,5,0,58,8,0,10,0,12,0,61,9,0,1,0,1,0,1,1,1,1,1,1,1,1,
        3,1,69,8,1,1,1,1,1,1,1,1,2,1,2,1,2,1,2,5,2,78,8,2,10,2,12,2,81,9,
        2,1,2,1,2,1,3,1,3,1,3,1,3,1,4,1,4,1,4,5,4,92,8,4,10,4,12,4,95,9,
        4,1,5,1,5,1,5,3,5,100,8,5,1,6,1,6,5,6,104,8,6,10,6,12,6,107,9,6,
        1,7,1,7,1,8,1,8,1,9,1,9,1,9,5,9,116,8,9,10,9,12,9,119,9,9,1,10,1,
        10,1,10,1,11,1,11,5,11,126,8,11,10,11,12,11,129,9,11,1,11,1,11,1,
        12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,3,
        12,146,8,12,1,13,1,13,1,13,1,13,1,13,1,14,1,14,1,14,1,14,1,14,1,
        14,1,14,1,14,5,14,161,8,14,10,14,12,14,164,9,14,1,15,1,15,1,15,1,
        16,1,16,1,16,1,16,1,16,1,16,1,16,3,16,176,8,16,1,17,1,17,1,17,1,
        17,1,17,1,17,1,18,1,18,1,18,1,18,1,18,3,18,189,8,18,1,18,3,18,192,
        8,18,1,18,1,18,3,18,196,8,18,1,18,1,18,1,18,1,19,1,19,3,19,203,8,
        19,1,19,1,19,1,20,1,20,1,20,3,20,210,8,20,1,20,1,20,1,21,1,21,1,
        21,5,21,217,8,21,10,21,12,21,220,9,21,1,22,1,22,1,22,1,22,1,22,3,
        22,227,8,22,1,22,1,22,1,22,1,22,1,22,1,22,1,22,3,22,236,8,22,1,22,
        3,22,239,8,22,1,23,1,23,1,23,5,23,244,8,23,10,23,12,23,247,9,23,
        1,24,1,24,1,24,1,24,1,24,1,24,1,24,1,24,1,24,1,24,1,24,3,24,260,
        8,24,1,24,1,24,1,24,1,24,1,24,1,24,1,24,1,24,1,24,1,24,1,24,1,24,
        1,24,1,24,1,24,5,24,277,8,24,10,24,12,24,280,9,24,1,25,1,25,1,26,
        1,26,1,26,0,1,48,27,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,
        34,36,38,40,42,44,46,48,50,52,0,8,2,0,9,11,42,42,2,0,12,12,25,26,
        1,0,27,28,1,0,29,32,1,0,33,34,1,0,35,36,2,0,28,28,37,37,1,0,38,40,
        300,0,59,1,0,0,0,2,64,1,0,0,0,4,73,1,0,0,0,6,84,1,0,0,0,8,88,1,0,
        0,0,10,96,1,0,0,0,12,101,1,0,0,0,14,108,1,0,0,0,16,110,1,0,0,0,18,
        112,1,0,0,0,20,120,1,0,0,0,22,123,1,0,0,0,24,145,1,0,0,0,26,147,
        1,0,0,0,28,152,1,0,0,0,30,165,1,0,0,0,32,168,1,0,0,0,34,177,1,0,
        0,0,36,183,1,0,0,0,38,200,1,0,0,0,40,206,1,0,0,0,42,213,1,0,0,0,
        44,238,1,0,0,0,46,240,1,0,0,0,48,259,1,0,0,0,50,281,1,0,0,0,52,283,
        1,0,0,0,54,58,3,2,1,0,55,58,3,4,2,0,56,58,3,6,3,0,57,54,1,0,0,0,
        57,55,1,0,0,0,57,56,1,0,0,0,58,61,1,0,0,0,59,57,1,0,0,0,59,60,1,
        0,0,0,60,62,1,0,0,0,61,59,1,0,0,0,62,63,5,0,0,1,63,1,1,0,0,0,64,
        65,3,12,6,0,65,66,5,42,0,0,66,68,5,1,0,0,67,69,3,18,9,0,68,67,1,
        0,0,0,68,69,1,0,0,0,69,70,1,0,0,0,70,71,5,2,0,0,71,72,3,22,11,0,
        72,3,1,0,0,0,73,74,5,3,0,0,74,75,5,42,0,0,75,79,5,4,0,0,76,78,3,
        6,3,0,77,76,1,0,0,0,78,81,1,0,0,0,79,77,1,0,0,0,79,80,1,0,0,0,80,
        82,1,0,0,0,81,79,1,0,0,0,82,83,5,5,0,0,83,5,1,0,0,0,84,85,3,12,6,
        0,85,86,3,8,4,0,86,87,5,6,0,0,87,7,1,0,0,0,88,93,3,10,5,0,89,90,
        5,7,0,0,90,92,3,10,5,0,91,89,1,0,0,0,92,95,1,0,0,0,93,91,1,0,0,0,
        93,94,1,0,0,0,94,9,1,0,0,0,95,93,1,0,0,0,96,99,5,42,0,0,97,98,5,
        8,0,0,98,100,3,48,24,0,99,97,1,0,0,0,99,100,1,0,0,0,100,11,1,0,0,
        0,101,105,3,14,7,0,102,104,3,16,8,0,103,102,1,0,0,0,104,107,1,0,
        0,0,105,103,1,0,0,0,105,106,1,0,0,0,106,13,1,0,0,0,107,105,1,0,0,
        0,108,109,7,0,0,0,109,15,1,0,0,0,110,111,5,12,0,0,111,17,1,0,0,0,
        112,117,3,20,10,0,113,114,5,7,0,0,114,116,3,20,10,0,115,113,1,0,
        0,0,116,119,1,0,0,0,117,115,1,0,0,0,117,118,1,0,0,0,118,19,1,0,0,
        0,119,117,1,0,0,0,120,121,3,12,6,0,121,122,5,42,0,0,122,21,1,0,0,
        0,123,127,5,4,0,0,124,126,3,24,12,0,125,124,1,0,0,0,126,129,1,0,
        0,0,127,125,1,0,0,0,127,128,1,0,0,0,128,130,1,0,0,0,129,127,1,0,
        0,0,130,131,5,5,0,0,131,23,1,0,0,0,132,146,3,6,3,0,133,146,3,26,
        13,0,134,146,3,32,16,0,135,146,3,34,17,0,136,146,3,36,18,0,137,146,
        3,38,19,0,138,139,3,40,20,0,139,140,5,6,0,0,140,146,1,0,0,0,141,
        142,3,44,22,0,142,143,5,6,0,0,143,146,1,0,0,0,144,146,3,22,11,0,
        145,132,1,0,0,0,145,133,1,0,0,0,145,134,1,0,0,0,145,135,1,0,0,0,
        145,136,1,0,0,0,145,137,1,0,0,0,145,138,1,0,0,0,145,141,1,0,0,0,
        145,144,1,0,0,0,146,25,1,0,0,0,147,148,3,28,14,0,148,149,5,8,0,0,
        149,150,3,48,24,0,150,151,5,6,0,0,151,27,1,0,0,0,152,162,5,42,0,
        0,153,154,5,13,0,0,154,155,3,48,24,0,155,156,5,14,0,0,156,161,1,
        0,0,0,157,158,5,15,0,0,158,161,5,42,0,0,159,161,3,30,15,0,160,153,
        1,0,0,0,160,157,1,0,0,0,160,159,1,0,0,0,161,164,1,0,0,0,162,160,
        1,0,0,0,162,163,1,0,0,0,163,29,1,0,0,0,164,162,1,0,0,0,165,166,5,
        16,0,0,166,167,5,42,0,0,167,31,1,0,0,0,168,169,5,17,0,0,169,170,
        5,1,0,0,170,171,3,48,24,0,171,172,5,2,0,0,172,175,3,24,12,0,173,
        174,5,18,0,0,174,176,3,24,12,0,175,173,1,0,0,0,175,176,1,0,0,0,176,
        33,1,0,0,0,177,178,5,19,0,0,178,179,5,1,0,0,179,180,3,48,24,0,180,
        181,5,2,0,0,181,182,3,24,12,0,182,35,1,0,0,0,183,184,5,20,0,0,184,
        188,5,1,0,0,185,189,3,6,3,0,186,189,3,26,13,0,187,189,5,6,0,0,188,
        185,1,0,0,0,188,186,1,0,0,0,188,187,1,0,0,0,189,191,1,0,0,0,190,
        192,3,48,24,0,191,190,1,0,0,0,191,192,1,0,0,0,192,193,1,0,0,0,193,
        195,5,6,0,0,194,196,3,48,24,0,195,194,1,0,0,0,195,196,1,0,0,0,196,
        197,1,0,0,0,197,198,5,2,0,0,198,199,3,24,12,0,199,37,1,0,0,0,200,
        202,5,21,0,0,201,203,3,48,24,0,202,201,1,0,0,0,202,203,1,0,0,0,203,
        204,1,0,0,0,204,205,5,6,0,0,205,39,1,0,0,0,206,207,5,42,0,0,207,
        209,5,1,0,0,208,210,3,42,21,0,209,208,1,0,0,0,209,210,1,0,0,0,210,
        211,1,0,0,0,211,212,5,2,0,0,212,41,1,0,0,0,213,218,3,48,24,0,214,
        215,5,7,0,0,215,217,3,48,24,0,216,214,1,0,0,0,217,220,1,0,0,0,218,
        216,1,0,0,0,218,219,1,0,0,0,219,43,1,0,0,0,220,218,1,0,0,0,221,222,
        5,22,0,0,222,223,5,1,0,0,223,224,5,41,0,0,224,226,5,7,0,0,225,227,
        5,23,0,0,226,225,1,0,0,0,226,227,1,0,0,0,227,228,1,0,0,0,228,229,
        5,42,0,0,229,239,5,2,0,0,230,231,5,24,0,0,231,232,5,1,0,0,232,235,
        5,41,0,0,233,234,5,7,0,0,234,236,3,46,23,0,235,233,1,0,0,0,235,236,
        1,0,0,0,236,237,1,0,0,0,237,239,5,2,0,0,238,221,1,0,0,0,238,230,
        1,0,0,0,239,45,1,0,0,0,240,245,3,48,24,0,241,242,5,7,0,0,242,244,
        3,48,24,0,243,241,1,0,0,0,244,247,1,0,0,0,245,243,1,0,0,0,245,246,
        1,0,0,0,246,47,1,0,0,0,247,245,1,0,0,0,248,249,6,24,-1,0,249,250,
        3,50,25,0,250,251,3,48,24,5,251,260,1,0,0,0,252,253,5,1,0,0,253,
        254,3,48,24,0,254,255,5,2,0,0,255,260,1,0,0,0,256,260,3,52,26,0,
        257,260,3,40,20,0,258,260,3,28,14,0,259,248,1,0,0,0,259,252,1,0,
        0,0,259,256,1,0,0,0,259,257,1,0,0,0,259,258,1,0,0,0,260,278,1,0,
        0,0,261,262,10,10,0,0,262,263,7,1,0,0,263,277,3,48,24,11,264,265,
        10,9,0,0,265,266,7,2,0,0,266,277,3,48,24,10,267,268,10,8,0,0,268,
        269,7,3,0,0,269,277,3,48,24,9,270,271,10,7,0,0,271,272,7,4,0,0,272,
        277,3,48,24,8,273,274,10,6,0,0,274,275,7,5,0,0,275,277,3,48,24,7,
        276,261,1,0,0,0,276,264,1,0,0,0,276,267,1,0,0,0,276,270,1,0,0,0,
        276,273,1,0,0,0,277,280,1,0,0,0,278,276,1,0,0,0,278,279,1,0,0,0,
        279,49,1,0,0,0,280,278,1,0,0,0,281,282,7,6,0,0,282,51,1,0,0,0,283,
        284,7,7,0,0,284,53,1,0,0,0,26,57,59,68,79,93,99,105,117,127,145,
        160,162,175,188,191,195,202,209,218,226,235,238,245,259,276,278
    ]

class MiniCParser ( Parser ):

    grammarFileName = "MiniC.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "'struct'", "'{'", "'}'", 
                     "';'", "','", "'='", "'int'", "'char'", "'bool'", "'*'", 
                     "'['", "']'", "'.'", "'->'", "'if'", "'else'", "'while'", 
                     "'for'", "'return'", "'scanf'", "'&'", "'printf'", 
                     "'/'", "'%'", "'+'", "'-'", "'<'", "'<='", "'>'", "'>='", 
                     "'=='", "'!='", "'&&'", "'||'", "'!'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "BOOL", "INT", "CHAR", "STRING", 
                      "ID", "WS", "COMMENT", "LINE_COMMENT" ]

    RULE_program = 0
    RULE_functionDecl = 1
    RULE_structDecl = 2
    RULE_varDecl = 3
    RULE_varDeclList = 4
    RULE_varDeclItem = 5
    RULE_typ = 6
    RULE_baseType = 7
    RULE_pointerType = 8
    RULE_paramList = 9
    RULE_param = 10
    RULE_block = 11
    RULE_statement = 12
    RULE_assignStat = 13
    RULE_lvalue = 14
    RULE_pointerDereference = 15
    RULE_ifStat = 16
    RULE_whileStat = 17
    RULE_forStat = 18
    RULE_returnStat = 19
    RULE_funcCall = 20
    RULE_argumentList = 21
    RULE_ioStat = 22
    RULE_expressionList = 23
    RULE_expression = 24
    RULE_unaryOp = 25
    RULE_literal = 26

    ruleNames =  [ "program", "functionDecl", "structDecl", "varDecl", "varDeclList", 
                   "varDeclItem", "typ", "baseType", "pointerType", "paramList", 
                   "param", "block", "statement", "assignStat", "lvalue", 
                   "pointerDereference", "ifStat", "whileStat", "forStat", 
                   "returnStat", "funcCall", "argumentList", "ioStat", "expressionList", 
                   "expression", "unaryOp", "literal" ]

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
    T__33=34
    T__34=35
    T__35=36
    T__36=37
    BOOL=38
    INT=39
    CHAR=40
    STRING=41
    ID=42
    WS=43
    COMMENT=44
    LINE_COMMENT=45

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
            return self.getToken(MiniCParser.EOF, 0)

        def functionDecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniCParser.FunctionDeclContext)
            else:
                return self.getTypedRuleContext(MiniCParser.FunctionDeclContext,i)


        def structDecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniCParser.StructDeclContext)
            else:
                return self.getTypedRuleContext(MiniCParser.StructDeclContext,i)


        def varDecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniCParser.VarDeclContext)
            else:
                return self.getTypedRuleContext(MiniCParser.VarDeclContext,i)


        def getRuleIndex(self):
            return MiniCParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)




    def program(self):

        localctx = MiniCParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 59
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 4398046514696) != 0):
                self.state = 57
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
                if la_ == 1:
                    self.state = 54
                    self.functionDecl()
                    pass

                elif la_ == 2:
                    self.state = 55
                    self.structDecl()
                    pass

                elif la_ == 3:
                    self.state = 56
                    self.varDecl()
                    pass


                self.state = 61
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 62
            self.match(MiniCParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typ(self):
            return self.getTypedRuleContext(MiniCParser.TypContext,0)


        def ID(self):
            return self.getToken(MiniCParser.ID, 0)

        def block(self):
            return self.getTypedRuleContext(MiniCParser.BlockContext,0)


        def paramList(self):
            return self.getTypedRuleContext(MiniCParser.ParamListContext,0)


        def getRuleIndex(self):
            return MiniCParser.RULE_functionDecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionDecl" ):
                listener.enterFunctionDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionDecl" ):
                listener.exitFunctionDecl(self)




    def functionDecl(self):

        localctx = MiniCParser.FunctionDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_functionDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 64
            self.typ()
            self.state = 65
            self.match(MiniCParser.ID)
            self.state = 66
            self.match(MiniCParser.T__0)
            self.state = 68
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 4398046514688) != 0):
                self.state = 67
                self.paramList()


            self.state = 70
            self.match(MiniCParser.T__1)
            self.state = 71
            self.block()
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
            return self.getToken(MiniCParser.ID, 0)

        def varDecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniCParser.VarDeclContext)
            else:
                return self.getTypedRuleContext(MiniCParser.VarDeclContext,i)


        def getRuleIndex(self):
            return MiniCParser.RULE_structDecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStructDecl" ):
                listener.enterStructDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStructDecl" ):
                listener.exitStructDecl(self)




    def structDecl(self):

        localctx = MiniCParser.StructDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_structDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 73
            self.match(MiniCParser.T__2)
            self.state = 74
            self.match(MiniCParser.ID)
            self.state = 75
            self.match(MiniCParser.T__3)
            self.state = 79
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 4398046514688) != 0):
                self.state = 76
                self.varDecl()
                self.state = 81
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 82
            self.match(MiniCParser.T__4)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typ(self):
            return self.getTypedRuleContext(MiniCParser.TypContext,0)


        def varDeclList(self):
            return self.getTypedRuleContext(MiniCParser.VarDeclListContext,0)


        def getRuleIndex(self):
            return MiniCParser.RULE_varDecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVarDecl" ):
                listener.enterVarDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVarDecl" ):
                listener.exitVarDecl(self)




    def varDecl(self):

        localctx = MiniCParser.VarDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_varDecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 84
            self.typ()
            self.state = 85
            self.varDeclList()
            self.state = 86
            self.match(MiniCParser.T__5)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarDeclListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def varDeclItem(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniCParser.VarDeclItemContext)
            else:
                return self.getTypedRuleContext(MiniCParser.VarDeclItemContext,i)


        def getRuleIndex(self):
            return MiniCParser.RULE_varDeclList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVarDeclList" ):
                listener.enterVarDeclList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVarDeclList" ):
                listener.exitVarDeclList(self)




    def varDeclList(self):

        localctx = MiniCParser.VarDeclListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_varDeclList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 88
            self.varDeclItem()
            self.state = 93
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==7:
                self.state = 89
                self.match(MiniCParser.T__6)
                self.state = 90
                self.varDeclItem()
                self.state = 95
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarDeclItemContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniCParser.ID, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniCParser.ExpressionContext,0)


        def getRuleIndex(self):
            return MiniCParser.RULE_varDeclItem

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVarDeclItem" ):
                listener.enterVarDeclItem(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVarDeclItem" ):
                listener.exitVarDeclItem(self)




    def varDeclItem(self):

        localctx = MiniCParser.VarDeclItemContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_varDeclItem)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 96
            self.match(MiniCParser.ID)
            self.state = 99
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==8:
                self.state = 97
                self.match(MiniCParser.T__7)
                self.state = 98
                self.expression(0)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def baseType(self):
            return self.getTypedRuleContext(MiniCParser.BaseTypeContext,0)


        def pointerType(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniCParser.PointerTypeContext)
            else:
                return self.getTypedRuleContext(MiniCParser.PointerTypeContext,i)


        def getRuleIndex(self):
            return MiniCParser.RULE_typ

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTyp" ):
                listener.enterTyp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTyp" ):
                listener.exitTyp(self)




    def typ(self):

        localctx = MiniCParser.TypContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_typ)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 101
            self.baseType()
            self.state = 105
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==12:
                self.state = 102
                self.pointerType()
                self.state = 107
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BaseTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniCParser.ID, 0)

        def getRuleIndex(self):
            return MiniCParser.RULE_baseType

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBaseType" ):
                listener.enterBaseType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBaseType" ):
                listener.exitBaseType(self)




    def baseType(self):

        localctx = MiniCParser.BaseTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_baseType)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 108
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 4398046514688) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PointerTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MiniCParser.RULE_pointerType

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPointerType" ):
                listener.enterPointerType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPointerType" ):
                listener.exitPointerType(self)




    def pointerType(self):

        localctx = MiniCParser.PointerTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_pointerType)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 110
            self.match(MiniCParser.T__11)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def param(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniCParser.ParamContext)
            else:
                return self.getTypedRuleContext(MiniCParser.ParamContext,i)


        def getRuleIndex(self):
            return MiniCParser.RULE_paramList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParamList" ):
                listener.enterParamList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParamList" ):
                listener.exitParamList(self)




    def paramList(self):

        localctx = MiniCParser.ParamListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_paramList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 112
            self.param()
            self.state = 117
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==7:
                self.state = 113
                self.match(MiniCParser.T__6)
                self.state = 114
                self.param()
                self.state = 119
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typ(self):
            return self.getTypedRuleContext(MiniCParser.TypContext,0)


        def ID(self):
            return self.getToken(MiniCParser.ID, 0)

        def getRuleIndex(self):
            return MiniCParser.RULE_param

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParam" ):
                listener.enterParam(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParam" ):
                listener.exitParam(self)




    def param(self):

        localctx = MiniCParser.ParamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_param)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 120
            self.typ()
            self.state = 121
            self.match(MiniCParser.ID)
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
                return self.getTypedRuleContexts(MiniCParser.StatementContext)
            else:
                return self.getTypedRuleContext(MiniCParser.StatementContext,i)


        def getRuleIndex(self):
            return MiniCParser.RULE_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock" ):
                listener.enterBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock" ):
                listener.exitBlock(self)




    def block(self):

        localctx = MiniCParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 123
            self.match(MiniCParser.T__3)
            self.state = 127
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 4398071287312) != 0):
                self.state = 124
                self.statement()
                self.state = 129
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 130
            self.match(MiniCParser.T__4)
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

        def varDecl(self):
            return self.getTypedRuleContext(MiniCParser.VarDeclContext,0)


        def assignStat(self):
            return self.getTypedRuleContext(MiniCParser.AssignStatContext,0)


        def ifStat(self):
            return self.getTypedRuleContext(MiniCParser.IfStatContext,0)


        def whileStat(self):
            return self.getTypedRuleContext(MiniCParser.WhileStatContext,0)


        def forStat(self):
            return self.getTypedRuleContext(MiniCParser.ForStatContext,0)


        def returnStat(self):
            return self.getTypedRuleContext(MiniCParser.ReturnStatContext,0)


        def funcCall(self):
            return self.getTypedRuleContext(MiniCParser.FuncCallContext,0)


        def ioStat(self):
            return self.getTypedRuleContext(MiniCParser.IoStatContext,0)


        def block(self):
            return self.getTypedRuleContext(MiniCParser.BlockContext,0)


        def getRuleIndex(self):
            return MiniCParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)




    def statement(self):

        localctx = MiniCParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_statement)
        try:
            self.state = 145
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 132
                self.varDecl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 133
                self.assignStat()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 134
                self.ifStat()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 135
                self.whileStat()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 136
                self.forStat()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 137
                self.returnStat()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 138
                self.funcCall()
                self.state = 139
                self.match(MiniCParser.T__5)
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 141
                self.ioStat()
                self.state = 142
                self.match(MiniCParser.T__5)
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 144
                self.block()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignStatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lvalue(self):
            return self.getTypedRuleContext(MiniCParser.LvalueContext,0)


        def expression(self):
            return self.getTypedRuleContext(MiniCParser.ExpressionContext,0)


        def getRuleIndex(self):
            return MiniCParser.RULE_assignStat

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignStat" ):
                listener.enterAssignStat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignStat" ):
                listener.exitAssignStat(self)




    def assignStat(self):

        localctx = MiniCParser.AssignStatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_assignStat)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 147
            self.lvalue()
            self.state = 148
            self.match(MiniCParser.T__7)
            self.state = 149
            self.expression(0)
            self.state = 150
            self.match(MiniCParser.T__5)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LvalueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(MiniCParser.ID)
            else:
                return self.getToken(MiniCParser.ID, i)

        def pointerDereference(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniCParser.PointerDereferenceContext)
            else:
                return self.getTypedRuleContext(MiniCParser.PointerDereferenceContext,i)


        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniCParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MiniCParser.ExpressionContext,i)


        def getRuleIndex(self):
            return MiniCParser.RULE_lvalue

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLvalue" ):
                listener.enterLvalue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLvalue" ):
                listener.exitLvalue(self)




    def lvalue(self):

        localctx = MiniCParser.LvalueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_lvalue)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 152
            self.match(MiniCParser.ID)
            self.state = 162
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,11,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 160
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [13]:
                        self.state = 153
                        self.match(MiniCParser.T__12)
                        self.state = 154
                        self.expression(0)
                        self.state = 155
                        self.match(MiniCParser.T__13)
                        pass
                    elif token in [15]:
                        self.state = 157
                        self.match(MiniCParser.T__14)
                        self.state = 158
                        self.match(MiniCParser.ID)
                        pass
                    elif token in [16]:
                        self.state = 159
                        self.pointerDereference()
                        pass
                    else:
                        raise NoViableAltException(self)
             
                self.state = 164
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,11,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PointerDereferenceContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniCParser.ID, 0)

        def getRuleIndex(self):
            return MiniCParser.RULE_pointerDereference

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPointerDereference" ):
                listener.enterPointerDereference(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPointerDereference" ):
                listener.exitPointerDereference(self)




    def pointerDereference(self):

        localctx = MiniCParser.PointerDereferenceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_pointerDereference)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 165
            self.match(MiniCParser.T__15)
            self.state = 166
            self.match(MiniCParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfStatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(MiniCParser.ExpressionContext,0)


        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniCParser.StatementContext)
            else:
                return self.getTypedRuleContext(MiniCParser.StatementContext,i)


        def getRuleIndex(self):
            return MiniCParser.RULE_ifStat

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfStat" ):
                listener.enterIfStat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfStat" ):
                listener.exitIfStat(self)




    def ifStat(self):

        localctx = MiniCParser.IfStatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_ifStat)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 168
            self.match(MiniCParser.T__16)
            self.state = 169
            self.match(MiniCParser.T__0)
            self.state = 170
            self.expression(0)
            self.state = 171
            self.match(MiniCParser.T__1)
            self.state = 172
            self.statement()
            self.state = 175
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.state = 173
                self.match(MiniCParser.T__17)
                self.state = 174
                self.statement()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WhileStatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(MiniCParser.ExpressionContext,0)


        def statement(self):
            return self.getTypedRuleContext(MiniCParser.StatementContext,0)


        def getRuleIndex(self):
            return MiniCParser.RULE_whileStat

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhileStat" ):
                listener.enterWhileStat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhileStat" ):
                listener.exitWhileStat(self)




    def whileStat(self):

        localctx = MiniCParser.WhileStatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_whileStat)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 177
            self.match(MiniCParser.T__18)
            self.state = 178
            self.match(MiniCParser.T__0)
            self.state = 179
            self.expression(0)
            self.state = 180
            self.match(MiniCParser.T__1)
            self.state = 181
            self.statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForStatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self):
            return self.getTypedRuleContext(MiniCParser.StatementContext,0)


        def varDecl(self):
            return self.getTypedRuleContext(MiniCParser.VarDeclContext,0)


        def assignStat(self):
            return self.getTypedRuleContext(MiniCParser.AssignStatContext,0)


        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniCParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MiniCParser.ExpressionContext,i)


        def getRuleIndex(self):
            return MiniCParser.RULE_forStat

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForStat" ):
                listener.enterForStat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForStat" ):
                listener.exitForStat(self)




    def forStat(self):

        localctx = MiniCParser.ForStatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_forStat)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 183
            self.match(MiniCParser.T__19)
            self.state = 184
            self.match(MiniCParser.T__0)
            self.state = 188
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.state = 185
                self.varDecl()
                pass

            elif la_ == 2:
                self.state = 186
                self.assignStat()
                pass

            elif la_ == 3:
                self.state = 187
                self.match(MiniCParser.T__5)
                pass


            self.state = 191
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 6459899248642) != 0):
                self.state = 190
                self.expression(0)


            self.state = 193
            self.match(MiniCParser.T__5)
            self.state = 195
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 6459899248642) != 0):
                self.state = 194
                self.expression(0)


            self.state = 197
            self.match(MiniCParser.T__1)
            self.state = 198
            self.statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturnStatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(MiniCParser.ExpressionContext,0)


        def getRuleIndex(self):
            return MiniCParser.RULE_returnStat

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReturnStat" ):
                listener.enterReturnStat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReturnStat" ):
                listener.exitReturnStat(self)




    def returnStat(self):

        localctx = MiniCParser.ReturnStatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_returnStat)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 200
            self.match(MiniCParser.T__20)
            self.state = 202
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 6459899248642) != 0):
                self.state = 201
                self.expression(0)


            self.state = 204
            self.match(MiniCParser.T__5)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncCallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniCParser.ID, 0)

        def argumentList(self):
            return self.getTypedRuleContext(MiniCParser.ArgumentListContext,0)


        def getRuleIndex(self):
            return MiniCParser.RULE_funcCall

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFuncCall" ):
                listener.enterFuncCall(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFuncCall" ):
                listener.exitFuncCall(self)




    def funcCall(self):

        localctx = MiniCParser.FuncCallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_funcCall)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 206
            self.match(MiniCParser.ID)
            self.state = 207
            self.match(MiniCParser.T__0)
            self.state = 209
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 6459899248642) != 0):
                self.state = 208
                self.argumentList()


            self.state = 211
            self.match(MiniCParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgumentListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniCParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MiniCParser.ExpressionContext,i)


        def getRuleIndex(self):
            return MiniCParser.RULE_argumentList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArgumentList" ):
                listener.enterArgumentList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArgumentList" ):
                listener.exitArgumentList(self)




    def argumentList(self):

        localctx = MiniCParser.ArgumentListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_argumentList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 213
            self.expression(0)
            self.state = 218
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==7:
                self.state = 214
                self.match(MiniCParser.T__6)
                self.state = 215
                self.expression(0)
                self.state = 220
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IoStatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(MiniCParser.STRING, 0)

        def ID(self):
            return self.getToken(MiniCParser.ID, 0)

        def expressionList(self):
            return self.getTypedRuleContext(MiniCParser.ExpressionListContext,0)


        def getRuleIndex(self):
            return MiniCParser.RULE_ioStat

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIoStat" ):
                listener.enterIoStat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIoStat" ):
                listener.exitIoStat(self)




    def ioStat(self):

        localctx = MiniCParser.IoStatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_ioStat)
        self._la = 0 # Token type
        try:
            self.state = 238
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [22]:
                self.enterOuterAlt(localctx, 1)
                self.state = 221
                self.match(MiniCParser.T__21)
                self.state = 222
                self.match(MiniCParser.T__0)
                self.state = 223
                self.match(MiniCParser.STRING)
                self.state = 224
                self.match(MiniCParser.T__6)
                self.state = 226
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==23:
                    self.state = 225
                    self.match(MiniCParser.T__22)


                self.state = 228
                self.match(MiniCParser.ID)
                self.state = 229
                self.match(MiniCParser.T__1)
                pass
            elif token in [24]:
                self.enterOuterAlt(localctx, 2)
                self.state = 230
                self.match(MiniCParser.T__23)
                self.state = 231
                self.match(MiniCParser.T__0)
                self.state = 232
                self.match(MiniCParser.STRING)
                self.state = 235
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==7:
                    self.state = 233
                    self.match(MiniCParser.T__6)
                    self.state = 234
                    self.expressionList()


                self.state = 237
                self.match(MiniCParser.T__1)
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


    class ExpressionListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniCParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MiniCParser.ExpressionContext,i)


        def getRuleIndex(self):
            return MiniCParser.RULE_expressionList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpressionList" ):
                listener.enterExpressionList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpressionList" ):
                listener.exitExpressionList(self)




    def expressionList(self):

        localctx = MiniCParser.ExpressionListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_expressionList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 240
            self.expression(0)
            self.state = 245
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==7:
                self.state = 241
                self.match(MiniCParser.T__6)
                self.state = 242
                self.expression(0)
                self.state = 247
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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

        def unaryOp(self):
            return self.getTypedRuleContext(MiniCParser.UnaryOpContext,0)


        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniCParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MiniCParser.ExpressionContext,i)


        def literal(self):
            return self.getTypedRuleContext(MiniCParser.LiteralContext,0)


        def funcCall(self):
            return self.getTypedRuleContext(MiniCParser.FuncCallContext,0)


        def lvalue(self):
            return self.getTypedRuleContext(MiniCParser.LvalueContext,0)


        def getRuleIndex(self):
            return MiniCParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)



    def expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniCParser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 48
        self.enterRecursionRule(localctx, 48, self.RULE_expression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 259
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.state = 249
                self.unaryOp()
                self.state = 250
                self.expression(5)
                pass

            elif la_ == 2:
                self.state = 252
                self.match(MiniCParser.T__0)
                self.state = 253
                self.expression(0)
                self.state = 254
                self.match(MiniCParser.T__1)
                pass

            elif la_ == 3:
                self.state = 256
                self.literal()
                pass

            elif la_ == 4:
                self.state = 257
                self.funcCall()
                pass

            elif la_ == 5:
                self.state = 258
                self.lvalue()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 278
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,25,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 276
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
                    if la_ == 1:
                        localctx = MiniCParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 261
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 262
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 100667392) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 263
                        self.expression(11)
                        pass

                    elif la_ == 2:
                        localctx = MiniCParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 264
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 265
                        _la = self._input.LA(1)
                        if not(_la==27 or _la==28):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 266
                        self.expression(10)
                        pass

                    elif la_ == 3:
                        localctx = MiniCParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 267
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 268
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 8053063680) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 269
                        self.expression(9)
                        pass

                    elif la_ == 4:
                        localctx = MiniCParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 270
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 271
                        _la = self._input.LA(1)
                        if not(_la==33 or _la==34):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 272
                        self.expression(8)
                        pass

                    elif la_ == 5:
                        localctx = MiniCParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 273
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 274
                        _la = self._input.LA(1)
                        if not(_la==35 or _la==36):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 275
                        self.expression(7)
                        pass

             
                self.state = 280
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,25,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class UnaryOpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MiniCParser.RULE_unaryOp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnaryOp" ):
                listener.enterUnaryOp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnaryOp" ):
                listener.exitUnaryOp(self)




    def unaryOp(self):

        localctx = MiniCParser.UnaryOpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_unaryOp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 281
            _la = self._input.LA(1)
            if not(_la==28 or _la==37):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(MiniCParser.INT, 0)

        def CHAR(self):
            return self.getToken(MiniCParser.CHAR, 0)

        def BOOL(self):
            return self.getToken(MiniCParser.BOOL, 0)

        def getRuleIndex(self):
            return MiniCParser.RULE_literal

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLiteral" ):
                listener.enterLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLiteral" ):
                listener.exitLiteral(self)




    def literal(self):

        localctx = MiniCParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 283
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1924145348608) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[24] = self.expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 10)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 9)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 6)
         




