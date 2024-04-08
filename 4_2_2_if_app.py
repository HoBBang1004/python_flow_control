input_id = input('id : ')
id='dbwjd'


# 사용자에게 id를 입력받아서 만약 id가 'dbwjd'과 같다면 welcome을 출력하고 아니라면 who are you? 출력하게 함


# else를 사용하지 않는 방법
#if input_id == id:
    #print('welcome')


#if input_id != id:
    #print('who are you?')



# else를 사용하는 방법
if input_id == id:
    print('welcome')
else:
    print('who are you?')