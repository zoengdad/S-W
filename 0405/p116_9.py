'''
본봉과 수당을 정수로 입력 반아서 이번달 월급 수령액 구하는 프로그램(p116-9)
2023-04-05
장월
'''

sal=int(input("본봉:"))
allo=int(input("수당:"))

tax = (sal + allo) * 0.2
total_sal = sal + allo - tax

print("본봉{}, 수당{}, 수령액{}".format(sal,allo,total_sal))