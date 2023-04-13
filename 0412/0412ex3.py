'''
두 점수 입력 후, 모두 짝수이면""출력, 모두 훌수이면""출력
아니면 "훌수,짝수 섞어 있음"출력
2023-04-12
장월
#문제 분서
    변수-num1,num2에 정수 입력
    수식-num1%2==o(num1은 짝수)/num1%2!=o(num1은 홀수)
#알고리즘
    1.변수 선언
        num1,num2에 정수 입력
    2.논리(선택if~elif~else)
        if num1%2==0 and num2%2==0:
            (참)모두 짝수
        elif num1%2==1 and num2%2==1:
            (참)모두 홀수
        else:
            훌수,짝수 섞어 있음 
'''

first=input("input num1:")#첫번째 정수 입력
second=input("input num2:")#두번째 정수 입력

if first%2==0 and second%2==0:
    print("첫번째 정수:",first,"두번째 정수:",second,"모두 짝수.")
elif first%2==1 and second%2==1:
    print("첫번째 정수:",first,"두번째 정수:",second,"모두 홀수.")
else:
    print("첫번째 정수:",first,"두번째 정수:",second,"훌수,짝수 섞어 있음.")
