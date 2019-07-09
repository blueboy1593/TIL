dinner = {
    '양자강' : '02-557-4211', #차돌짬뽕
    '김밥카페' : '02-553-3181', #라돈
    '순남시래기' : '02-508-0887', #보쌈정식
}
#print(dinner.items())
#print(dinner.keys())
#print(dinner.values())

# 1. String formatting 파일을 하나 새롭게 만들어서
with open('dinner.csv', 'w', encoding='utf-8') as f: # 한글으로 인코딩 하는거라 utf-8이라고 주는듯 합니다.
    for item in dinner.items(): # [['양자강', '02-557-4221'],['김밥카페-------]] 딕셔너리를 for문으로 돌게 하기 위해서 이렇게 하는것.
        f.write(f'{item[0]},{item[1]}\n')

# 2. csv.writer를 사용하는 방법
import csv
with open('dinner.csv', 'w', encoding='utf-8', newline='') as f:
    csv_writer = csv.writer(f) # f라는 파일에 csv를 작성하는 객체를 생성
    for item in dinner.items():
        csv_writer.writerow(item) #윈도우 환경에서는 한줄씩 추가된다고 생각하고 있으면 된답니다. newline이라는 용어를 사용해서 한줄만 띄도록 고정시켜버리기
