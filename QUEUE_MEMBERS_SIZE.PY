#CREATE A QUEUE AND DISPLAY ALL MEMBERS AND SIZE OF QUEUE.
import queue
q = queue.Queue()
for x in range(4):
    q.put(x)
print("Members of the queue:")
y=z=q.qsize()

for n in list(q.queue):
    print(n, end=" ")
print("\nSize of the queue:")
print(q.qsize())
'''
Members of the queue:                                                                                         
0 1 2 3                                                                                                       
Size of the queue:                                                                                            
4 
'''
