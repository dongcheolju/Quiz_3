a=input("나이를 입력하세요.")
int(a)
if a > "19" :
    print("성인입니다")
elif a <= "19" :
    print("미성년자입니다.")


과일들 = ["사과", "바나나", "딸기"]
for 과일 in 과일들 :
    print(과일)

학생 = {"이름":"홍길동", "나이":19}
for i in 학생:
    print(i)

숫자 = 1
while 숫자 < 5 :
    print(숫자)
    숫자 = 숫자 + 1

else :
    print("숫자 변수가 5 이상이면 종료합니다.")



숫자 = 1
while 숫자 < 5 :
    print(숫자)
    break
    숫자 = 숫자 + 1

