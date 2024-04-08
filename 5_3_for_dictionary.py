# 자바에서 hashmap 개념! (객체 개념도 조금 있는 듯)
# key:value로 이뤄져 있음!!
# value값을 출력하고 싶다면 print(key) 출력할 때 key값을 입력해주면 됨
# list와는 다르게 []가 아닌 {}로 감싸야 함!!

"""
    * 작성법 
    list 이름 ={'key':value, 'key':'value', 등등}
"""


person = {'name' : 'dbwjd','address':'seoul','age' : '23'}

# person의 name의 value를 출력해보자
print(person['name']) # dbwjd 잘 나옴 
# print(person['dbwjd']) # key값을 출력할 수는 없음! 오류 발생함


print('--------------------------------')

# 반복문을 이용해서 출력해보자 
for key in person:
    print(key) # value 값이 아닌 key값이 출력됨 

"""
name
address
age

"""


print('--------------------------------')
# 그럼 만약 value값을 출력하고 싶다면?
# key값을 설정해주고 person 안에 key값의 value를 출력하라는 의미
for key in person:
    print(person[key])

"""
dbwjd
seoul
23
"""    

print('--------------persons------------------')
# 자바에서의 객체를 만들어보자 
persons = [
    {'name' : 'dbwjd','address':'seoul','age' : '23'},
    {'name' : 'owzl','address':'zamsil','age' : '24'},
    {'name' : 'hobbang','address':'sky','age' : '100'}

]

# 이제 for문으로 데이터 출력해보자 

for person in persons:
    print(person)


"""
{'name': 'dbwjd', 'address': 'seoul', 'age': '23'}
{'name': 'owzl', 'address': 'zamsil', 'age': '24'}
{'name': 'hobbang', 'address': 'sky', 'age': '100'}

"""

print('  ')

print('-------------- 이중 for문 -----------------')



# ★ 이중 for문을 활용 ★
# list의 각 인덱스의 값과 그 인덱스의 value 값을 각각 출력해보자


for person in persons: # 이걸 통해서 list에서 각 인덱스에 접근 가능
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print(person)  # 여기에서는 각 인덱스의 값들이 출력됨
    for key in person:  # 각 인덱스의 key 값에 접근
        print(key, ':' , person[key]) # 접근한 key값에 해당하는 value값 출력
        print('')

"""
-------------- 이중 for문 -----------------
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
{'name': 'dbwjd', 'address': 'seoul', 'age': '23'}
name : dbwjd

address : seoul

age : 23

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
{'name': 'owzl', 'address': 'zamsil', 'age': '24'}
name : owzl

address : zamsil

age : 24

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
{'name': 'hobbang', 'address': 'sky', 'age': '100'}
name : hobbang

address : sky

age : 100

"""        
