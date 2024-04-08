#이번엔 id를 두 개를 구분할 것임

input_id = input('id : ')
id1='dbwjd'
id2='owzl'



# 사용자에게 id를 입력받아서 만약 'dbwjd' 혹은 'owzl'와 같다면 welcome을 출력하고 아니라면 who are you? 출력하게 함


# elif를 사용하는 방법
if input_id == id1:
    print('welcome ' + id1 + " ~!")
elif input_id == id2:
    print('welcome ' + id2 + " ~!")
else:  
    print('who are you?')