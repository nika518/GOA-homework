
def check_alive(health):
    if health <= 0:
        return False
    else:
        return True
    


def repeat_str(repeat, string):
    return repeat * string




def cookie(x):
    if type(x) == str:
        name = "Zach"
    elif type(x) == int or type(x)== float:
        name = "Monica"
    else:
        name = "the dog"
        
    return f"Who ate the last cookie? It was {name}!"




def century(year):
    
    if year % 100 == 0:
        return year//100
    else:
        return year // 100 + 1




def find_average(nums):
    return sum(nums)/len(nums)









