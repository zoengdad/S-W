'''
2023-05-16
장월
파일 입출력 - writelines() 리스트나 튜플 같은 자료형을 파일에 출력
         - writelines() 리스트나 튜플 자료형은 문자열 파일에 출력
         - write() 문자열만 파일에 출력
'''

L1 = ['충청남도','충청북도\n','전라남도','전라북도\n','경상남도','경상북도\n'] # 문자열 리스트

L2 = [1,2,3,4,5] # 정수 리스트

with open("/Users/gg/data/linetest.txt","w") as f : # with를 이용하여 쓰기 모드로 파일 객체 생성
    
    f.writelines(L1)   # writelines() L1리스트의 내용 파일에 출력
    # f.writelines(L2) 