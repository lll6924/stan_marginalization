from lexer import Lexer
from parser import Parser
from printer import printer
def main():
    with open("8schools.stan") as f:
        data = f.read()
    lexer = Lexer()
    lexer.build()
    parser = Parser()
    parser.build()
    ast = parser.parse(data)
    blocks = {block.name : block for block in ast.list}
    ys = []
    xs = []
    codes = []
    if 'data' in blocks.keys():
        ys = blocks['data'].statements
    if 'parameters' in blocks.keys():
        xs = blocks['parameters'].statements
    if 'model' in blocks.keys():
        codes = blocks['model'].statements
    printer(xs=xs, ys=ys, codes=codes, filename='8schools_reprint.stan')

if __name__ == '__main__':
    main()