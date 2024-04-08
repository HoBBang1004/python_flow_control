# java의 else if와 같은 건 elif


# 결과문 : 0 1 4 
# 이유 : 만약 if문의 첫번째 조건이 만족한다면 나머지 조건은 실행안됨 
# 그래서 첫번째 print(1)만 출력되고 나머지는 출력 안된 것 임
print(0)
if True:
    print(1)
elif True:
    print(2)
else:    
    print(3)
print(4)


print("---------------------------")

#만약 첫번째 조건문의 false로 바꾼다면?
# 결과값 : 0 2 4 
# 이유 : False 건너뛰고 그 다음 True를 실행하고 밑에 조건문은 무시하기 때문

print(0)
if False:
    print(1)
elif True:
    print(2)
else:    
    print(3)
print(4)


print("-----------------------")


#만약 조건이 모두 False 라면?
# 결과값 : 0 3 4 
# 이유 : False는 모두 건너뛰어서 else문의 print(3)만 출력됨

print(0)
if False:
    print(1)
elif False:
    print(2)
else:    
    print(3)
print(4)