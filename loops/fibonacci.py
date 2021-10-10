
print(" fibonacci sayisini bulmaya hosgeldiniz "
      " 20 adet fibonacci uretecegiz")

a = int(1)
b = int(1)

fibonacci = [a,b]
for i in range(20):
      a,b = b,a+b
      fibonacci.append(b)
print(fibonacci)

