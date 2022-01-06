'''
AUTHOR : HAIDER ALI JUTT
DATE   : JANUARY 20 2021
PURPOSE: CHALLENGE Mysirg.com
'''

from os import system,name
def clear():
    if name=='nt':
        _ = system('cls')
    else:
        _ = system('clear')

def addition(*args):
    pass

def substraction(*args):
    pass

def multiplication(*args):
    pass


def muna_func(text):
    # text=text.lower()
    text=text.lower().split(' ')

    calculation=[]
    for i in text:
        if i.isdigit():
            calculation.append(i)

    # print(calculation)
    try:
        if 'multiplication' in text or 'multiply' in text:
            print(f"Multiplication of {calculation[0]} and {calculation[1]} = {int(calculation[0])*int  (calculation[1])}")
        elif 'add' in text or 'sum' in text or 'addition' in text or 'plus' in text:
            print(f"Sum of {calculation[0]} and {calculation[1]} = {int(calculation[0])+int(calculation[1]) }")
        elif 'substraction' in text or 'minus' in text:
            print(f"Substraction of {calculation[0]} and {calculation[1]} = {int(calculation[0])-int    (calculation[1])}")
        elif 'division' in text:
            print(f"Division of {calculation[0]} and {calculation[1]} = {int(calculation[0])/int    (calculation[1])}")
        elif 'remainder'in text or 'modules' in text:
            print(f'Modules  =  {int(calculation[0])%int(calculation[1])}')
        elif 'square' in text:
            print(f"Square of {calculation[0]} = {int(calculation[0])**2} ")
        elif 'cube' in text:
            print(f"Cube of {calculation[0]} = {int(calculation[0])**3}")
        elif 'power' in text:
            print(f'Power of {calculation[0]} is {calculation[1]} = {int(calculation[0])**int(calculation   [1])}')
        elif 'hcf' in text:
            num=int(calculation[0])
            num2=int(calculation[1])
            for i in range(num,0,-1):
                if num%i==0 and num2%i==0:
                    print(f"HCF Of {calculation[0]} and {calculation[1]} = {i}")
                    break
        elif 'lcm' in text:
            num=int(calculation[0])
            num2=int(calculation[1])
            maxNum=max(num,num2)
            while True:
                if maxNum%num == 0 and maxNum%num2 == 0 :
                    print(f"LCM Of These Two Numbers = {maxNum}")
                    break
                maxNum+=1


        elif 'table' in text:
            table_number=int(calculation[0])
            for i in range(1,11):
                print(f'{table_number} * {i} = {table_number*i}')
        elif 'percentage' in text:
            obtain_marks=int(calculation[0])
            total_marks=int(calculation[1])
            per = ((obtain_marks*100)/total_marks).__round__(3)
            if per<33:
                print(f"Your Percentage is : {per} You Have Failed The Examination Failure ! ")
            else:
                print(f"Your Percentage is : {per}\nYou Have Passed The Examination Conguratulation ! ")
        elif 'factorial' in text:
            num=int(calculation[0])
            total=1
            for i in range(1,num+1):
                total*=i
            print(f"Factorial of {num} = {total}")
        elif 'quite' in text or 'exit' in text or 'suja' in text or 'clear' in text:
            exit()
        elif 'name' in text:
            print(f"My name is Munna Smart Calculator")
        else:
            print('Some Thing Went Wrong In Your Input Please Check It ! ')
    except Exception as e:
        print(f'YOUR QUESTION IS NOT DEFINED PLEASE TELL ME AGAIN')


if __name__ == "__main__":
    while True:
        print('\n\n\t\t\t\tMunna Smart Calculator')
        print('\n\t\t\t\tWelcome To Muna Calculator\n\n')
        a=input('Please Enter Some Text For Calculate : ')
        muna_func(a)
        input()
        clear()