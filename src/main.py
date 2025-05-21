from antlr4 import FileStream, CommonTokenStream
from antlr_gen.MiniCLexer import MiniCLexer
from antlr_gen.MiniCParserParser import  MiniCParserParser
from ast_builder import ASTBuilder
from obfuscator import Obfuscator
from generator import generate_code

def main():
    input_path = "test_input/input.mc"
    output_path = "test_output/output.mc"

    input_stream = FileStream(input_path, encoding='utf-8')
    lexer = MiniCLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = MiniCParserParser(stream)

    tree = parser.program()
    builder = ASTBuilder()
    ast = builder.visit(tree)

    obf = Obfuscator()
    obfuscated_ast = obf.apply(ast)

    code = generate_code(obfuscated_ast)

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(code)

if __name__ == "__main__":
    main()
