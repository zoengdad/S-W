'''
2023-04-12
장월
성적처리 프로그램(증첩 if문으로 작성)
입력받은 성적이 90이상이면a ,80이상 90미만b ,70이상 80미만c ,70이하이면 f.
#문제분석
'''

jumsu = int (input("성적 입력:"))

if jumsu >= 70: #조건1
    if jumsu >= 80: #조건2
        if jumsu >=90: #조건3
            print("A학점") #조건3 참
        else : #조건3은 거짓,조건2는 참
            print("B학점") #조건2 참
    else: #조건2은 거짓,조건1는 참
        print("C학점") #조건1 참
else: #조건1 거짓
    print("F학점")