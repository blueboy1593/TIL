import random

ssafy = {
    'location': ['서울', '대전', '구미', '광주'],
    'language': {
        'python': {
            'python standard library': ['os', 'random', 'webbrowser'],
            'frameworks': {
                'flask': 'micro',
                'django': 'full-functioning'
            },
            'data_science': ['numpy', 'pandas', 'scipy', 'sklearn'],
            'scraping': ['requests', 'bs4'],
        },
        'web' : ['HTML', 'CSS']
    },
    'classes': {
        'dj': {
            'lecturer': 'harry',
            'manager': '노구하',
            'class president': '박나율',
            'groups': {
                'A': ['이길현', '우동균', '이승현', '이가경', '이병재'],
                'B': ['차진권', '박성진', '심규현', '남승현'],
                'C': ['신승호', '조현호', '이병주', '박홍은'],
                'D': ['조규홍', '조수지', '임소희', '이해인'],
                'E': ['박상원', '고병권', '김준호', '신정우', '박나율']
            }
        },
        'gj': {
            'lecturer': 'change',
            'manager': 'pro-gj'
        }
    }
}


"""
난이도* 1. 지역(location)은 몇 개 있나요?
출력예시)
4
"""
print('1번답')
print(len(ssafy['location']))

"""
난이도** 2. python standard library에 'requests'가 있나요?
출력예시)
False
"""
print('2번답')
bb = 0
for aa in ssafy['language']['python']['python standard library']:
    if aa == 'requests':
        bb = 1
        print('네 있습니다.')
if bb == 1:
    print('네 있습니다.')
else:
    print('아니오 없습니다.')

# True False로 구분해서 할 수 있다.
flag = False
for aa in ssafy['language']['python']['python standard library']:
    if aa == 'requests':
        flag = True
print(flag)
print('requests' in ssafy['language']['python']['python standard library'])

"""
난이도** 3. dj 반의 반장의 이름을 출력하세요.
출력예시)
박나율
"""

print('3번답')
print(ssafy['classes']['dj']['class president'])

"""
난이도*** 4. ssafy에서 배우는 언어들을 출력하세요.
출력 예시)
python
web
"""

print('4번답')
for key in ssafy['language'].keys():
    print(key)

"""
난이도*** 5 ssafy gj반의 강사와 매니저의 이름을 출력하세요.
출력 예시)
change
pro-gj
"""

print('5번답')
for value in ssafy['classes']['gj'].values():
    print(value)

"""
난이도***** 6. framework 들의 이름과 설명을 다음과 같이 출력하세요.
출력 예시)
flask는 micro이다.
django는 full-functioning이다.
"""

print('6번답')
for key, value in ssafy['language']['python']['frameworks'].items():
    print(f'{key}는 {value}이다.')

"""
난이도***** 7. 오늘 당번을 뽑기 위해 groups의 E 그룹에서 한명을 랜덤으로 뽑아주세요.
출력예시)
오늘의 당번은 김준호
"""

print('7번답')
ttt = ssafy['classes']['dj']['groups']['E']
rrr = random.choice(ttt)
print(f'오늘의 당번은 {rrr}')

