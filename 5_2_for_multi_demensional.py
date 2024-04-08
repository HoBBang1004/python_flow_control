# 들여쓰기 엄청 중요!! 
# IndentationError: unexpected indent 오류는 들여쓰기나 띄어쓰기를 잘못했을 경우 발생하는 오류
# 자바에서의 arraylist 개념!!
# 이중 list (혹은 다차원 list)

"""
    리스트 안에 또 list를 넣어서 각 사람에 대한 정보도 넣을 수 있음 
    person = [
                ['hobbang','seoul','23'],
                ['owzl','gupondari','24'],
                ['dbwjd','bucheon','25'],
             ]

"""


persons = [
    ['hobbang','seoul','23'],
    ['owzl','gupondari','24'],
    ['dbwjd','bucheon','25'],

]

#만약 persons의 첫번째 index 값을 가져오고 싶다면?
print(persons[0])  #['hobbang', 'seoul', '23']
print(persons[0][0])  #hobbang -> persons의 첫번째 인덱스의 첫번째 값을 출력


print('-------------------------------------------')

# 이번에는 모든 인덱스의 이름을 반복적으로 출력해보자
for person in persons:
    print(person[0] +' , ' +  person[1] + ' , ' + person[2])




"""
    hobbang , seoul , 23
    owzl , gupondari , 24
    dbwjd , bucheon , 25

"""   

print('--------------------------')
 # 4. 응용해보자 
person = ['hobbang','seoul','23']
name = person[0]
address = person[1]
age = person[2]

print(name + ', ' + address + ', ' + age)  # hobbang, seoul, 23



# 4.처럼 list 이름 저장하고 각 인덱스에 대한 정의를 해주면 너무 귀찮음 
name, address, age = ['hobbang','seoul','23'] # 이렇게 작성해도 됨
print(name + ', ' + address + ', ' + age)  # hobbang, seoul, 23


print('------------------------------')

# 반복문을 이렇게도 작성가능 하다!!

for name, address, age in persons:
    print(name +' , ' +  address + ' , ' + age)

"""
hobbang , seoul , 23
owzl , gupondari , 24
dbwjd , bucheon , 25
    -> 결과 값이 제대로 출력됨
"""    

print('------------------1')


# 이름만 출력해보기
for name, address, age in persons:
    print(name)