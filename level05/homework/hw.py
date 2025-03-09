#1) for ციკლის გამოყენებით გამოიტანეთ რიცხვები 1-დან 10-მდე

for i in range(1,11):
   print(i)

 

#2) for ციკლის გამოყენებით გამოიტანეთ რიცხვები 5-დან 25-მდე
for i in range(5,26):
    print(i)



#3) for ციკლის გამოყენებით გამოიტანეთ რიცხვები 10-დან 100-მდე, 5ის stepით

for i in range(10,101,5):
    print(i)




#4) მომხმარებელს შემოატანინეთ ნებისმიერი სიტყვა, შემდეგ ამ სიტყვიდან გამოიტანეთ მხოლოდ 'A' ასოები, თუ არ შეიცავს 'A'ს გამოიტანეთ ცარიელი სტრინგი

word = input('enter your name') #manana
for i in word:
    if i == "A":
        print(i)
else:
    print("There is no A")        


#5) კომენტარებით დაწერეთ რას გამოიტანს შემდეგი გამოსახულება: True or True and False or True and False and False and True or False

print(True or True and False or True and False and False and True or False)
