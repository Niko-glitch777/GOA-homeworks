#1)მომხმარებელს შემოატანინეთ მისი ასაკი# და გაიგეთ 
#რამდენჯერ მოთავსდება რიცხვი 10 მასში

user_age = int(input('Enter your age: '))
age = user_age // 10
print(age)



#2)მომხმარებელს შემოატანინეთ მისი სახელი და გაიგეთ უდრის 
#თუ არა ის თქვენს სახელს

user_name ='Niko'
name = str(input('Enter your name: '))
print(user_name == name)



#3)მომხმარებელს შემოატანინეთ ორი რიცხვი (num1 და num2) და 
#გაიგეთ რა იქნება ნაშთი, პირველი რიცხვის მეორეზე გაყოფის შემდეგ

num1 = int(input('Enter first number: '))
num2 = int(input('Enter second number: '))
print(num1 % num2)



#4)მომხმარებელს შემოატანინეთ მისი ასაკი და გაიგეთ არის თუ 
# არა ის ლუწი (იყოფა თუ არა ზუსტად 2ზე) ანუ 
# გვრჩება თუ არა ნაშთი ნული, ორზე გაყოფის შედეგად


age1 = int(input('Enter your age: '))
print(age1 % 2)