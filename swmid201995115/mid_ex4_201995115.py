'''
#문제분석
    ans 입력 가장 종아하는 번호 저장
    입력수자 보다 작아 높아
#알고리즘
    1.변수 ans num
    2.수식
    ans > num 작아
    ans < num 높아
    ans = num 종아
'''
ans = int (input ("입력 가장 종아하는 번호 저장"))
num = int (input ("숫자 입력:"))

if ans > num :
    if ans < num:
        print("{} 더 높아요.".format(num))
    print("{} 더 작아요.".format(num))

else:
    print("{} 종아하는 번호.".format(num))