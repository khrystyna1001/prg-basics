import queue
import math

natural_number = 18
stack = queue.LifoQueue()

for n in reversed(range(1, natural_number + 1)):
    if natural_number % n == 0:
        n = natural_number / n
        stack.put(0)
    elif natural_number % n == 1:
        n = natural_number / n
        n = math.floor(n)
        stack.put(1)

while not stack.empty():
    i = stack.get()
    print(i)