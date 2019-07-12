from flask import Flask, render_template, request # 사용자의 요청을 확인할 수 있음.
import requests
app = Flask(__name__)

@app.route('/') # / => root
def index():
    return '반갑습니다'


@app.route('/greeting/<string:name>')
def greeting(name):
    return render_template('greeting.html', newname=name)    #어제 했는데 기억이 안나냐 ㅋㅋㅋ


@app.route('/ping')
def ping():
    return render_template('ping.html')


@app.route('/pong')
def pong():
    age = request.args.get('age')   #age의 변수를 대답받는 내용.
    return f'Pong! age: {age}'
    #render_template('pong.html')


@app.route('/google')
def google():
    return render_template('google.html')


@app.route('/naver')
def naver():
    return render_template('naver.html')


@app.route('/ascii_input')
def ascii_input():  # 사용자가 입력할 수 있는 페이지를 만들겠다는 것.
    return render_template('ascii_input.html')


@app.route('/ascii_result')
def ascii_result():
    text = request.args.get('text')
    # Ascii Art API를 활용해서 사용자의 input 값을 변경한다.
    response = requests.get(f'http://artii.herokuapp.com/make?text={text}')
    result = response.text
    return render_template('ascii_result.html', result=result)


@app.route('/lotto_input')
def lotto_input():
    # 사용자가 입력할 수 있는 페이지만 전달.
    return render_template('lotto_input.html')


@app.route('/lotto_result')
def lotto_result():
    # 사용자 입력 값 받기
    lotto_round = request.args.get("round")
    lotto_numbers = request.args.get("numbers").split() # 이 함수를 list로 만들어줘야 한다.

    # 로또 실제 당첨번호 확인
    url = f'https://dhlottery.co.kr/common.do?method=getLottoNumber&drwNo={lotto_round}'
    response = requests.get(url)
    lotto_info = response.json() # json 타입의 파일을 python dictionary로 parsing 해줘. json 타입의 파일은 따로 다운받지 않아도 되는 형식인가보다!!!
    print(lotto_info)
    lotto_temp = [str(lotto_info['drwtNo1']), str(lotto_info['drwtNo2']), str(lotto_info['drwtNo3']), str(lotto_info['drwtNo4']), str(lotto_info['drwtNo5']), str(lotto_info['drwtNo6'])]
    lotto_bonus = [str(lotto_info['bnusNo'])]
    print(lotto_temp)

    n = 0
    m = 0
    compare = False
    for i in lotto_numbers:
        compare = f'{i}' in lotto_temp
        print(compare)
        if compare == True:
            n = n + 1
    print(n)

    bonus = False
    for i in lotto_numbers:
        bonus = f'{i}' in lotto_bonus
        print(bonus)
        if bonus == True:
            m = m + 1
    print(m)

    if n == 6:
        result = '1등 당첨입니다! 추카추카'
    elif n == 5:
        if m == 1:
            result = '2등 당첨이네요~ 저도 좀 주세요'
        else:
            result = '3등 당첨. 100만원 개꿀'
    elif n == 4:
        result = '4등 당첨. 10만원 받아가세요.'
    elif n == 3:
        result = '5등 당첨. 5천원으로 한번 더!'
    else:
        result = '꽝. 다음 기회에.'

    return f'회차는 {lotto_round}\n 구매하신 숫자는...{lotto_numbers}\n 해당 회차의 당첨번호는{lotto_temp}\n 그리고 2등을 위한 보너스 숫자는 {lotto_bonus}입니다 \n  숫자 확인 결과....두근두근 {result}'

        # 번호 교집합 개수 찾기
        # if len(lotto_numbers) == 6: # 사용자의 input이 6개의 숫자가 맞는지 확인을 해줘야 한다.
        #     matched = 0
        #     for 



if __name__ == '__main__': 
    app.run(debug=True)
