'''
#문제분석
    num1 ,num2 입력 배수를 구하기
#알고리즘
    1.변수 num1 ,num2
    2.수식
    num1 % num2 == 0;
'''
num1 = int(input("첫 번째 정수를 입력 :"))
num2 = int(input("두 번째 정수를 입력 :"))

if num1 // num2 != 0:
    print("배수")
else:
    print("배수 아니다.")