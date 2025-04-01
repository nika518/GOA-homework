#1
def calculator(x, y, op):
    if type(x) == int and type(y) == int:
        if op == "+":
            return x  +  y
        elif op == "-":
            return x - y
        elif op == "*":
            return x * y
        elif op == "/":
            return x / y
        else:
            return "unknown value"
    else:
        return "unknown value"



#2
def string_clean(s):
    string = ""
    for i in s:
        if i not in "0123456789":
            string+=i
    return string   


#4
def count_char_occurrences(strng, char):
    count = 0
    for i in strng:
        if i == char:
            count+=1
    return count   





