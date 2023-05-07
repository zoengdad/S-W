'''
2023-05-03
장월
#문제정의
    반복문 3의 배수의 총합이 입력된 숫자를 넘었을 때의 N값과 총합계
#문제분서
    변수-num
#알고리증
    1.변수선언
        num 정수 입력
    2.논리(반복-while)
        (조건) while(count <= num):
                넘었을 때의 값, 넘었을 때까지의 총 합, 넘었을 때까지 몇 번째 3의 배수 출력
'''

num=0
sum=0
count=3

num = int(input("숫자를 입력하시오:"))

print("사용자 입력 : {}".format(num))

while(count <= num):
    sum = sum + count
    count = count + 3
    div = count/3
print("{}을 넘었을 때의 값 : {}".format(num,count))

print("{}을 넘었을 때까지의 총 합계 : {}".format(num,sum))

print("{}을 넘었을 때까지 몇 번째 3의 배수인가 : {} ".format(num,div))