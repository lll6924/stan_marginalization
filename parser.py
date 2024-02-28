import ply.yacc as yacc
import ply.lex as lex
from lexer import Lexer
from nodes import *

class Parser:
    tokens = Lexer.tokens

    def build(self, **kwargs):
        self.parser = yacc.yacc(module=self, **kwargs)

    start = 'block_list'

    def p_number(self, p):
        '''
            number : INTEGER
                    | FLOAT
        '''
        p[0] = p[1]

    def p_expression(self, p):
        '''
            expression : number
                        | ID
        '''
        p[0] = Expression()
        if isinstance(p[1], str):
            p[0].variable = p[1]
        else:
            p[0].number = p[1]

    def p_expression_list(self, p):
        '''
            expression_list : expression_list ',' expression
                            | expression
        '''
        if isinstance(p[1], Expression):
            p[0] = ExpressionList([p[1]])
        else:
            l = p[1].expressions
            l.append(p[3])
            p[0] =  ExpressionList(l)

    def p_arraydef(self, p):
        '''
            arraydef : '[' expression ']'
                    | empty
        '''
        if p[1] is None:
            p[0] = None
        else:
            p[0] = p[2]

    def p_lower(self, p):
        '''
            lower : '<' LOWER '=' number '>'
                    | empty
        '''
        if p[0] is None:
            p[0] = None
        else:
            p[0] = p[4]

    def p_type(self, p):
        '''
            type : INT  lower arraydef
                | REAL  lower arraydef
                | VECTOR  lower arraydef
        '''
        p[0] = Type(p[1], p[2], p[3])

    def p_statement(self, p):
        '''
            statement : type ID ';'
                      | ID '~' ID '(' expression_list ')' ';'
        '''
        p[0] = Statement()

        if isinstance(p[1], Type):
            p[0].type = p[1]
            p[0].variable = p[2]
        else:
            p[0].variable = p[1]
            p[0].distribution = p[3]
            p[0].expression_list = p[5]

    def p_statement_list(self, p):
        '''
            statement_list : statement_list statement
                            | statement
        '''
        if isinstance(p[1], Statement):
            p[0] = StatementList([p[1]])
        else:
            l = p[1].statements
            l.append(p[2])
            p[0] = StatementList(l)


    def p_block(self, p):
        '''
            block : ID '{' statement_list '}'
        '''
        p[0] = Block(p[1], p[3])

    def p_block_list(self, p):
        '''
            block_list : block_list block
                        | block
        '''
        if isinstance(p[1], Block):
            p[0] = BlockList([p[1]])
        else:
            l = p[1].list
            l.append(p[2])
            p[0] = BlockList(l)


    def p_empty(self, p):
        'empty :'
        p[0] = None

    def parse(self, data):
         return self.parser.parse(data)
    def test(self, data):
        lexer = Lexer()
        lexer.build()
        result = self.parser.parse(data)
        print(result)

if __name__ == '__main__':
    with open("8schools.stan") as f:
        data = f.read()
    parser = Parser()
    parser.build()
    parser.test(data)
