# A = (13, 5, 43, 49, 67, 32, 12, 98, 6, 10, 34, 20, 55, 68, 14, 60, 14)
# B = (53, 21, 4, 23, 76, 3, 43, 12, 54, 342, 21)
# Необходимо определить:
# 1) Сумма элементов какого из кортежей больше и вывести соответствующее
# сообщение на экран ( Сумма больше в кортеже - ..)
# 2) Вывести на экран порядковые номера минимальных элементов этих кортежей

A = (13, 5, 43, 49, 67, 32, 12, 98, 6, 10, 34, 20, 55, 68, 14, 60, 14)
B = (53, 21, 4, 23, 76, 3, 43, 12, 54, 342, 21)

if sum(A) > sum(B):
    print("Сумма больше в кортеже - A")
else:
    print("Сумма больше в кортеже - B")
print("min в A:", min(A), "Порядковый номер: ", A.index(min(A)))
print("min в B:", min(B), "Порядковый номер: ", B.index(min(B)))
