def enqueue(st_insert, x):
    st_insert.append(x)


def dequeue(st_insert, st_delete):
    if st_delete:
        return st_delete.pop()
    else:
        while st_insert:
            st_delete.append(st_insert.pop())
        return st_delete.pop() if st_delete else None


def front(st_insert, st_delete):
    if st_delete:
        return st_delete[-1]
    else:
        while st_insert:
            st_delete.append(st_insert.pop())
        return st_delete[-1] if st_delete else None


n = int(input())

st_insert = []
st_delete = []

for _ in range(n):
    query = input().split()
    if query[0] == '1':
        x = int(query[1])
        enqueue(st_insert, x)
    elif query[0] == '2':
        dequeue(st_insert, st_delete)
    elif query[0] == '3':
        print(front(st_insert, st_delete))
