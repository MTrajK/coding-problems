#fUNCTION FOR FIND ING THE CO=PRIME NUMBERS
def coprime_no(a,b):
    f = 1
    for i in range (1,a+1):
        if a%i==0 and b % i== 0:
            f = i
    return f == 1
#rEADING THE NUMBERS FROM THE USER
first_no = int(input(''))
second_no = int(input(''))

if coprime_no(first_no,second_no):
    print(first_no,"and",second_no,"are CO-PRIME numbers")
else:
    print(first_no,"and",second_no,"are not CO-PRIME numbers")
