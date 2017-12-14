# 1.  While there are tokens to be read:
# 2.        Read a token
# 3.        If it's a number add it to queue
# 4.        If it's an operator
# 5.               While there's an operator on the top of the stack with greater precedence:
# 6.                       Pop operators from the stack onto the output queue
# 7.               Push the current operator onto the stack
# 8.        If it's a left bracket push it onto the stack
# 9.        If it's a right bracket
# 10.            While there's not a left bracket at the top of the stack:
# 11.                     Pop operators from the stack onto the output queue.
# 12.             Pop the left bracket from the stack and discard it
# 13. While there's operators on the stack, pop them to the queue

# The following symbols are defined, in order of decreasing priority:
# • ( and ) which are fairly obvious. Example : A + (B | C) => D
# • ! which means NOT. Example : !B
# • + which means AND. Example : A + B
# • | which means OR. Example : A | B
# • ˆ which means XOR. Example : A ˆ B
# • => which means "implies". Example : A + B => C
# • <=> which means "if and only if". Example : A + B <=> C


def in_to_postfix(line):
    postfix = ''
    op_stack = []
    line = line.split('=>')
    operators = ['!', '+', '|', "^"]
    for sides in line:
        for e in sides:
            if e != ' ':
                # 	if the token is a number, then push it to the output queue.
                if e[0].isupper():
                    postfix += e + ' '
                # if the token is an operator, then:
                # while (there is an operator at the top of the operator stack with
                # 			greater precedence) or (the operator at the top of the operator stack has
                #                         equal precedence and
                #                         the operator is left associative) and
                #                       (the operator at the top of the stack is not a left bracket):
                elif e in operators:
                    while




                if e[0] == '!':
                    if op_stack:
                        while (operators.index('!') < operators.index(op_stack[-1])):

                    op_stack.append('!')
                    postfix += e[1] + ' '

                elif e in operators:
                    while (operators.index(e) < operators.index(op_stack[-1]))



