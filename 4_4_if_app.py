# 로그인 기능 간이 구현해보기 
# 아이디와 비번 모두 일치한다면 welcome!
# 만약 아이디는 맞지만 비번이 틀리면 pw wrong!
# 만약 비번은 맞지만 아이디 틀리면 id wrong! 출력
# 실행됨



input_id = input('id? : ')
id='dbwjd'
input_password = input('password? : ' )
password = '1111'

# 이건 나만의 방법
"""
if input_id == id and input_password == password:
    print("welcome")
elif input_id != id and input_password == password: 
    print("id wrong!")  
else:    
    print("pwd wrong!")
"""

# 강사님께서는 중첩하셔서 작성하심 
# 강사님의 코드

if input_id == id:
    if input_password == password:
        print("welcome")
    else:
        print("pwd wrong!") 
else:
    print("wrong id")





# 이건 내가 모든 경우의 수를 조건문으로 출력해본 것임
# 제대로 실행됨
"""
if input_id == id:
    if input_password == password:
        print("welcome")
    else:
        print("pwd wrong!") 

 * elif부터는 따질 필요 없는 듯 
 * 왜냐하면 강사님의 코드를 보면 간단하게 작성해도 나와 같은 결과가 나옴
 * 어차피 아이디가 틀려도 비번은 입력받아야 하니까 아이디가 다를 경우에는 그냥 wrong id라고만 하면 됨 
 * 내가 작성한 코드 같은 경우는 만약 id를 틀리게 입력했을 때 비번을 입력못하게 막게 구현했다면 맞는 코드임 

elif input_id != id:
    if input_password == password:
        print("id wrong!")
    elif input_password != password:
        print("id , pwd wrong!")    
else:
    print("welcome")                
"""