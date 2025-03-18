#For loop-ის დახმარებით შექმენით პროგრამა, სადაც მომხმარებელი შემოიტანს რიცხვს (50-ის ჩათვლით, თუ არა დაუპრინტეთ, რომ თავიდან შეიყვანოს), და თქვენ გამოიტანეთ ამ რიცხვის ჯერადები 100-ის ჩათვლით.

num = int(input('enter number'))
if num<=50:
    for i in range(1,101):
        if i%num == 0:
            print(i)

else:    
    print("please try again")


#შექმენით პატარა თამაში, სადაც თქვენ შექმნით რაიმე რიცხვების თანმიმდევრობას (ოთხნიშნა integer-რიცხვი), და მომხმარებელმა კი უნდა გამოიცნოს ეს თანმიმდევრობა (გამოიყენეთ While loop)

num = int(input("enter sequences"))
num1 = 1020
while num!=num1:
    print("arasworia")
    num = int(input("enter sequences"))
if num == num1:
    print("shemotanili mimdevroba sworia")
    

