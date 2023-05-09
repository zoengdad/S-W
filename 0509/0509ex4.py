'''
2023-05-09
장월
#문제정의
    1~100까지의 입력받은 숫자의 배수 합계
#문제분서
    변수-정수(num),합계(sum),반복변수(i)
#알고리증
    1.변수선언(번수 초기화)
        num변수에 정수 입력
        sum = 0
        i = 0
    2.논리(반복 while)
       while i <= 100:
        i = i + 1
        if i가 num의 배수가 아니면
            continue
        sum = sum + i
'''

num = int(input("배수 숫자 입력: "))
sum = 0
i = 0

while i <= 100:
    i = i + 1
    if i % num != 0:
        continue
    sum = sum + i

print("1~100까지의 {}의 배수 합: {}".format(num,sum))