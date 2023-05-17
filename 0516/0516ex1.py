'''
2023-05-16
장월
파일 입출력
'''

ft = open("/Users/gg/data/test.txt","w") #파일 객채 ft생성(읽기)

for i in range(1,11): #10번 반복
    ft.write("%d번째 줄입니다.\n"%i) #ft에 i출력

ft.close() #파일 종료