'''
2023-05-10
장월
#문제정의
    입력받은 숫자의 합이 1000이상이면 합계와 평균 출력
#문제분서
    변수-합계(sum),입력횟수(cnt),평균(avg),정수(num)
#알고리증
    1.변수선언(번수 초기화)
        num 키보트로 입력
        sum = 0,cnt = 0,abg = 0
    2.논리(반복안에 선택 포함)
        (반복) while True:
                num 키보트로 입력
                cnt 1증가
                sum에 더하기
            (선택)if sum >= 1000:
                    break
    3.합계, 평균 출력
       
'''

sum = 0
cnt = 0
avg = 0

while True:
    num = int(input("숫자 입력:"))
    cnt += 1
    sum += num

    if sum >= 1000:
        break

avg = sum / cnt

print('1000을 넘은수',sum,end=" ")
print("평균: %.2f"%avg)
