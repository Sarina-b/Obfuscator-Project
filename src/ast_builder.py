from antlr_gen.MiniCParserVisitor import MiniCParserVisitor
from antlr_gen.MiniCParserParser import *

class ASTNode:
    def __init__(self, type_, children=None, value=None):
        self.type = type_
        self.children = children or []
        self.value = value

    def __repr__(self):
        return f"{self.type}({self.value}) -> {self.children}"