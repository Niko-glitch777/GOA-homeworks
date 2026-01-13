

#1)დაასრულეთ საშინაო დავალება


#2)
def get_count(sentence):
    count = 0
    v = "aeiou"
    for i in sentence:
        if i in v:
            count += 1
    return count


#3)
def filter_list(l):
    l2 = []                  
    for i in l:
        if type(i)== int:
            l2.append(i)
    return l2

#4) 
def solution(text, ending):         
    return text.endswith(ending)      

#5)
def century(year):
    sum = year // 100
    if year % 100 == 0:
        return sum
    else:
        return sum + 1
    

#6)
def friend(x):
    sum = []
    for i in x:
        if len(i) == 4:
            sum.append(i)
    return sum


#7)
def grow(arr):
    sum = 1
    for i in arr:
        sum = sum * i
    return sum


#8)
def goals(laLiga, copaDelRey, championsLeague):
    return laLiga + copaDelRey + championsLeague

