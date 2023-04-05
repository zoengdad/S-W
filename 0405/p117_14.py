'''
5과목의 점수 총점과 평균을 구하는 프로그램을 작성(p117-14)
2023-04-05
장월
'''

num1=float(input('과목1 점수 입력:'))
num2=float(input('과목2 점수 입력:'))
num3=float(input('과목3 점수 입력:'))
num4=float(input('과목4 점수 입력:'))
num5=float(input('과목5 점수 입력:'))

total=num1+num2+num3+num4+num5
avg=total/5

print("5과목의 점수 총점{}, 평균{}.".format(total,avg))