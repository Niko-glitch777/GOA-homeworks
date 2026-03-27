# Create Phone Number
# def create_phone_number(n):
#     st = "(xxx) xxx-xxxx"
#     res = ""
#     for i in range(len(n)):
        
#         if len(st) == len(res):
#             break
        
#         for x in range(len(st)):
#             if (st[x] == "x"):
#                 res += st[x].replace("x",str(n[i]))
#                 i+=1
#             else:
#                 res+= st[x]
#     return res


# Who likes it?

# if names == []:
#         return "no one likes this"
#     elif len(names) == 1:
#         return f"{names[0]} likes this"
#     elif len(names) == 2:
#         return f"{names[0]} and {names[1]} like this"
#     elif len(names) == 3:
#         return f"{names[0]}, {names[1]} and {names[2]} like this"
#     else:
#         return f"{names[0]}, {names[1]} and {len(names) - 2 } others like this"