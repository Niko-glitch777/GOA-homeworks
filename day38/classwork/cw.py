


#1)

#tuple - არის საცავი რაც ინახავს ერთს ან მეტ მნიშვნელობას და ის list ისგან განსხვავდება იმით რომ 
# ის არის immutable

# 2)

names = ("Luka","Lasha","Dato","Vitali","Badri")  
                                                            # <--ამ კოდში გამოვიყენე negative index 
                                                            # რომ რამდენი ელემენტიც არ უნდა იყოს
                                                            # მაინ დაგვიბრუნებს პირველი და ბოლო ელემნტის გარეშე ყველა ელემენტს
print(names[1:-1])


# 3)
# tuple methods - count() - გვიბრუნებს ფრჩხილებში გადაცემული მნიშვნელობა რამდენჯერ არის 
#                           გამეორებული tuple ში

#                 index() - გვიბრუნებს მასზე გადაცემული მნიშვნელობა რომელ ინდექსზეა tuple ში

# 5)

#unpacking - ის დახმარებით შეგვიძლია tuple - იდან გადმოვიტანოთ ელემენტები ცალცალკე ცვლადებში ან რამოდენიმე ელემენტი 1 ცვლაში

names1 = ["admingegechkori","NikaComia","tyupibadrijani"]
name1,name2,name3 = names1 



nums = [1,2,3,4,5,6,7]

num1, num2, num3,num4 ,*num = nums



i = ["i1","i2","i3","i4","i5"]

ii1,ii2,ii3,ii4,ii5 = i


nums2 = [11,12,13,14,15]

nums1,nums3,nums5,nums7,nums9 = nums2

names6 = ["Luka","datomod","Kaibiwidaviti"]

name4,*names7 = names6