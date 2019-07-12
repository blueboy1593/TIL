"""
Python dictionary 연습 문제
"""

# 1. 평균을 구하시오.
print('==== Q1 ====')
# 아래에 코드를 작성해 주세요.

score = {
    '수학': 80,
    '국어': 90,
    '음악': 100
}
Hab = 0

for value in score.values():
    
    Hab = value + Hab

print(f'평균은 {Hab/3}점 입니다.')
# len(score.values()를 활용)



# 2. 반 평균을 구하시오. -> 전체 평균
print('==== Q2 ====')
# 아래에 코드를 작성해 주세요.
scores = {
    'a': {
        '수학': 80,
        '국어': 90,
        '음악': 100
    },
    'b': {
        '수학': 80,
        '국어': 90,
        '음악': 100
    }
}
aHab = 0
bHab = 0
for value in scores['a'].values():
    
    aHab = value + aHab

for value in scores['b'].values():
    
    bHab = value + bHab

ave = (aHab/3 + bHab/3)/2

print(f'반 평균 점수는 {ave}점 입니다.')



# 3. 도시별 최근 3일의 온도입니다.

# 3-1. 도시별 최근 3일의 온도 평균은?
print('==== Q3-1 ====')
# 아래에 코드를 작성해 주세요.
"""
출력 예시)
서울 : 값
대전 : 값
광주 : 값
부산 : 값
"""

city = {
    '서울': [-6, -10, 5],
    '대전': [-3, -5, 2],
    '광주': [0, -2, 10],
    '부산': [2, -2, 9],
}
for aaa in city:
    dosi = aaa
    sumS = 0
    for value in city[f'{dosi}']:

        sumS = sumS + value
    aveS = sumS/3
    print(f'{dosi}의 평균 온도는 {aveS}도 입니다!')

for key, value in city.items():
    average_temp = sum(value) / len(value)
    print(f'{key} : {average_temp:.1f}')
#.1f를 활용해서 소숫점 첫째 자리까지 출력.

# 3-2. 도시 중에 최근 3일 중에 가장 추웠던 곳, 가장 더웠던 곳은?
print('==== Q3-2 ====')
# 아래에 코드를 작성해 주세요.

city = {
    '서울': [-6, -10, 5],
    '대전': [-3, -5, 2],
    '광주': [0, -2, 10],
    '부산': [2, -2, 9],
}
m = 0
n = 0
maxx = 0
value = 0
for ddd in city:
    dosi = ddd
    for eee in city[f'{dosi}']:
        value = eee
        n = f'{dosi}'
        if maxx < eee:
            maxx = eee
            m = n

print(f'가장 추웠던 곳은 {m} 입니다')
    
city = {
    '서울': [-6, -10, 5],
    '대전': [-3, -5, 2],
    '광주': [0, -2, 10],
    '부산': [2, -2, 9],
}
m = 0
n = 0
maxx = 0
value = 0
for ddd in city:
    dosi = ddd
    for eee in city[f'{dosi}']:
        value = eee
        n = f'{dosi}'
        if maxx > eee:
            maxx = eee
            m = n

print(f'가장 더웠던 곳은 {m} 입니다')


# 3-3. 위에서 서울은 영상 2도였던 적이 있나요?
print('==== Q3-3 ====')
# 아래에 코드를 작성해 주세요.
city = {
    '서울': [-6, -10, 5],
    '대전': [-3, -5, 2],
    '광주': [0, -2, 10],
    '부산': [2, -2, 9],
}
ccc = 0
for bbb in city['서울']:
    if bbb == 2:
        ccc = 1
if ccc == 1:
    print('예 형님')
else:
    print('업읍니당')
    