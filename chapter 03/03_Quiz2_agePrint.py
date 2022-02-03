# Q2. 사람의 나이 출력하기

# 데이터 살펴보기. 사람과 이름의 나이를 출력
people = [
    {'name': 'bob', 'age': 20},
    {'name': 'carry', 'age': 38},
    {'name': 'john', 'age': 7},
    {'name': 'smith', 'age': 17},
    {'name': 'ben', 'age': 27},
]

# for person in people:
#     print(person['name'],person['age'])

# bob의 나이를 출력하는 알고리즘을 슈도코드로 작성

    # 사람 정보가 담긴 리스트가 있을 때,

    # 리스트 안의 딕셔너리인 각 사람에 대해서
    # 만약 사람의 이름이 'bob'이라면
    # 그 사람의 나이를 출력해라

# for isBob in people:
#     if isBob['name'] == 'bob':
#         print(isBob['age'])

# 다른 사람의 이름을 넣는 함수

def get_age(myname):
    for person in people:
        if person['name'] == myname:
            return person['age']
    return '해당하는 이름이 없습니다'

print(get_age('bob'))
print(get_age('kay'))