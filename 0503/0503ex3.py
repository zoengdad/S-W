'''
2023-05-03
장월
#문제정의
    1~ 입력받은 숫자까지의 합계 구하기
#문제분서
    변수-숫자(num) ,합계(total)
#알고리증
    1.변수선언
        num에 정수 입력
        total = 0
    2.논리(반복)
        (조건) for i in range(1,num+1):
    
'''

num = int(input('합계 구할 숫자:'))
total = 0

for i in range (1,num + 1):
    total = total + i #합계
print('1~{}까지 합계{} '.format(num,total))