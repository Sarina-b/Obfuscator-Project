# main.py
import sys
from antlr4 import FileStream, CommonTokenStream
from MiniCLexer import MiniCLexer
from MiniCParser import MiniCParser
from ast_builder import AstBuilder # Your AST builder class
from obfuscator import Obfuscator    # Your Obfuscator class
from generator import CodeGenerator  # Your Code Generator class

def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py input.mc")
        return

    input_file = sys.argv[1]
    output_file = "output.mc"

    try:
        # 1. Read input file
        input_stream = FileStream(input_file)

        # 2. Lexer
        lexer = MiniCLexer(input_stream)
        token_stream = CommonTokenStream(lexer)

        # 3. Parser
        parser = MiniCParser(token_stream)
        parse_tree = parser.program()  # 'program' is your entry rule in MiniC.g4

        # 4. AST Building
        ast_builder_visitor = AstBuilder()
        ast = ast_builder_visitor.visit(parse_tree)
        print("--- Original AST (Conceptual) ---")
        # You might want a way to print/debug your AST here
        # print(ast)

        # 5. Obfuscation
        obfuscator_instance = Obfuscator(ast)
        obfuscated_ast = obfuscator_instance.obfuscate()
        print("--- Obfuscated AST (Conceptual) ---")
        # print(obfuscated_ast)

        # 6. Code Generation
        code_gen = CodeGenerator()
        obfuscated_code = code_gen.generate(obfuscated_ast)
        print(f"\n--- Obfuscated Code ({output_file}) ---")
        print(obfuscated_code)

        # 7. Write to output file
        with open(output_file, 'w') as f:
            f.write(obfuscated_code)
        print(f"\nSuccessfully obfuscated '{input_file}' to '{output_file}'")

    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == '__main__':
    main()