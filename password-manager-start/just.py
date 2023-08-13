# def GCD(m, n):
#
#     listt = [ i for i in range(1, min(m,n)+1) if m % i == 0 and n % i == 0]
#     print(listt[-1])
#
# GCD(96,40)
#
# # GCD without list
#
# def GCD_L(m,n):
#     for i in range(1,min(m,n)+1):
#         if m % i == 0 and n % i == 0:
#             fcd = i
#     print(fcd)
#
# GCD_L(96, 40)
#
# def GCD_h(m,n):
#     i = min(m, n)
#     while i > 0:
#         if m % i == 0 and n % i ==0:
#             return i
#         else:
#             i = i-1
#
# print(GCD_h(12,13))

a = [1,2,3]
b =[4,5,6]
new_a = [str(num) for num in a]
new_b=[str(num) for num in b]
m=int("".join(new_a))+ int("".join(new_b))
k = [ num for num in str(m)]
print(k)