'''
2023-05-03
장월
#문제정의
    반복문 1부터 100까지의 합을 구하여 다음과 같이 출력
#문제분서
    변수-num
#알고리증
    1.변수선언
        num 정수 입력
    2.논리(반복-while)
        (조건) while j <= 100: 
                합 출력
'''

j = 1 #j(반복횟수) 초기화
sum100 = 0 #합계

if j % 10 == 0 :
    print("1-"+j+" : "+sum100)
    
while j <= 100: #반복 조건
    sum100 = sum100 + j #합계 저장
    j = j + 1 #j 1증가
print('1~100까지 합계: ',sum100)