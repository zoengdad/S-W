'''
2023-05-16
장월
파일 입출력 - seek(0) 파일의 처음으로 포인트 이동
         - read(int n) 지정한 갯수만큼 파일 읽어 오기 
'''

f = open("/Users/gg/data/test.txt","r") #파일 객채 ft생성(읽기)

print(f.read(10),end='') #파일에서 10개의 문자 읽어서 출력(포인트 이동)
print(f.read(10),end='')
print(f.read(10))

f.seek(0) #파일의 처음으로 포인트 이동

print(f.read(10),end='') #파일에서 10개의 문자 읽어서 출력(포인트 이동)
print(f.read(10),end='')
print(f.read(10))

f.close() #파일 종료