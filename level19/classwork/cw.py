
#1) 

def six_toast(num):
    return abs(num - 6)






#2) შექმენით ორი ლისთი და ლუპის მეშევოებით შექმენით ახალი ლისთი რომელიც იქნება ამ ორის გაერთანება



list1 = [1,2,3,4]
list2 = [5,6,7,8]
gaertianebuli = []

for i in list1:
    list1.append(i)

for i in list2:
    list2.append(i)
            
print(gaertianebuli)




#3) შექმენით ფუნქცია რომელიც იღებს მასივს და აბრუნებს ახალ მასივს კენტი ელემენტების გარეშე

def wavshalot_kenti(numbers):
    shedegi = []
    for i in numbers:
        if i % 2 == 0 :
            shedegi.append(i)
    return shedegi        
list = [1,2,3,4,5,6,7,8]
NewList = wavshalot_kenti(list)
print(NewList)
