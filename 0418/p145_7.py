'''
2023-04-12
장월
3장 연습문제 7번
두 정수 입력 x>y -> x//y, x<y -> x+y, x==y -> x*y
단,나놋셈 몫 계산할 때 y는 0안됨
#문제분석
    변수 : x, y 
#알고리즘
    1.변수선언
        x,y 에 점수 입력 받기
    2.논리 (선택-중첩if)
        x > y :
            x // y
        x < y :
            x + y
        x = y :
            x * y
'''

x = int (input("x의 값을 입력:"))
y = int (input("y의 값을  입력:"))

if x > y :
    if y == 0:
        print ("나놋셈 몫 계산할 때 y는 0 안됨")
    else:
        print ("x","//","y","=",x // y)
elif x < y :
    print ("x","+","y","=",x + y)
else :
    print("x","*","y","=",x * y)