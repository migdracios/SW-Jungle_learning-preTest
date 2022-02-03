# Q1. 과일 갯수 세기 함수 만들기

fruits = ['사과','배','배','감','수박','귤','딸기','사과','배','수박']

# 1. 사과의 갯수를 센다면 어떻게 하면 좋을지 슈도코드로 적기

    # 과일 리스트가 있을 때,
    
    # 결과를 저장할 변수를 만들고 초깃값은 0으로 한다
    # 리스트 안에 있는 각 과일에 대해서
    # 이름이 사과이면
    # 결과를 1 증가시킨다

    # 결과 출력

# 직접 만든 코드
#     count = 0
#     for fruit in fruits:
#         if fruit = '사과':
#             count+=1
#     print(count)
#  실패

# 해설 코드
# count = 0                  # 이 부분이 틀렸다! - 전체 줄맞춤을 알맞게 해야함
# for fruit in fruits:
#     if fruit == '사과':     # 이 부분이 틀렸다! - == 이름이 사과이면, True or False 가 나올 수 있도록 bool
#         count+=1
    
# print(count)


# c.f_사과가 아닌 다른 과일에 대해서도 쓸 수 있도록 함수를 만든다

def count_fruits(target):
    count=0
    for fruit in fruits:
        if fruit == target:
            count+=1
    return count

subak_count = count_fruits('수박')
print(subak_count) # 수박의 갯수

gam_count = count_fruits('감')
print(gam_count) # 감의 갯수
