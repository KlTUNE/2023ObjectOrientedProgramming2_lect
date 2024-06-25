from flask import Flask, request, render_template, jsonify
import json  # Python標準のJSONライブラリを読み込んで、データの保存等に使用する

app = Flask(__name__)
app.config["JSON_AS_ASCII"] = False  # 日本語などのASCII以外の文字列を返したい場合は、こちらを設定しておく


# http://127.0.0.1:5000/address
@app.route('/address', methods=["GET"])
def address_get():

    # 検索パラメータの取得
    p_first_name = request.args.get('fn', None)
    p_last_name = request.args.get('ln', None)
    p_email = request.args.get('em', None)
    # print(p_first_name, p_last_name, p_email)

    with open('address.json') as f:
        json_data = json.load(f)

    print("------------------lllll--")
    print(type(json_data))
    print("--------------------")

    # パラメータにより返すデータをフィルタリングする
    if p_first_name is not None:
        # ラムダにより匿名関数化しているため、分かりづらく見えますが、filter関数には関数を渡す必要があるため、
        # json_dataの中からfirst_name内にパラメータの値が含まれているかどうかを判定する関数を匿名で作成し、
        # それによって得た結果のデータを基にlist生成しています。
        json_data = list(filter(lambda item: p_first_name.lower() in item["first_name"].lower(), json_data))
    if p_last_name is not None:
        json_data = list(filter(lambda item: p_last_name.lower() in item["last_name"].lower(), json_data))
    if p_email is not None:
        json_data = list(filter(lambda item: p_email.lower() in item["email"].lower(), json_data))

    return jsonify(json_data)
    # return render_template("addressbook.html")

@app.route('/address', methods=["POST"])
def address_set():
    p_first_name = request.form.get('fn', None)
    p_last_name = request.form.get('ln', None)
    p_email = request.form.get('em', None)

    data = {
        "first_name": p_first_name,
        "last_name": p_last_name,
        "email": p_email
    }

    with open('address.json') as f:
        json_data = json.load(f)

    try:
        json_data.append(data)
        with open('address.json', 'w') as f:
            json.dump(json_data, f, indent = 4)
    except:
        return jsonify({"result": "error"})

    with open('address.json') as f:
        json_data = json.load(f)
    return jsonify({"result": "success", "json_data": json_data})

# http://127.0.0.1:5000/
@app.route('/')
def index():
    return render_template("addressbook.html")


if __name__ == "__main__":
    # debugモードが不要の場合は、debug=Trueを消してください
    app.run(debug=True)