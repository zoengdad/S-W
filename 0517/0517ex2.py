'''
2023-05-17
장월
#문제정의
    기존파일을 새로운 파일에 복사하는 프로그램 만들기
#문제문석
    변수: 원본파일입력(source),복사할파일(target),
        뭔본파일의 내용(texts).
#알고리즘
    1. source에 원본파일 이름 입력
    2. target에 복사할파일 이름 입력
    3.파일 처리
        source파일 객체생성
            한 즐식 읽어 오기
            내용를 texts변수에 저장
        target파일 객체생성
            내용를 texts변수에 스기
            파일생성 출력
        
'''

source = input("source 파일 입력: ")
target = input("target 파일 입력: ")

with open("/Users/gg/data/linetest.txt","r") as f: #읽어파일 개체
    texts = f.read() #파일 한꺼번에 문자여로 읽기

with open("/Users/gg/data/copylinetest.txt","w") as fp: #스기파일 개체
    fp.write(texts) #원본파일에서 읽어 온 애용 파일에 출력

    print(target+"파일이 생성되었습니다.")#메세지 출력