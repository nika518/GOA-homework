#1) მომხმარებელს შემოატანინეთ სიტყვა ან წინადადება შეინახეთ ის შეტრიალებულად reversed_string  ცვლადში და გამოიტანეთ ეს ცვლადი 

text = input("enter word: ")
print(text[::-1])

#2) გამოთვალეთ 0 დან 100ს ჩათვლით ყველა რიცხვის ჯამი და შეინახეთ ის sum ცვლადში
sum = 0
for i in range(0,100):
    sum+=i
print(sum)


#3) მომხმარებეს შემოატანინეთ სამ ასოიანი სიტყვა, თუ  მან არ შემოიყვანა სამი ასო მაშინ გამოუპრინტეთ რომ მან უნდა შეიყვანოს ზუსტად სამი ასო და გაუშვას პროგრამა თავიდან. როდესაც მომხმარებელი შეიყვანს სამ ასოიან სიტყვას, შეამოწმეთ არის თუ არა ის პალინდრომი და გაოუტანეთ True ან False შესაბამისად

text = input('sheiyvanet 3 asoiani texti: ')
if len(text) != 3:
    print('shen unda sheiyvano zustad 3 aso')
elif text == text[::-1]:
    print("true")
else:
    print("false")


#4) გამოიტანეთ 100დან 300მდე ყველა რიცხვის კვადრატი 

for x in range(100, 301):
    print(x**2)


#5) გამოიტანეთ ჯერ False, შემდეგ True, შემდეგ False, True, False... და ასე 1000-ჯერ

sequence = "False, True" * 500
print(sequence)






