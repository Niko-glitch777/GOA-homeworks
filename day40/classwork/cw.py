#1)
def basic_op(operator, value1, value2):
    if operator == "+":
        return value1 + value2
    elif operator == "-":
        return value1 - value2
    elif operator == "*":
        return value1 * value2
    elif operator == "/":
        return value1 / value2

#2)
def are_you_playing_banjo(name):
    if name.lower()[0] == "r":
        return f"{name} plays banjo"
    else:
        return f"{name} does not play banjo"

#3)
def count_positives_sum_negatives(arr):
    count_positives = 0
    sum_negatives = 0
    if arr == []:
        return []
    
    for i in arr:
        if i > 0:
            count_positives += 1
        else:
            sum_negatives += i
    return [count_positives,sum_negatives]

#4)
def minimum(arr):
    return min(arr)

def maximum(arr):
    return max(arr)



#5)
def reverse_seq(n):
    l = []
    for i in range(n,0,-1):
        l.append(i)
    return l