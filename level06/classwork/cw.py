1#მომხარებელს შემოატანინეთ რაიმე რიცხვი, შემდეგ for ციკლის გამოყენებით შეამოწმეთ, არის თუ არა ეს რიცხვი მარტივი, თუ არის დაპრინტეთ "your number is a prime" თუ არ არის დაპრინტეთ "your number is not a prime" 

num =int(input('enter number'))
count = 0
for i in range(2,num+1):
    if num % i == 0 and count == 0:
        print("no prime num")
        break
else:
    print(' prime num')


