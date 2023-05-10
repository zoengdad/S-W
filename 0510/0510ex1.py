'''
2023-05-10
장월
#문제정의
    입력받은 숫자가 소수인지 아닌자 판별하는 프로그랩
#문제분서
    변수-정수(num)
#알고리증
    1.변수선언(번수 초기화)
        num변수에 정수 입력
        sum = 0
        i = 0
    2.논리(반복안에 선택포함)
        (반복) for i in range(2,num+1):
            (선택)num % i == 0:
                    break
        (선택) if num == i:
                    소수
            else:
                    소수 아닌
       
'''

num = int(input("소수 검즘 숫자: "))
for i in range (2, num + 1):
    if num % i == 0:
        break
if num == i:
    print('{} 소수'.format(num))
else :
    print('{} 소수 아닌'.format(num))