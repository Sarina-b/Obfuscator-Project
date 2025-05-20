mport sys
from antlr4 import FileStream, CommonTokenStream
from antlr_gen.MiniCLexer import MiniCLexer
from antlr_gen.MiniCParser import MiniCParser

from ast_builder import ASTBuilder
from obfuscator import Obfuscator
from generator import generate_code

def main():
    if len(sys.argv) != 2:
        print("Usage: python main.py <input_file.mc>")
        return

    input_file = sys.argv[1]

    # مرحله ۱: خواندن فایل و ساخت Lexer و Parser
    input_stream = FileStream(input_file)
    lexer = MiniCLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = MiniCParser(token_stream)
