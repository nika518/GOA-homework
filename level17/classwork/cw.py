
# 1) manual sum ფუნქციის შექმნა

def manual_sum(numbers):
    total = 0
    for i in numbers:
        total += i
    return total

num = [1,2,3,4,5]
res = manual_sum(num)
print(res)


# 2) შექმენით manual_append ფუნქცია
 
def my_list(list, item): #შევქმნათ ფუნქცია და შევიტანოთ არგუმენტად list(რაც გვაქ მოცემული) და item (რა რიცხვის დამატებაც გვინდა )
    new_list = [] #შევქმნათ ახალი ცარიელი ლისთი
    for i in list:
        new_list += [i] 
    new_list += [item]    
    return new_list 
list = [1,2,3]
res = my_list(list,"ნიკა")
print(res)












