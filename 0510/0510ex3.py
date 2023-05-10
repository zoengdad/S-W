'''
2023-05-10
장월
#문제정의
    입력받은 숫자 만킁 즐 반복 하면서 별 찍기
#문제분서
    변수-숫자(num)
#알고리증
    1.변수선언(번수 초기화)
        num 변수에 정수 입력
    2.논리(증첩 반복)
        (반복) for i in range(1,num+1) #즐 반복
            (반복) for j in range(1,i+1) #별 찍기 반복
                    별 찍기
       
'''

num = int(input("숫자 입력:"))
for i in range(1,num+1):
    for j in range(1,i+1):
        print("*",end=" ")
    print() #즐 바꿈

#거꾸로 출력
print("\n거꾸로 출력")

num2 = int(input("숫자 입력:"))
for i in range(1,num2+1):
    for j in range(i,num2+1):
        print("*",end=" ")
    print() #즐 바꿈