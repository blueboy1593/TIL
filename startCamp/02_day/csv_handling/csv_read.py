# 1. split이라는 함수 사용
with open('dinner.csv', 'r', encoding='utf-8') as f:
    lines = f.readlines()     #리드라인스로 해야 리스트 형식으로 된다고 하셨당.
    for line in lines:
                                            
        print(line.strip().split(','))      #,기준으로 파일을 스플릿뜨 한다.
#strip을 쓰면 어째서 엔터줄이 사라지는거지?

# 2. csv reader
import csv
with open('dinner.csv', 'r', encoding='utf-8') as f:
    items = csv.reader(f)
    for item in items:
        print(item)
