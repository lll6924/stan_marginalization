from nodes import *

def printer(ys, xs, codes, filename):
    with open(filename, 'w') as f:
        print('data {', file=f)
        for y in ys.statements:
            st = y.type.type
            if y.type.lower is not None:
                st += '<lower={}>'.format(y.type.lower)
            if y.type.arraydef is not None:
                st += '[{}]'.format(y.type.arraydef.val)
            print(st, y.variable + ';', file=f)
        print('}', file=f)

        print('parameters {', file=f)
        for x in xs.statements:
            st = x.type.type
            if x.type.lower is not None:
                st += '<lower={}>'.format(x.type.lower)
            if x.type.arraydef is not None:
                st += '[{}]'.format(x.type.arraydef.val)
            print(st, x.variable + ';', file=f)
        print('}', file=f)

        print('model {', file=f)
        for line in codes.statements:
            exprs = ','.join([str(e.val) for e in line.expression_list.expressions])
            print(line.variable, '~', line.distribution,'(' + exprs + ');', file=f)
        print('}', file=f)
