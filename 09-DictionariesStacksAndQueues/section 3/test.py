import queue

cards = queue.LifoQueue()

cards.put('King of Hearts \u2665')    
cards.put('Queen of Diamonds \u2666')  
cards.put('Jack of Spades \u2660')     

print('Number of stack elements:', cards.qsize())

while not cards.empty():
    card = cards.get()
    print(card)

cards.put(2)
cards.put(3)
cards.put(7)
cards.put(4)
cards.put(1)
cards.put(9)
cards.put(8)

if cards.qsize() >= 2:
    first = cards.get()
    last = cards.get()
    sum = first + last

total = 0
while not cards.empty():
    total += cards.get()

print(sum)
print(total)