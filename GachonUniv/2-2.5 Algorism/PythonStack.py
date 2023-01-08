
def push(stack, element):
	stack.append(element)
	return stack

def peek(stack):
	if len(stack) != 0:
		return stack[-1]


def pop(stack):
	if len(stack) != 0:
		return stack.pop(-1)


stack = []

push(stack, "Apple")
push(stack, "Banana")
push(stack, "Cinamon")

print(pop(stack))
print(peek(stack))
print(stack)

