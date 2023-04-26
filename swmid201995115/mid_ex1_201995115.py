'''
#문제분석
    water ,salt 입력 농도avg 를  구기
#알고리즘
    1.변수 water ,salt
    2.수식
    avg = (salt / water)*100%
'''

salt=int(input("소금 양 :"))
water=int(input("물 양 :"))

avg = (salt / water)* 0.1
print("소금{}g,물{}g 일 때소금물 농도는{}%입니다.".format(salt,water,avg))