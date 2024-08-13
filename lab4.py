from flask import Flask, request
import random

app = Flask(__name__)

@app.route('/game', methods=['POST'])
def game():
    player = request.form.get('player')
    computer = random.choice(['剪刀', '石頭', '布', '蜥蜴', '史波克'])
    if player == computer:
        return '平手'
    elif player == '剪刀' and computer == '石頭':
        return '你輸了'
    elif player == '石頭' and computer == '布':
        return '你輸了'
    elif player == '布' and computer == '剪刀':
        return '你輸了'
    elif player == '剪刀' and computer == '蜥蜴':
        return '你贏了'
    elif player == '蜥蜴' and computer == '史波克':
        return '你贏了'
    elif player == '史波克' and computer == '石頭':
        return '你贏了'
    elif player == '石頭' and computer == '蜥蜴':
        return '你贏了'
    else:
        return '輸入錯誤'

if __name__ == '__main__':
    app.run(debug=True)