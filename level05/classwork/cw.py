#1) for ციკლით გადაუარეთ რიცხვებს 2-დან 25-მდე და გამოიტანეთ მხოლოდ კენტი რიცხვები

for x in range(2,25):
    if x % 2 == 1:
        print(x)


 #2 მომხმარებელს შემოატანინეთ სახელი inputის დახმარებით, შემდეგ for ციკლით გადაუარეთ ამ სახელს და გამოიტანეთ თვითოეული ასო ცალ-ცალკე

name = input("enter name")
for x in name:
    print(x)

#3) შექმენით correct_password ცვლადი სადაც შეინახავთ რაიმე პაროლს, შემდეგ მომხმარებელს inputით შემოატანინეთ რაიმე პაროლი, 
#  სანამ ეს მომხმარებლის შემოტანილი პაროლი არ უდრის correct_passwordს თავიდან შემოატანინეთ მომხმარებელს პაროლი


correct_password = "nika12345"
paroli = input("enter password")
while correct_password != paroli:
    print("password isn't correct, try again")
    paroli = input("enter password")
    print("paroli sworia")



