'''
2023-05-17
장월
#문제정의
    학생이름 성적 3개 반아서 파일에 저장하기
#문제문석
    변수: 이름성적 입력(score),반복 변수 i
#알고리즘
    1. 파일 객체 생성(w모드)
    2. 이름성적 입력(5명-반복)
        while i <= 5;
            score변수에 이름성적 입력
            파일에 쓰기
            i 1증가
        
'''

f = open("/Users/gg/data/stu.txt","w")  # stu.txt 파일을 쓰기 모드로 설정

i = 1
while i <= 5 :  # 5번 반복
    
        score = input("%d번째 학생이름과 3과목성적 입력(예: 홍길동 80 90 70) : "%i) #이름과 성적으로 공간으로 구분하여 입력
        
        f.write(score+"\n")  # 줄 바꿈 문자를 포함하여 파일에 저장
        i += 1
        
f.close()  # 파일 종료