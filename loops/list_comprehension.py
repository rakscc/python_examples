
print(" list comprehension metoduyla 1-100 arasindaki sayilardan cift sayilari cekilecek")

list = [*range(1,101)]
cift_list = []

for i in list:
    if ( i%2==0 ):
        cift_list.append(i)

print(cift_list)

