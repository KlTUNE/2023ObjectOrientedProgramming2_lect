// データの初期表示
fetch("/address").then(response => {
    console.log(response);
    response.json().then((data) => {
        console.log("----------------");
        console.log(data);  // 取得されたレスポンスデータをデバッグ表示
        console.log("----------------");
        // データを表示させる

        document.querySelector('#error-container').style.display = "none"
        document.querySelector('#message-container').style.display = "none"

        const tableBody = document.querySelector("#address-list > tbody");
        data.forEach(elm => {
            // 1行づつ処理を行う
            let tr = document.createElement('tr');
            // first name
            let td = document.createElement('td');
            td.innerText = elm.first_name;
            tr.appendChild(td);
            // last name
            td = document.createElement('td');
            td.innerText = elm.last_name;
            tr.appendChild(td);
            // email
            td = document.createElement('td');
            td.innerText = elm.email;
            tr.appendChild(td);

            // 1行分をtableタグ内のtbodyへ追加する
            tableBody.appendChild(tr);
        });
    });
});

const btnSerch = document.querySelector("#search-submit");
btnSerch.addEventListener("click", (event) => {
    console.log("検索ボタンが押されました");
    event.preventDefault();

    document.querySelector('#error-container').style.display = "none"
    document.querySelector('#message-container').style.display = "none"

    const params = new URLSearchParams()
    params.set("fn", document.querySelector('#search-firstname').value)
    params.set("ln", document.querySelector('#search-lastname').value)
    params.set("em", document.querySelector('#search-email').value)
    console.log("送信データ:params", params.toString())

    fetch("/address?" + params.toString()).then(response => {
        console.log(response);
        response.json().then((data) => {
            console.log(data);  // 取得されたレスポンスデータをデバッグ表示
            // データを表示させる
            const tableBody = document.querySelector("#address-list > tbody");

            // 子要素を全削除
            while (tableBody.firstChild) {
                tableBody.removeChild(tableBody.firstChild)
            }

            data.forEach(elm => {
                // 1行づつ処理を行う
                let tr = document.createElement('tr');
                // first name
                let td = document.createElement('td');
                td.innerText = elm.first_name;
                tr.appendChild(td);
                // last name
                td = document.createElement('td');
                td.innerText = elm.last_name;
                tr.appendChild(td);
                // email
                td = document.createElement('td');
                td.innerText = elm.email;
                tr.appendChild(td);

                // 1行分をtableタグ内のtbodyへ追加する
                tableBody.appendChild(tr);
            });
        });
    });
})

const btnAdd = document.querySelector("#add-submit");
btnAdd.addEventListener("click", (event) => {
    console.log("追加ボタンが押されました");
    event.preventDefault();

    let fn = document.querySelector('#add-firstname').value
    let ln = document.querySelector('#add-lastname').value
    let em = document.querySelector('#add-email').value

    if (fn == "" || ln == "" || em == "") {
        document.querySelector("#error-container").innerHTML = "未入力の項目があります"
        document.querySelector('#error-container').style.display = "block"
        return
    }

    const formdata = new FormData()
    formdata.append("fn", fn)
    formdata.append("ln", ln)
    formdata.append("em", em)

    fetch("/address", {
        method: "POST",
        body: formdata
    }).then(response => {
        console.log(response);
        response.json().then((data) => {
            console.log(data);  // 取得されたレスポンスデータをデバッグ表示

            document.querySelector('#error-container').style.display = "none"
            document.querySelector('#message-container').style.display = "none"

            if (data.result == "error") {
                document.querySelector("#error-container").innerHTML = "書き込みに失敗しました"
                document.querySelector('#error-container').style.display = "block"
                return
            }
            else if (data.result == "success") {
                document.querySelector("#message-container").innerHTML = "書き込みに成功しました"
                document.querySelector('#message-container').style.display = "block"

                            // データを表示させる
                const tableBody = document.querySelector("#address-list > tbody");

                // 子要素を全削除
                while (tableBody.firstChild) {
                    tableBody.removeChild(tableBody.firstChild)
                }}

                let json_response = data.json_data
                console.log("じぇーそん"+json_response)
                json_response.forEach(elm => {
                    // 1行づつ処理を行う
                    let tr = document.createElement('tr');
                    // first name
                    let td = document.createElement('td');
                    td.innerText = elm.first_name;
                    tr.appendChild(td);
                    // last name
                    td = document.createElement('td');
                    td.innerText = elm.last_name;
                    tr.appendChild(td);
                    // email
                    td = document.createElement('td');
                    td.innerText = elm.email;
                    tr.appendChild(td);

                    // 1行分をtableタグ内のtbodyへ追加する
                    tableBody.appendChild(tr);
                });
            }
        });
    });
})