class BlockList:
    def __init__(self, list):
        self.list = list

class Block:
    def __init__(self, name, statements):
        self.name = name
        self.statements = statements

class StatementList:
    def __init__(self, statements):
        self.statements = statements

class Statement:
    type = None
    variable = None
    distribution = None
    expression_list = None


class ExpressionList:
    def __init__(self, expressions):
        self.expressions = expressions

class Expression:
    number = None
    variable = None

    @property
    def val(self):
        if self.number is None:
            return str(self.variable)
        return str(self.number)

class Type:
    def __init__(self, type, lower, arraydef):
        self.type = type
        self.arraydef = arraydef
        self.lower = lower
