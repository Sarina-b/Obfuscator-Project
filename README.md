



# 🛡️ Mini-C Code Obfuscator

This project is a static code obfuscator for a C-like language called **Mini-C**. It parses a valid `.mc` program and produces an **obfuscated**, functionally equivalent version. The purpose is to protect code from reverse engineering while preserving its original behavior.

---

## 🚀 How to Run the Project

### 1. Install dependencies (requires Python 3.6+ and ANTLR 4):
```bash
pip install antlr4-python3-runtime
````

### 2. Generate the parser with ANTLR:

```bash
antlr4 -Dlanguage=Python3 MiniCLexer.g4
antlr4 -Dlanguage=Python3 MiniCParser.g4
```

> Alternatively, use the provided generated parser files in the `antlr_gen/` folder.

### 3. Run the obfuscator on an input file:

```bash
python main.py test_input.mc
```

The obfuscated output will be written to `output.mc`.

---

## 🔧 Obfuscation Techniques Implemented

The following transformations are applied to the original Mini-C code:

1. **Identifier Renaming**
   All variable and function names are replaced with meaningless random strings (e.g., `sum → fxz`, `x → a39`).

2. **Dead Code Insertion**
   Unused variables and operations are added to blocks to make the logic noisier.

3. **Expression Rewriting**
   Simple expressions are replaced with mathematically equivalent but more complex forms.
   *Example:* `a + b → a - (-b)`

4. **Control Flow Flattening**
   Sequential logic is replaced with `while + switch` structures to obscure the execution order.

---

## ✅ Functional Equivalence Testing

To ensure the output behaves exactly like the input:

* Both versions (`input.mc` and `output.mc`) are executed and compared manually using I/O inspection.
* The transformations do **not** alter the logic of the code — they only modify the syntax/structure.
* All inserted code (e.g., dead variables) is guaranteed to have **no side effects**.

---

## 🧰 Tools & Technologies Used

* **Python 3.10+** – core implementation
* **ANTLR 4.13.1** – for parsing and generating AST
* **Mini-C Grammar** – defined via `.g4` files
* **Custom AST Builder** – for easy tree traversal and rewriting
* **Manual Testing** – functional validation of transformation results

---

## 📂 Project Structure

```
Obfuscator-Project/
├── antlr_gen/               # ANTLR-generated parser classes
│   ├── MiniCLexer.py
│   ├── MiniCListener.py
│   ├── MiniCParser.py
│   └── MiniCVisitor.py
├── grammers/
│   └── MiniC.g4             # Grammar file
├── src/
│   ├── ast_builder.py       # AST construction
│   ├── cfg_builder.py       # CFG construction
│   ├── de_obfuscate.py      # De-obfuscation script
│   ├── generator.py         # Code generator from AST
│   ├── main.py              # Entry point
│   └── obfuscator.py        # Obfuscation logic
├── test_input/
│   ├── input.mc             # Sample input file
│   ├── input.obfuscated.mc  # Obfuscated version
│   ├── input1.mc
│   └── input1.obfuscated1.mc
├── test_output/
│   └── output.mc            # Generated output
├── .gitignore
├── Dockerfile
├── README.md
└── Report-Phase1.pdf
```

---

## 👨‍💻 Authors
Fatemeh Amirabadi - Sarina Babadi - Mobina Davoodi 

---


