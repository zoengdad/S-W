'''
2023-05-03
장월
반복문 1~10까지 합계 구하기
'''

#for반복문
sum1 = 0 #합계
for p in range(1,11): #반복 조건
    sum1 = sum1 + p #합계 저장
print('1~10까지 합계: ',sum1)

print() #한 줄 띄우기

sum10 = 0 #합계
for q in range(1,101): #반복 조건
    sum10 = sum10 + q #합계 저장
print('1~100까지 합계: ',sum10)

print() #한 줄 띄우기

#while반복문
i = 1 #i(반복횟수) 초기화
sum = 0 #합계
while i <= 10: #반복 조건
    sum = sum + i #합계 저장
    i = i + 1 #i 1증가
print('1~10까지 합계: ',sum)

print() #한 줄 띄우기

j = 1 #i(반복횟수) 초기화
sum100 = 0 #합계
while j <= 100: #반복 조건
    sum100 = sum100 + j #합계 저장
    j = j + 1 #i 1증가
print('1~100까지 합계: ',sum100)

