'''
2023-05-17
장월
for문 이용한 파일 엵기
'''

#for문 이용한 파일 엵기 오기
with open("/Users/gg/data/linetest.txt","r") as f: #파일 엵기
    for line in f: #파일객채를 지정해서 반복문 적성
        print (line,end=' ') #쫄 바꿈 없이 출력

#readline(): [한 줄씩 읽어 오기] 메소드로 파일 읽어 오기
print()

with open("/Users/gg/data/linetest.txt","r") as f: #파일 엵기
    while True: #무한 반복
        line = f.readline() #파일 한 줄씩 읽어 오기
        print(line,end=' ') #줄 바꿈 없이 출력

        if line ==' ': #읽어 올 내용 없다면
            break #반복 종료

#readline(): 한 줄씩 읽어서 리스트형으로 반환
print()

with open("/Users/gg/data/linetest.txt","r") as f: #파일 엵기
    textlists = f.readlines()
    print(type(textlists))
    print(textlists)

#print() 함수로 파일 출력하기
f=open("/Users/gg/data/ptest.txt","w") #쓰기 모드의 파일 개체 생성

print("aaaaaa",file=f) #파일에 출력
print("bbbbbb",file=f) #파일에 출력
print("cccccc",file=f) #파일에 출력

f.close() #파일 달긴