'''
2023-04-19
장월
입력받은 숫자가 양수 ,0 , 음수인지 판단
#문제분서 
    변수 - 정수 (num)
    수식 
        num > 0 양수
        num < 0 음수
#알고리즘(단순)
    1.변수 선언
        num 에 정수 입력
    2.논리(선택)
        if num > 0:
            양수
        elif num < 0:
            음수
        else:
            0
'''
#단순if문
num = int (input("숫자 입력: "))

if (num < 0 ):
    print("입력값 %d은(는) 음수입니다."%num)
if (num > 0 ):
    print("입력값 %d은(는) 양수입니다."%num)
if (num == 0):
    print("입력값 %d은(는) 0입니다."%num)

#이중if문
num = int (input("숫자 입력: "))

if (num < 0 ):
    print("입력값 %d은(는) 음수입니다."%num)
elif (num > 0 ):
    print("입력값 %d은(는) 양수입니다."%num)
else :
    print("입력값 %d은(는) 0입니다."%num)
