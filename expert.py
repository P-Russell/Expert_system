IF_AND_ONLY_IF = "if_and_only_if"
IMPLIES = "implies"

import algebra

def shunt_yard(string):
    new_str = ''
    if ('=>' in string):
        str_arr = string.split('=>')
        return new_str + shunt_yard(str_arr[0]) + shunt_yard(str_arr[1]) + ' =>'
    elif ('+' in string):
        str_arr = string.split('+')
        return new_str + shunt_yard(str_arr[0]) + shunt_yard(str_arr[1]) + ' +'
    elif ('|' in string):
        str_arr = string.split('|')
        return new_str + shunt_yard(str_arr[0]) + shunt_yard(str_arr[1]) + ' |'
    elif ('^' in string):
        str_arr = string.split('^')
        return new_str + shunt_yard(str_arr[0]) + shunt_yard(str_arr[1]) + ' ^'
    elif ('!' in string):
        str_arr = string.split('!')
        return new_str + shunt_yard(str_arr[1]) + ' !'
    return string

class Rule:
    types = {
        "<=>": IF_AND_ONLY_IF,
        "=>": IMPLIES
    }

    def __init__(self, left, right, type):
        self.left = left
        self.right = right
        self.type = type
    
    @classmethod
    def from_string(cls, string, rules):
        out = Rule(None, None, None)

        # do shunting yard here
        string = shunt_yard(string)
        stack = []
        for token in string.split(): # replace with intelligent tokenisation
            if token in algebra.operators:
                amount = 1 if algebra.operators[token].unary else 2
                operands = [stack.pop(-1) for i in range(amount)][::-1]
                stack.append(algebra.operators[token](*operands, appeared_as=token))
            else:
                stack.append(rules[token])
        
        rule = stack[0]
        out.type = Rule.types[rule.appeared_as]
        out.left = rule.left
        out.right = rule.right
        return out

class Fact:
    def __init__(self, status=False, confirmed=False):
        self.status = status
        self.confirmed = confirmed

class FactCollection:
    @classmethod
    def from_file(cls, file):
        collection = cls()
        for line in file:
            line = line.strip()

            # comments
            if not line.split("#")[0]:
                pass

            # initial true facts
            elif line.startswith("="):
                line = line[1:]
                line = line.split("#")[0].strip()
                for fact in line:
                    collection.facts[fact] = Fact(True, True)
            
            # queries
            elif line.startswith("?"):
                line = line[1:]
                line = line.split("#")[0].strip()
                collection.queries = list(line)

            # rules
            else:
                line = line.split("#")[0].strip()
                collection.rules.append(Rule.from_string(line, collection))

        return (collection)

    def __init__(self, rules=[], facts={}, queries=[]):
        self.facts = facts
        self.rules = rules
        self.queries = queries

    def truth_check(self, letter):
        if (letter in self.facts and self.facts[letter].status == True):
            return True
        else:
            for rule in self.rules:
                if rule.right.contains(letter):
                    try:
                        if rule.right.reaches(letter, rule.left.eval()) == True:
                            return True
                    except:
                        if rule.left.eval() == True:
                            return True
        return False

    def __getitem__(self, fact):
        if fact not in self.facts:
            self.facts[fact] = Fact()
        return algebra.Fact(self, fact)

    def __setitem__(self, rule, value):
        self.facts[fact] = value