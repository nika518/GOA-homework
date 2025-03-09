#1) for ციკლის გამოყენებით გამოიტანეთ რიცხვები 1-დან 10-მდე

for x in range(1,11):
   print(x)

 

#2) for ციკლის გამოყენებით გამოიტანეთ რიცხვები 5-დან 25-მდე
for x in range(5,26):
    print(x)



#3) for ციკლის გამოყენებით გამოიტანეთ რიცხვები 10-დან 100-მდე, 5ის stepით

for x in range(10,15,20,101):
    print(x)



#4) მომხმარებელს შემოატანინეთ ნებისმიერი სიტყვა, შემდეგ ამ სიტყვიდან გამოიტანეთ მხოლოდ 'A' ასოები, თუ არ შეიცავს 'A'ს გამოიტანეთ ცარიელი სტრინგი

name = input("please enter your name")
amount = 0
for i in name:
    if i == 'A':
        print(i)
        amount - amount + 1
if amount == 0:
    print("there are not any A letter")        



#5) კომენტარებით დაწერეთ რას გამოიტანს შემდეგი გამოსახულება: True or True and False or True and False and False and True or False