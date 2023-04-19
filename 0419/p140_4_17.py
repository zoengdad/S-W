'''
2023-04-19
장월
p140실습예제 4_17
#문제분서 
    변수 - 키 (height),나이 (age)
    수식 
        age >= 8 & age >= 120
        고속 롤러코스터
        age >= 8 & age < 120
        저속 롤러코스터
        age < 8
        NOPE!

#알고리즘(단순)
    1.변수 선언
        height,age 에 정수 입력
    2.논리(선택)
        if age >= 8 height >= 120
            고속
        if age >= 8 height < 120
            저속
        else
'''

age = int(input("나이 입력 :"))

if age >= 8 : 
    height = int (input("키 입력(cm) :"))
    if height >= 120 :
        print("고속 롤러코스터 입장 가능")
    else :
        print("저속 롤러코스터 입장 가능")

else :
    print("입장할 수 없습니다.")