from AbstractDataTypes import Queue, Stack

OPERATORS = {"+": 1, "-": 1, "*": 2, "/": 2, "%": 2, "**": 3}
OPEN_PARENTHESIS = "("
CLOSE_PARENTHESIS = ")"

def to_postfix(infix):
	infix = Queue(infix.strip().split())
	stack = Stack()
	postfix = str()

	while infix.size != 0:
		char = infix.dequeue()
		if char.isalpha() or char.isnumeric():
			postfix += char
			postfix += " "
		elif char == OPEN_PARENTHESIS:
			stack.push(char)
		elif char == CLOSE_PARENTHESIS:
			while stack.peek() != OPEN_PARENTHESIS:
				postfix += stack.pop()
				postfix += " "
			stack.pop()
		else:
			while stack.size > 0 and stack.peek() != OPEN_PARENTHESIS and OPERATORS[stack.peek()] >= OPERATORS[char]:
				postfix += stack.pop()
				postfix += " "
			stack.push(char)

		if infix.size == 0 and stack.size > 0:
			while stack.size != 0:
				postfix += stack.pop()
				postfix += " "

	if evaluate:
		return postfix

	return postfix[:-1]

def evaluate(postfix, variables={}):
	stack = Stack()
	postfix = Queue(postfix.strip().split())

	while postfix.size != 0:
		char = postfix.dequeue()
		if char.isalpha() or char.isnumeric():
			stack.push(eval(char, variables, locals()))
		else:
			operand_1 = stack.pop()
			operand_2 = stack.pop()
			answer = eval(f"operand_2 {char} operand_1", variables, locals())
			stack.push(answer)
	return stack.pop()
