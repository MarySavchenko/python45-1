elements = [1, 2, 7, 10, 14, 77, 5, 49]

# i = 0

# for x in elements:  #for i in range(len(elements)):
#     if x % 7 ==0:   #if elements[i] % ==0:
#         print(i, x) #print(i, elemrnts[i])
#         i += 1
for i, x in enumerate(elements):
    if x % 7 == 0:
        print(i, x)