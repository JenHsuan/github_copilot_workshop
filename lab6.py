from flask import Flask, request  # 引入 Flask 和 request
import random  # 引入 random 模組

app = Flask(__name__)  # 創建一個新的 Flask 應用

@app.route('/game', methods=['POST'])  # 定義一個 POST 路由 /game
def game():
  player = request.form.get('player')  # 從表單數據中獲取 player 參數
  computer = random.choice(['剪刀', '石頭', '布', '蜥蜴', '史波克'])  # 電腦隨機選擇一個選項
  if player == computer:  # 如果玩家和電腦選擇相同
      return '平手'  # 返回 "平手"
  elif player == '剪刀' and computer == '石頭':  # 如果玩家選擇 "剪刀" 且電腦選擇 "石頭"
      return '你輸了'  # 返回 "你輸了"
  elif player == '石頭' and computer == '布':  # 如果玩家選擇 "石頭" 且電腦選擇 "布"
      return '你輸了'  # 返回 "你輸了"
  elif player == '布' and computer == '剪刀':  # 如果玩家選擇 "布" 且電腦選擇 "剪刀"
      return '你輸了'  # 返回 "你輸了"
  elif player == '剪刀' and computer == '蜥蜴':  # 如果玩家選擇 "剪刀" 且電腦選擇 "蜥蜴"
      return '你贏了'  # 返回 "你贏了"
  elif player == '蜥蜴' and computer == '史波克':  # 如果玩家選擇 "蜥蜴" 且電腦選擇 "史波克"
      return '你贏了'  # 返回 "你贏了"
  elif player == '史波克' and computer == '石頭':  # 如果玩家選擇 "史波克" 且電腦選擇 "石頭"
      return '你贏了'  # 返回 "你贏了"
  elif player == '石頭' and computer == '蜥蜴':  # 如果玩家選擇 "石頭" 且電腦選擇 "蜥蜴"
      return '你贏了'  # 返回 "你贏了"
  else:  # 如果玩家選擇的不是有效選項
      return '輸入錯誤'  # 返回 "輸入錯誤"

if __name__ == '__main__':  # 如果這個檔案是直接執行的，而不是被導入的
  app.run(debug=True)  # 啟動 Flask 應用，並開啟 debug 模式