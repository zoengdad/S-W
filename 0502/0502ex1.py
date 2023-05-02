'''
2023-05-02
장월
파이썬 내장함수
'''

# 자료형 변환 함수
s = '123114' #s변수에 문자열 '123' 저장

ch1 = int(s) #ch1 변수에 s를 정수로 변환해서 저장
ch2 = list(s) #ch2 변수에 s를 리스트로 변환해서 저장
ch3 = tuple(s) #ch3 변수에 s를 튜플로 변환해서 저장
ch4 = set(s) #ch4 변수에 s를 집합으로 변환해서 저장 (증복 제거)

print('{} 의 자료형은 {}'.format(ch1,type(ch1)))
print('{} 의 자료형은 {}'.format(ch2,type(ch2)))
print('{} 의 자료형은 {}'.format(ch3,type(ch3)))
print('{} 의 자료형은 {}'.format(ch4,type(ch4)))

print() #한 줄 띄우기
num1 = abs(-5) #num1변수에 -5 의 절대값 저장
num2 = round(4,6) #num2변수에 반올립 값 저장
num3 = bin(10) #num3변수에 정수10를 이진수로 변환해서 저장
str1 = chr(97) #str1변수에 97에 해당하는 문자 저장
str2 = ord('A') #str2변수에 'A'의 아스키 코드값 저장

print('-5 의 절대값: ',num1)
print('4,6에 반올립값: ',num2)
print('10를 이진수로 변환: ',num3)
print('97에 해당하는 문자: ',str1)
print('A의 아스키 코드값: ',str2)

print() #한 줄 띄우기

num10 = [6,3,5,1,9,2,8] #리스트 자료형
print('num10 원소의 길이: ',len(num10))
print('num10 원소 종 가장 큰 값: ',max(num10))
print('num10 원소 종 가장 작은 값: ',min(num10))
print('num10 원소들의 합계: ',sum(num10))
print('num10 원소들 정렬: ',sorted(num10)) #오름차순

print() #한 줄 띄우기

print(zip('123',('kim','lee','part')))

#문자열과 튜플를 몪어서 리스트 자료형으로 반환
print(list(zip('123',('kim','lee','part'))))

#문자열과 튜플를 몪어서 튜를 자료형으로 반환
print(tuple(zip('123',('kim','lee','part'))))
