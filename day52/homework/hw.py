


# 1.
# def get_sum(a,b):
#     sum = 0
#     if a == b: return a
#     elif a > b:
#         for i in range(b,a +1):
#             sum += i
#         return sum
#     elif b > a:
#         for i in range(a,b + 1):
#             sum += i
#         return sum

#2.
# def min_max(lst):
#   result = [min(lst),max(lst)]
#   return result


#3.
# def mxdiflg(a1, a2):
#     if not a1 or not a2:
#         return -1
#     max1 = max(len(i) for i in a1)
#     min1 = min(len(i) for i in a1)
#     max2 = max(len(i) for i in a2)
#     min2 = min(len(i) for i in a2)
#     return max(max1 - min2, max2 - min1)


#4.
# def nb_year(p0, percent, aug, p):
#     zero = 0
#     while p0 < p:
#         p0 += int(p0 * percent / 100) + aug
#         zero += 1
#     return zero


#5.
# def longest(al, az):
#     return "".join(sorted(set(al + az)))


#6.
# def get_count(sentence):
#     count = 0
#     vowels = "aeiou"
#     for i in sentence:
#         if i in vowels:
#             count += 1
#     return count




#7.
# def find_short(s):
#     x = s.split()
#     x.sort(key = len)
#     return len(x[0])


#8.
# def is_leap_year(year):
#     if year % 400 == 0:
#         return True
#     elif year %100 == 0:
#         return False
#     elif year % 4 == 0:
#         return True
#     else:
#         return False



#9.
# def odd_or_even(arr):
#     sum = 0 
#     for i in arr:
#         sum = sum + i
#     if sum % 2 == 0:
#         return "even"
#     else:
#         return "odd"


#10.
# def friend(x):
#     sum = []
#     for i in x:
#         if len(i) == 4:
#             sum.append(i)
#     return sum