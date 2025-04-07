'''შექმენით ფუნქცია, რომელსაც გადაეცემა შემდეგი ლისთი: [1,23,165,2,3,92,10,34,911] და ერთი ინტეჯერი(მაგ. 3), თქვენი დავალებაა, რომ ახალ ცარიელ ლისთში შეინხოთ მხოლოდ ისეთი რიცხვები, რომლებიც უნაშთოთ იყოფიან გადმოცემულ ინტეჯერზე(ამ შემთხვევაში 3-ზე).'''

num = [1,23,165,2,3,92,10,34,911]
res = []
def isprime(n):
    
    if n == 1:
            return
    for i in range(2,n):
          if n%i == 0:
                return False
    return True           

for i in num:
      if isprime(i):
            res.append(i)
print(res)
            


#2 codewars


def reverse_list(l):
    return l[::-1]







# 3 codewars
def even_last(numbers):
    if len(numbers) == 0:
        return 0
    res = 0
    for i in range (0,len(numbers),2):
        res += numbers[i]
    return res * numbers[-1]

    








