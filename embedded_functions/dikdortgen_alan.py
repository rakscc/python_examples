
liste = [(3,4),(10,3),(5,6),(1,9)]

liste1 = []
liste2 = []

for i,j in liste:
    liste1.append(i)
    liste2.append(j)

print(list(map(lambda x, y: x * y, liste1, liste2)))
