class Fact:
    def __init__(self, collection, name):
        self.name = name
        self.collection = collection

    def eval(self):
        status = self.collection.truth_check(self.name)
        return status

    def contains(self, fact):
        return self.name == fact

    def reaches(self, letter, status):
        if (self.name == letter):
            return status

    def __str__(self):
        return str(self.name)

class Operator:
    unary = False
    def __init__(self, left, right=None, appeared_as=None):
        self.left = left
        self.right = right
        self.appeared_as = appeared_as

    def contains(self, fact):
        if self.__class__.unary == True:
            return self.left.contains(fact)
        else:
            return self.left.contains(fact) or self.right.contains(fact)
    
    def __str__(self):
        if self.__class__.unary:
            return "{} {}".format(self.appeared_as, self.left)
        return "{} {} {}".format(self.left, self.appeared_as, self.right)

class And(Operator):
    def eval(self):
        return self.left.eval() and self.right.eval()
    
    def reaches(self, letter, status):
        return self.left.reaches(letter, status) or self.right.reaches(letter, status)

class Or(Operator):
    def eval(self):
        return self.left.eval() or self.right.eval()

    def reaches(self, letter, status):
        return self.left.reaches(letter, status) or self.right.reaches(letter, status)

class Not(Operator):
    unary = True
    def eval(self):
        return not self.left.eval()

class Xor(Operator):
    def eval(self):
        if self.left.eval() == False and self.right.eval() == False:
            return False
        else:
            return not self.left.eval() or not self.right.eval()

    def reaches(self, letter, status):
        return False #self.left.reaches(letter, status) or self.right.reaches(letter, status)

operators = {
    "+": And,
    "|": Or,
    "!": Not,
    "^": Xor,
    "=>": Operator,
    "<=>": Operator
}