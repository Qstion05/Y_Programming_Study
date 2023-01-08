def push(queue, element):
	queue.append(element)
	return queue

def peek(queue):
	return queue[0]

def pop(queue):
	return queue.pop(0)


queue = []

push(queue, "Apple")
push(queue, "Banana")
push(queue, "Cinamon")

print(pop(queue))
print(peek(queue))
print(queue)

