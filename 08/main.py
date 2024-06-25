from flask import Flask, request, render_template
import random  # ランダムデータ作成のためのライブラリ
from datetime import datetime as dt

app = Flask(__name__)


# 1. プロジェクトのトップ（じゃんけんアプリや、課題のアプリへのリンクを配置するだけ）
@app.route("/")
def index():
    return render_template("index.html")


# 2. じゃんけんアプリの入力フォーム
@app.route("/janken")
def janken():
    # じゃんけんの入力画面のテンプレートを呼び出し
    return render_template("janken_form.html")


@app.route("/janken/play", methods=["POST"])
def janken_play():
    # <input type="text" id="your_name" name="name">
    name = request.form.get("name")
    reception = request.form.get("reception")
    if not name:
        name = "名無しさん"

    # <input type="radio" id="hand_rock" value="rock" name="hand">
    # <input type="radio" id="hand_scissor" value="scissor" name="hand">
    # <input type="radio" id="hand_paper" value="paper" name="hand">
    hand = request.form.get("hand", None)

    # リストの中からランダムに選ぶ
    cpu = random.choice(["rock", "scissor", "paper"])

    if reception:
        win = True
        if hand == "rock":
            cpu = "scissor"
            result_message = "{}の勝ち".format(name)
        elif hand == "scissor":
            cpu = "paper"
            result_message = "{}の勝ち".format(name)
        elif hand == "paper":
            cpu = "rock"
            result_message = "{}の勝ち".format(name)
        else:
            cpu = "scissor"
            result_message = "{}の勝ち".format(name)

    # じゃんけん処理
    elif hand == cpu:
        win = False
        result_message = "あいこ"
    else:
        win = False
        if hand == "rock":
            if cpu == "scissor":
                win = True
                result_message = "{}の勝ち".format(name)
            else:
                result_message = "{}の負け".format(name)
        elif hand == "scissor":
            if cpu == "paper":
                win = True
                result_message = "{}の勝ち".format(name)
            else:
                result_message = "{}の負け".format(name)
        elif hand == "paper":
            if cpu == "rock":
                win = True
                result_message = "{}の勝ち".format(name)
            else:
                result_message = "{}の負け".format(name)
        else:
            result_message = "後出しはダメです。"

    # 渡したいデータを先に定義しておいてもいいし、テンプレートを先に作っておいても良い
    return render_template("janken_play.html", result_message=result_message, name=name, hand=hand, cpu=cpu, win=win)


@app.route("/uranai")
def uranai():
    return render_template("uranai_form.html")


@app.route("/uranai/play", methods=["POST"])
def uranai_play():
    name = request.form.get("name")
    if not name: name = dt #名前が入力されていない場合は、len()でエラーが出るようにした
    dt_now = dt.now()

    try:
        birthday = dt.strptime(request.form.get("birthday"), '%Y-%m-%d')
        date_diff = abs(dt_now - birthday)
        print(date_diff.days)
        amari = (int(date_diff.days) * len(name)) % 5
        result = [5, 1, 3, 2, 4]
    except:
        return render_template("uranai_play.html", result=-1)

    return render_template("uranai_play.html", result=result[amari])


if __name__ == "__main__":
    app.run(host="localhost", port=8888, debug=True)
