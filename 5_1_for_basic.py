
# for문 작성법 

"""

** for문을 실행하기 위해서는 list가 무조건 필수적임!!

    * for 반복적으로 실행할 변수명 in list명
        print(반복적으로 실행할 변수명)


    ex) a = ['b','c','d']

        for v in a:
            print(v)

        ==> 여기서 v는 내가 정하는 변수명임 
        ==> 자동으로 list안에 있는 요소 하나하나가 다 v로 설정됨   




"""




names = ['dbwjd','owzl','hobbang']

# names 에 있는 모든 사람들에게 편지보내기 

for name in names:
    print(name)

# 결과 값 : dbwjd, owzl, hobbang 이 차례로 나옴


for name in names:
    print("Hi " + name + "! nice to meet you!")
    """
        Hi dbwjd! nice to meet you!
        Hi owzl! nice to meet you!
        Hi hobbang! nice to meet you!
    """