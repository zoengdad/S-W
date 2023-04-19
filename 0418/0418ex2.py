'''
2023-04-12
장월
성적처리 프로그램(증첩 if문으로 작성)
두 과목 모두75이상 그리고 총점180이상 "최우수"
총점160이상 "우수", 150이상"보통",
두 과목 모두75미만면 "분발 합니다."
#문제분석
    변수 :점수1(score1), 점수2(score2), 합계(total).
#알고리즘
    1.변수선언
        점수1(score1), 점수2(score2)에 점수 입력 받기
    2.논리 (선택-중첩if)
        if(score1)>=75 and(score2)>=75 :
            if(total)>=180:
                최우수
            elif(total)>=160 :
                우수
            else:
                보통
        else :
            분발 합니다
'''

score1 = int (input("성적1 입력:"))
score2 = int (input("성적2 입력:"))
total = score1 + score2

if(score1)>=75 and (score2)>=75 :
    if (total)>=180 :
        print("최우수")
    elif (total)>=160 :
        print("우수")
    else :
        print("보통")

else :
    print("분발 합니다")