# l = list() # []
# l.append(10)
# l.append(-3)
# l.append(25)
# # l.append('kjhsdfgyhu')
# # l.append([1, 2, 3, 4])
# # print(l[0]) #поэлементно выводить
# l.sort()
# l.reverse()
# print(l.pop())
# print(l)

# t = tuple([10, -3, 5])

# print(t.count(-1))


# t =('s', )
# print(type(t))


# l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
# s = 'hello'

# print('hell' in s)


# print(hash('abcdef'))
# print(hash('abcdee'))


d = dict(a=12345, b=87654) # d = {
#     'a': 1234,
#     'b': 5678,
# }
# d.update({'c': 9939339})
# # new_list = list(d.values())
# # new_list.reverse()
# # print(new_list)   #items все пары ключ-значение
# print(d.get('g', 'No value')) #доп.проверка,если выдается ошибка,программа дольше не иден.А если 'None',то можно работать
# s = {1, 2, 3, 6, 5}


# print(s)
# print(2 in s)
# a = 3
# b = 3
# print(a is b )
# # print(id(321))


# l1 = [1, 2, 3, 4, 5, [1, 2, 3, 4]]
# l2 = l1.copy()  #[1, 2, 3, 4, 5]

# l2[-1].append(10)

# print(l1)
# print(l2)

# print(l1[-1] is l2[-1]) #сравнивается по месту в оперативной памяти
# print(l1 == l2) #сравнивается по значению


# if 10 > 11:
#     print('True')
# else:
#     print('False')


is_valid = True
# status = 'clean' if is_valid else 'not clean'
# print(status)
# print(int(is_valid))
# status = ('not clean', 'clean')[is_valid]
# print(status)

# func_output = 'Some output'
# msg = func_output or 'No output'
# print(msg)


# result = 1
# if result == 1:
#     print('Good result')
# elif result == 2:
#     print('Bad result')
# else:
#     print('Invalid result')


# i = 10
# while i > 0:
#     print(i)
#     i -=1


# for i in range(0, 14):
#     print(i)


for x in '1234567890':
    if x in ('gflgl'):
        break
    print(x)
else:
    print('не было break')
print('Конец цикла')