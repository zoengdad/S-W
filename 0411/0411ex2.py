'''
선택문if-elif-else연습
2023-04-11
장월
'''

score=int(input("점수 입력:"))

if score>=90: #선택 조건1
    print("A학점") #조건1이 참인 경우
elif score>=80:#선택 조건2
    print("B학점") #조건2이 참인 경우
elif score>=70:#선택 조건3
    print("C학점") #조건3이 참인 경우
else:
    print("F학점") #조건1,2,3이 거지인 경우
