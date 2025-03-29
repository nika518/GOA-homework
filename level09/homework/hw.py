#1
def repeat_str(repeat, string):
    return repeat * string



#2
def say_hello(name):
    return "Hello,"+" "+ name



#3
def rps(p1, p2):
    if p1==p2:
        return "Draw!"
    elif p1=='rock' and p2 =='scissors':
        return "Player 1 won!"
    elif p1 == 'scissors' and p2 == 'paper':
        return "Player 1 won!"
    elif p1 == 'paper' and p2 == 'rock':
        return "Player 1 won!"
    else:
        return "Player 2 won!"
    

#4
def get_grade(s1, s2, s3):
    avarage = (s1+s2+s3)/3
    if 90<=avarage<=100:
        return 'A'
    elif 80 <= avarage < 90:
        return 'B'
    elif 70 <= avarage < 80:
        return 'C'
    elif 60 <= avarage < 70:
        return 'D'
    else:
        return 'F'
    

#5
def simple_multiplication(number) :
    if number%2 == 0:
        return number * 8
    else:
        return number * 9



#  შექმენით ფუნქცია რომელსაც გადაეცემა ორი პარამეტრი name, lastname. თქვენი დავალებაა გამოიტანოთ სახელის პირველი ასო, წერტილი და გვარი, მაგალითად:
def name(name,lastname):
    return name[0] + "." + lastname

print(name('goga', 'chalauri'))













