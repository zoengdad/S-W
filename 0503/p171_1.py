'''
2023-05-03
장월
#문제정의
    반복문 0보다 큰 수에 대해서만 전체 합 평균 구하기
#문제분서
    변수-num
#알고리증
    1.변수선언
        num 정수 입력
    2.논리(반복-while)
        (조건) while count <= 10:
                합 평균 출력
'''

num=0
sum=0
count=1

num = int(input("숫자 입력"))

if num >= 0:
    sum = sum+num
    print("{}번째 숫자 : {}".format(count,num))
    count=count+1
while count <= 10:
    print("총 합 : {}".format(sum))
    print("평균 : {}".format(sum/10))
