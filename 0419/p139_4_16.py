'''
2023-04-19
장월
p139실습예제 4_16
#문제분서 
    변수 - 직급 (level),나이 (age)
    수식 
        40<=age<=49 & level=7(8)
        연금 80% 다상자
        50<=age<=59 & level=5(6)
        연금 100% 다상자

#알고리즘(단순)
    1.변수 선언
        level,age 에 정수 입력
    2.논리(선택)
        if 40<=age<=49 & level=7(8)
        연금 80% 다상자
        elif 50<=age<=59 & level=5(6)
        연금 100% 다상자
        else
'''

level = int (input("직급 입력 :"))
age = int (input("나이 입력 :"))

if (((level == 7) or (level == 8)) and ((40 <= age) and (age <= 49))) :
    print ("연금 80% 다상자입니다.")

elif (((level == 5) or (level == 6)) and ((50 <= age) and (age <= 59))) :
    print ("연금 100% 다상자입니다.")

else:
    print("연금 대상자가 아닙니다.")
