class MathDojo(object):
    def __init__(self):
        self.result = 0
    def add(self, *args):
        for arg in args:
            self.result += arg
        return self
    def substract(self, *args):
        for arg in args:
            self.result -= arg
        return self

md = MathDojo()
print md.add(2).add(2,5).substract(3,2).result
