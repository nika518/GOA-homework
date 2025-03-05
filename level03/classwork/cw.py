#1)  მომხმარებელს შემოატანინეთ სამი რიცხვი და გამოიტანეთ ამ რიცხვების ჯამი

num1 = input("enter first number")
num2 = input("enter second number")
num3 = input("enter third number")
num4 = int(num1) + int(num2) + int(num3)
print(num4)


#2) შემოატანინეთ მომხმარებელს სახელი და შეინახეთ მისი სახელი ცვლადში

First_name = input("your name: ")
last_name = input("your last name: ")
user = (First_name + " " +  last_name)
print(user)

#3) შემოიტანინეთ მომხმარელს ორი რიცხვი, თუ პირველი რიცხვი მეტია მეორეზე გამოიტანეთ True ( boolean ) თუ არადა გამოიტანეთ False ( boolean )

num1 = int(input("Enter Num1"))
num2 = int(input("Enter Num2"))
print(num1 > num2)


#4) მომხმარებელს შემოვატანინოთ სიტყვა და n რიცხვი, შემდეგ გამოვიტანოთ ეს სიტყვა n-ჯერ.

num1 = input("word: ")
num2 = int(input("enter number1: "))
num = num1 * num2 
print(num)

#5) შემოაყვანინეთ მომხმარებელს ორი რიცხვი, და გამოპრინტეთ ამ ორი რიცხვის გაერთიანებულ ვერსისას დამატებული 1, მაგ თუ ჯერ შემოვიდა ათი შემდეგ 11, თქვენი მიზანია გამოიტანოთ 1012, ვინაიდან 10 გაერთანებული 11 არის 1011 და 1011 + 1 არის 1012

num1 = int(input("Enter Num1: "))
num2 = int(input("Enter Num2: "))
print((int(num1 + num2) + 1))
















