# while there are tokens to be read:
# 	read a token.
# 	if the token is a number, then push it to the output queue.
# 	if the token is an operator, then:
# 		while (there is an operator at the top of the operator stack with
# 			greater precedence) or (the operator at the top of the operator stack has
#                         equal precedence and
#                         the operator is left associative) and
#                       (the operator at the top of the stack is not a left bracket):
# 				pop operators from the operator stack, onto the output queue.
# 		push the read operator onto the operator stack.
# 	if the token is a left bracket (i.e. "("), then:
# 		push it onto the operator stack.
# 	if the token is a right bracket (i.e. ")"), then:
# 		while the operator at the top of the operator stack is not a left bracket:
# 			pop operators from the operator stack onto the output queue.
# 		pop the left bracket from the stack.
# 		/* if the stack runs out without finding a left bracket, then there are
# 		mismatched parentheses. */
# if there are no more tokens to read:
# 	while there are still operator tokens on the stack:
# 		/* if the operator token on the top of the stack is a bracket, then
# 		there are mismatched parentheses. */
# 		pop the operator onto the output queue.
# exit.

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



