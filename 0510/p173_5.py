'''
2023-05-10
장월
#문제정의
    사용자로부터 가장 좋아하는 월을 입력 받아 그 월에 해당되는 계절을 출력 하시오.

#문제분서
    변수-월(month)
#알고리증
    1.변수선언(번수 초기화)
        month 정수 입력

    2.논리(반복안에 선택포함)
        if month = 3,4,5 봄
                 = 6,7,8 여름
                 = 9,10,11 가을
                 = 12,1,2 겨울
                 = 0 over
       
'''

while True:
    print("{:=^50s}".format("Split Line"))
    month = int(input("가장 좋아하는 월은?(종료 : 0): "))
    print("{:=^50s}".format("Split Line"))

    if month == 3 or month ==4 or month == 5:
        print("******",month,"월 ******")
        print(month,"월은 봄에 해당됩니다")

    elif month == 6 or month == 7 or month == 8:
        print("******",month,"월 ******")
        print(month,"월은 여름에 해당됩니다")
    
    elif month == 9 or month == 10 or month == 11:
        print("******",month,"월 ******")
        print(month,"월은 가을에 해당됩니다")

    elif month == 12 or month == 1 or month == 2:
        print("******",month,"월 ******")
        print(month,"월은 겨울에 해당됩니다")

    if month == 0:
        print("프로그램을 종료합니다.")
        break