from flask import Flask
import datetime
import random
#import hello
#print(hello.message)
app = Flask(__name__)

@app.route("/") # endpoint 어디로 갔을때 어떤 화면을 보여줘
def hello():
    return "Hello KangHyun!"


@app.route('/ssafy')
def ssafy(): #함수 이름은 무엇이던 상관없어요. 다른 함수랑 이름이 겹치지 않도록
    return 'Hello SSAFY'

@app.route('/dday')
def dday():
    today = datetime.datetime.now()
    b_day = datetime.datetime(2019, 11, 11)
    td = b_day - today
    return f'{td.days} 일 남았습니다!!'

@app.route('/html')
def html():
    return '<h1> This is HTML h1 tan!</h1>'

@app.route('/html_lines')
def html_lines():
    return '''
    <h1>여러줄을 보내봅시다.</h1>
    <ul>
        <li>1번</li>
        <li>2번</li>
    </ul>
    '''

@app.route('/greeting/<name>')
def greeting(name): #name == IU
    return f'반갑습니다! {name} 님!'
    #동적으로 url에서 변수를 받을 수 있게 되었다.

# @app.route('/cube/<int:num>') # int를 통해 number를 정의해준다.
# def cube(num):
#     return f'{num}의 3제곱은 {num ** 3}입니다!!'   #**는 몇의 몇승 이라는 의미

#실습 메뉴가 여러개 있을때 랜덤으로 사람 수만큼 메뉴를 뽑아서 반환해서 보여주기.
@app.route('/lunch/<int:people>')
def lunch(people):
    menu = ['짜장', '짬뽕', '라면', '김밥', '커피', '단무지', '콩', '햇반', '연어', '등심']
    order = random.sample(menu, people)
    return str(order)

if __name__ == '__main__': # 
    app.run(debug=True)
