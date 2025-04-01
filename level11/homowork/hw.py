def string_clean(s):
    string = ""
    for i in s:
        if i not in "0123456789":
            string+=i
    return string   

