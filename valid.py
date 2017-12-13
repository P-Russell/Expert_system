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
    for e in spl:
        length = len(e)
        if length == 2:
            if e != "=>":
                print("Syntax error in line ", line, " found unexpected characters ", e)
                return False
            elif e[0] != '!' and not e[1].isupper:
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
            if is_valid_rule(line):
                rules = True
            else:
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
