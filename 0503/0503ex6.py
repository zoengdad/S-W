'''
2023-05-03
장월
#문제 정의 
    구구단 출력(증첩 반복)

#분제 분석
    변수- i, j

#알고리즘
    논리(반복 - 증첩 반복(for))
    (조건) for i in range(2,10) : #단 반복
            제목 출력
            for j in range(1,10): #단 잔애서 곱하는 수 반복
                구구단 출력
'''

for i in range(2,10):
    print ('##',i,'##')
    for j in range(1,10):
        print('{}*{}={}'.format(i,j,i*j))