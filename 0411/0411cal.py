'''
사칙연산을 수행하는 프로그램 작성 연습
2023-04-11
장월
'''

num1 = int(input('num1에 정수 입력：'))
op = input('op에 연산자 입력:')
num2 = int(input('num2에 정수 입력:'))

if op == '+':
    res = num1 + num2
    print(str(num1) + '+' + str(num2) + '=' + str(res))
elif op == '-':
    res = num1 - num2
    print(str(num1) + '-' + str(num2) + '=' + str(res))
elif op == '*':
    res = num1 * num2
    print(str(num1) + '*' + str(num2) + '=' + str(res))
elif op == '/':
    res = num1 / num2
    print(str(num1) + '/' + str(num2) + '=' + str(res))
else:
    print('NOPE！')
