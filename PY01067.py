import queue
t = int(input())
while t > 0:
    n = int(input())
    q = queue.Queue()
    q.put("1")
    q.put("2")
    cnt = 0
    while q.qsize():
        a = q.get()
        b = a.count("2")
        if b > len(a) - b:
            print(a, end = " ")
            cnt += 1
            if cnt == n:
                break
        q.put(a + "0")
        q.put(a + '1')
        q.put(a + '2')
    print()
    t -= 1