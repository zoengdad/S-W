'''
2023-04-19
장월
성별,키,몸무게을 입력 받아서 BMI 지수를 구하고 비만도 측정하기
#문제분석
    변수:성별(sex),키(height),몸무게(weight),평균BMI(avg).
    수식:
        m: avg = height * weight * 22
        f: avg = height * weight * 21
        BMI: weight / avg * 100
#알고리즘
    1.변수선언
        성별(sex),키(height),몸무게(weight) 정수로 입력
    2.논리 (내포된 선택)
        if 성별이 여자:
            avg 계산
            if avg >= 120:
                "비만"
            elif 110<= avg <= 119:
                "과체중"
            else:
                "표준"
        elif 성별이 남자:
            avg 계산
            if avg >= 120:
                "비만"
            elif 110<= avg <= 119:
                "과체중"
            else:
                "표준"
        else:
            "성별 잘 못 입역"
        
'''
sex = input("성별 입력('M or m 또는 F or f'): ")
height = float(input("키 입력(cm): ")) / 100
weight = float(input("몸무게 입력(kg): "))

if (sex == "M" or sex == "m"): 
    avg = height * weight * 22
    if  weight / avg * 100 >= 120 :
        print("비만")
    elif 110 <= weight / avg * 100 <= 119 :
        print("과체중")
    else:
        print("표준")

elif (sex == "F" or sex == "f"):
    avg = height * weight * 21
    if  weight / avg * 100 >= 120 :
        print("비만")
    elif 110 <= weight / avg * 100 <= 119 :
        print("과체중")
    else:
        print("표준")

else:
    print("성별 잘 못 입역")