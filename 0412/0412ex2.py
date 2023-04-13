'''
입력받은 두 수의 크기 비교
2023-04-12
장월
#문제 분서
    변수-숫자1(num1),숫자2(num2)
#알고리즘
    1.변수 선언
        num1,num2에 정수 입력
    2.논리(선택)
        if num1 > num2:
            (참)큰 수는 num1,작은수 num2
        else:
            (거짓)큰 수는 num2,작은수 num1
'''

first=input("input num1:")#첫번째 정수 입력
second=input("input num2:")#두번째 정수 입력

if first>second:#선택 조건
    print("Big number is:",first,"Small number is:",second)#조건이 참일때 실행
eles:print("Big number is:",second,"Small number is:",first)#조건이 거짓일때 실행
