import re


def is_valid_rule(line):

    pattern = r'[^A-Z" "/+/|/^/!/=/</>/(/)]'
    if re.search(pattern, line):
        print("Invalid characters in line: ", line)
        return False

    if "=>" in line:
        tmp = line.split("=>")
    elif "<=>" in line:
        tmp = line.split("<=>")
    if len(tmp) != 2:
        print("Invalid syntax in line ", line)
        return False

    spl = line.split(' ')
    operators = ['+', '|', '^', "=>", "<=>"]
    op_found = False
    fact_found = False
    for e in spl:
        if e in operators and op_found:
            print("Syntax error in line ", line, " double operator found ", e)
            return False
        elif e in operators and not op_found:
            op_found = True
            fact_found = False

        if e not in operators and fact_found:
            print("Syntax error in line ", line, " double fact found ", e)
            return False
        elif e not in operators and not fact_found:
            fact_found = True
            op_found = False

        length = len(e)
        if length == 2:
            if e == "=>" or (e[0] == '!' and e[1].isupper()) or \
                    (e[0] == '(' and e[1].isupper()) or (e[1] == ')' and e[0].isupper()):
                pass
            else:
                print("Syntax error in line ", line, " found unexpected characters ", e)
                return False
        if length > 2:
            if e != "<=>":
                print("Syntax error in line ", line, " found unexpected characters ", e)
                return False
    return True


def is_valid_query(line):
    pattern = r'[^A-Z/?]'
    if re.search(pattern, line):
        print("Invalid characters in line: ", line)
        return False
    return True


def is_valid_facts(line):
    pattern = r'[^A-Z/=]'
    if re.search(pattern, line):
        print("Invalid characters in line: ", line)
        return False
    return True


def valid_syntax(fd):

    errors = 0
    facts = False
    queries = False
    rules = False

    for line in fd:
        line = line.split("#")[0].strip()

        if not line:
            pass

        elif "=>" in line or "<=>" in line:
            rules = True
            if not is_valid_rule(line):
                errors += 1

        elif line[0] == '=':
            if is_valid_facts(line):
                if not facts:
                    facts = True
                else:
                    print("Invalid line: ", line, " Facts all ready found")
                    errors += 1
            else:
                errors += 1

        elif line[0] == '?':
            if is_valid_query(line):
                if not queries:
                    queries = True
                else:
                    print("Invalid line: ", line, " Queries all ready found")
                    errors += 1
            else:
                errors += 1

        else:
            print('invalid line: ', line)
            errors += 1
    fd.seek(0)
    if not facts:
        print('No facts in file')
        return False
    if not queries:
        print('No queries in file')
        return False
    if not rules:
        print('No rules in file')

    if not errors:
        return True
