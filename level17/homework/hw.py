   #1) შექმენით manual_remove ფუნქცია
def manual_remove(list, item):
    new_list = []
    remove = False   # ჯერ ვუთითებთ რომ წააშლილი არაფერია
    for i in list:
        if i == item and not remove:
            remove = True
            continue    # ეს ნიშნავს რომ რა რიცხვსაც მივუთითებთ item არგუმენტის ნაცვლად ის ამოვარდება და ციკლი გაგრძელდება
        new_list.append(i) # ვამატებთ იტერაციას
    return new_list
list=[1,2,3,4,5]
res = manual_remove(list, 2)
print(res)

# 2)შექმენით manual_index ფუნქია
def manual_index(listn, number):
    for i in range(len(listn)) :
        if listn[i] == number:
            return i
    return 'unknown value'
listn = [1,2,3,4,5,6]
res = manual_index(listn,3)
print(res)


#3)შექმენით manual_len ფუნქცია
def manual_len(number):         # შეგვიძლია სტრინგიც ჩავსვათ 
    count = 0
    for i in number:
        count += 1    # ყოველი იტერაციის დროს count - ს დაემატება +1
    return count

number = [1,2,3,4,5,6,7,8,9,10]
res = manual_len(number)
print(res)

#4) შექმენით manual_pop ფუნქცია'''

def manual_pop(number, value):
    remove = False
    count = []
    for i in number :
        if i == value and not remove:
            remove = True
            continue
        count.append(i)
    return count    
number = [1,2,3,4,5,6]
res = manual_pop(number,2)
print(res)

# 5) შექმენით manual_reverse ფუნქცია


def manual_reverse(number):
    reversed_list = []
    for i in range(len(number)-1,-1,-1):
        reversed_list.append(number[i])
    return reversed_list
number = [1,2,3,4,5]
print(manual_reverse(number))






