import ply.lex as lex

class Lexer:
    reserved = {
        'int' : 'INT',
        'lower' : 'LOWER',
        'vector' : 'VECTOR',
        'real' : 'REAL',
    }

    tokens = [
        'INTEGER',
        'FLOAT',
        'ID',
    ] + list(reserved.values())

    def t_ID(self, t):
        r'[a-zA-Z_][a-zA-Z_0-9]*'
        t.type = self.reserved.get(t.value,'ID')    # Check for reserved words
        return t

    def t_FLOAT(self, t):
        r'([0-9]*[.])[0-9]+'
        t.value = float(t.value)
        return t

    def t_INTEGER(self, t):
        r'\d+'
        t.value = int(t.value)
        return t

    def t_newline(self, t):
        r'\n+'
        t.lexer.lineno += len(t.value)

    t_ignore  = ' \t'

    literals = "+-*/{}();,~[]<>="

    def t_error(self, t):
        print("Illegal character '%s'" % t.value[0])
        t.lexer.skip(1)

    def build(self, **kwargs):
        self.lexer = lex.lex(module=self, **kwargs)

    def test(self, data):
        self.lexer.input(data)
        while True:
            tok = self.lexer.token()
            if not tok:
                break
            print(tok)


if __name__ == '__main__':
    with open("8schools.stan") as f:
        data = f.read()
    lexer = Lexer()
    lexer.build()
    lexer.test(data)
