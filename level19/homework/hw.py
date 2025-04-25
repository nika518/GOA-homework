#1)შექმენით ფუნქცია, რომელიც აერთებს ორ ლისტს (ორივეში მხოლოდ integer-ებია) და ასევე ალაგებს მათ ზრდადობის მიხედვით.

def ori_listi(list1,list2):
    combine = list1+list2
    combine.sort()
    return combine

list1 = [1,5,3,4,2]
list2 = [7,6,8,9,10]
res = ori_listi(list1, list2)
print(res)
        



#2)შექმენით ფუნქცია რომელიც არგუმენტებად იღებს ორ ლისტს და გამოაქვს ის, რომლის ელემენტებთა ჯამი (iteger-თა) უფრო მეტია.
def ori_listis_udidesi_jami(list1,list2):
    sum1=sum(list1)
    sum2=sum(list2)
    if sum2>sum1:
        return list2
    else:
        list1

list1 = [1,2,3,4]
list2 = [5,6,7,8]

shedegi = ori_listis_udidesi_jami(list1,list2)
print(shedegi)

#3)შექმენით ფუნქცია რომელიც იღებ არგუმენტებად ორ ლისტს და აბრუნებს დადებითი რიცხვების რაოდენობასა და უარყოფითების ჯამს (ცალ-ცალკე).

def ori_listi(list1,list2):
    combine = list1+list2
    pozitiuris_raodenoba = 0
    negatiuris_jami = 0

    for i in combine:
        if i > 0 :
            pozitiuris_raodenoba += 1
        elif i < 0 :
            negatiuris_jami += i
    return pozitiuris_raodenoba, negatiuris_jami

list1 = [1,2,3,-3,-10,5]
list2 = [-2,-6,6,7,8,9]

res = ori_listi(list1,list2)
print(res)



#4)შექმენით ფუნქცია რომელიც არგუმენტად იღებს ლისტს და შლის ყველა ელემენტს რომელიც უნაშთოდ იყოფა 3-ზე

def wavshalot_elementi_romelic_3ze_iyofa (list):
    new_list = []
    for i in list:
        if i % 3 != 0 :
            new_list.append(i)
    return new_list

list = [1,2,3,4,5,6,7,8,9,10]
res = wavshalot_elementi_romelic_3ze_iyofa(list)
print(res)




#5)შექმენით ფუნქცია რომელსაც გამოაქვს არგუმენტად გადაცემული ლისტის ფორმა, სადაც ყველა ელემენტი გარომაგებულია 2-ზე, მაგალითად input: [2,3,4,5], output: [4,6,8,10]


def gavaormagot_listi(list):
    return (i * 2 for i in list)

input_list = [1, 2, 3, 4, 5, 6]
output_list = gavaormagot_listi(input_list)
print(list(output_list))  







