'''
2023-05-10
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

sum=0
count=0
i=0

num = int(input("숫자를 입력하시오:"))

while True:
    i = i + 3
    sum = sum + i
    count = count + 1
    if sum > num :
        break
print("{}을 넘었을 때의 값 : {}".format(num,i))

print("{}을 넘었을 때까지의 총 합계 : {}".format(num,sum))

print("{}을 넘었을 때까지 몇 번째 3의 배수인가 : {} ".format(num,count))