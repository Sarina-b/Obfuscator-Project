grammar MiniCParser;

options {
    tokenVocab=MiniCLexer;
}

program         : (structDecl | declaration | functionDef)* EOF ;

// ---- Struct Definition ----
structDecl      : 'struct' ID '{' structMember* '}' ';' ;
structMember    : type declarator ';' ;

// ---- Variable and Function Declarations ----
declaration     : type declarator ('=' expression)? ';' ;
functionDef     : type ID '(' parameters? ')' block ;
parameters      : parameter (',' parameter)* ;
parameter       : type declarator ;

// ---- Statements ----
block           : '{' statement* '}' ;

statement
    : block
    | declaration
    | expressionStatement
    | ifStatement
    | whileStatement
    | forStatement
    | returnStatement
    | ioStatement
    ;

expressionStatement : expression? ';' ;

ifStatement     : 'if' '(' expression ')' statement ('else' statement)? ;
whileStatement  : 'while' '(' expression ')' statement ;
forStatement    : 'for' '(' expression? ';' expression? ';' expression? ')' statement ;
returnStatement : 'return' expression? ';' ;

ioStatement     : ('printf' | 'scanf') '(' STRING_LITERAL (',' expression)* ')' ';' ;

// ---- Expressions ----
expression      : assignment ;
assignment      : logicOr ('=' assignment)? ;
logicOr         : logicAnd ('||' logicAnd)* ;
logicAnd        : equality ('&&' equality)* ;
equality        : relational (('==' | '!=') relational)* ;
relational      : additive (('<' | '>' | '<=' | '>=') additive)* ;
additive        : multiplicative (('+' | '-') multiplicative)* ;
multiplicative  : unary (('*' | '/') unary)* ;

unary           : ('!' | '-' | '*' | '&')? postfix ;
postfix         : primary ('.' ID)* ;

primary
    : INT_LITERAL
    | CHAR_LITERAL
    | BOOL_LITERAL
    | ID
    | '(' expression ')'
    ;

// ---- Types ----
type            : ('int' | 'char' | 'bool' | structType) pointer* ;
pointer         : '*' ;
structType      : 'struct' ID ;
declarator      : pointer* ID ;
