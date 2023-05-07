'''
2023-05-03
장월
#문제정의
    반복문 단, 짝수 번째에 입력되는 숫자는 양수는 음수로, 음수는 양수로 바꾸어 합을 구하
#문제분서
    변수-num
#알고리증
    1.변수선언
        num 정수 입력
    2.논리(반복-while)
        (조건) while j <= 100: 
                합 출력
'''

num=0
sum=0
count=1

num=int(input("숫자 입력"))

if(count%2==0):
    num=-num
    print ('{}번째 정수 :{}'.format(count,num))
    
if(count%2==1):
    print ('{}번째 정수 :{}'.format(count,num))

while(count<=10):
    sum=sum+num
    count=count+1
    print("총 합 : {}".format(sum))