li = [1, 2, 3, 4, 5, 6]

for i in li:                #inverterer alle oddetall
    if i%2:
        li[i-1] *= -1
print(li)
print(sorted(li, reverse=True))  #Reverserer listen
