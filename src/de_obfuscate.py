# clean.py
from antlr4 import FileStream, CommonTokenStream
from antlr_gen.MiniCLexer import MiniCLexer
from antlr_gen.MiniCParser import MiniCParser
from ast_builder import ASTBuilder
from de_obfuscator import Deobfuscator
from generator import generate_code
from src.cfg_builder import plot_cfg, CFGBuilder, CFGNode


def main():
    inp = "../test_input/input1.obfuscated1.mc"
    out = "../test_output/output1.cleaned1.mc"

    input_stream = FileStream(inp, encoding="utf-8")
    lexer = MiniCLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = MiniCParser(stream)

    tree = parser.program()
    print("Parse tree:", tree.toStringTree(recog=parser))

    builder = ASTBuilder()
    ast = builder.visit(tree)
    print("AST tree:", ast)

    de_obf = Deobfuscator()
    cleaned_ast = de_obf.apply(ast)

    cfg_builder = CFGBuilder()
    entry, exit_node = cfg_builder.build(cleaned_ast)
    plot_cfg(entry)


    code = generate_code(cleaned_ast)

    with open(out, "w", encoding="utf-8") as f:
        f.write(code)

    print("Done. Cleaned code written to:", out)


if __name__ == "__main__":
    main()
