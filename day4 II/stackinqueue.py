from queue import LifoQueue
n=LifoQueue(maxsize=3)
print(n.qsize())
n.put("a")
n.put("b")
n.put("c")
print(n.full())
print(n.qsize())
print(n.get())
print(n.get())
print(n.get())

print(n.empty())
