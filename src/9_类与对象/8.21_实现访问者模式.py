"""
8.21_实现访问者模式
"""
from pprint import pprint


class Node:
    pass


class UnaryOperator(Node):
    def __init__(self, operand):
        self.operand = operand


class BinaryOperator(Node):
    def __init__(self, left, right):
        self.left = left
        self.right = right


class Add(BinaryOperator):
    pass


class Sub(BinaryOperator):
    pass


class Mul(BinaryOperator):
    pass


class Div(BinaryOperator):
    pass


class Negate(UnaryOperator):
    pass


class Number(Node):
    def __init__(self, value):
        self.value = value


# Representation of 1 + 2 * (3 - 4) / 5
t1 = Sub(Number(3), Number(4))
t2 = Mul(Number(2), t1)
t3 = Div(t2, Number(5))
t4 = Add(Number(1), t3)


class NodeVisitor:
    def visit(self, node):
        method_name = 'visit_' + type(node).__name__.lower()
        method = getattr(self, method_name, None)
        if method is None:
            self.generate_node(node)
        return method(node)

    def generate_node(self, node):
        raise RuntimeError('No {} method'.format('visit_' + type(node).__name__.lower()))


class Evaluator(NodeVisitor):
    def visit_number(self, node):
        return node.value

    def visit_add(self, node):
        return self.visit(node.left) + self.visit(node.right)

    def visit_sub(self, node):
        return self.visit(node.left) - self.visit(node.right)

    def visit_mul(self, node):
        return self.visit(node.left) * self.visit(node.right)

    def visit_div(self, node):
        return self.visit(node.left) / self.visit(node.right)

    def visit_negate(self, node):
        return -node.operand


e = Evaluator()
print(e.visit(t4))


class StackCode(NodeVisitor):
    def generate_code(self, node):
        self.instructions = []
        self.visit(node)
        return self.instructions

    def visit_number(self, node):
        self.instructions.append(('PUSH', node.value))

    def binop(self, node, instruction):
        self.visit(node.left)
        self.visit(node.right)
        self.instructions.append((instruction,))

    def visit_add(self, node):
        self.binop(node, 'ADD')

    def visit_sub(self, node):
        self.binop(node, 'SUB')

    def visit_mul(self, node):
        self.binop(node, 'MUL')

    def visit_div(self, node):
        self.binop(node, 'DIV')

    def unaryop(self, node, instruction):
        self.visit(node.operand)
        self.instructions.append((instruction,))

s = StackCode()
pprint(s.generate_code(t4))
