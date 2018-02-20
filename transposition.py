from math import ceil
usr = input("Message to encrypt: ")
key = int(input("Key: "))
usrls = list(usr)
print(usrls)
print(len(usr))
rows = ceil(len(usr)/key)
print(rows)
bigls = []
newls = []
done = 0
while len(bigls) < rows:
    for char in usrls:
        for i in range(done,key):
            print(i)
            newls.append(usrls[i])
            done += 1
        bigls.append(newls)
for i in bigls:
    print(i)
