from flask import Flask, render_template, request
import datetime
import requests

app = Flask(__name__)

den1 = "https://sgp1.blynk.cloud/external/api/update?token=rAG4ADhrMioce3oAk8IdiVXMcqmoMvQl&V0="
den2 = "https://sgp1.blynk.cloud/external/api/update?token=rAG4ADhrMioce3oAk8IdiVXMcqmoMvQl&V3="
quat0 = "https://sgp1.blynk.cloud/external/api/update?token=rAG4ADhrMioce3oAk8IdiVXMcqmoMvQl&V1="
quat1 = "https://sgp1.blynk.cloud/external/api/update?token=rAG4ADhrMioce3oAk8IdiVXMcqmoMvQl&V4="
quat2 = "https://sgp1.blynk.cloud/external/api/update?token=rAG4ADhrMioce3oAk8IdiVXMcqmoMvQl&V5="
quat3 = "https://sgp1.blynk.cloud/external/api/update?token=rAG4ADhrMioce3oAk8IdiVXMcqmoMvQl&V6="
cauDao = "https://sgp1.blynk.cloud/external/api/update?token=rAG4ADhrMioce3oAk8IdiVXMcqmoMvQl&V7="
cua = "https://sgp1.blynk.cloud/external/api/update?token=rAG4ADhrMioce3oAk8IdiVXMcqmoMvQl&V2="

@app.route("/")
def index():
    return render_template("b.html")

@app.route("/mo_cau_dao")
def mo_cau_dao():
    url = cauDao + "1"
    requests.get(url)
    return  " "

@app.route("/dong_cau_dao")
def dong_cau_dao():
    url = cauDao + "0"
    requests.get(url)
    return  " "

@app.route("/bat_quat")
def bat_quat():
    url = quat0 + "1"
    requests.get(url)
    return " "

@app.route("/tat_quat")
def tat_quat():
    url = quat0 + "0"
    requests.get(url)
    return " "

@app.route("/nac_1")
def nac_1():
    url = quat1 + "1"
    requests.get(url)
    return " "

@app.route("/tat_nac_1")
def tat_nac_1():
    url = quat1 + "0"
    requests.get(url)
    return " "

@app.route("/nac_2")
def nac_2():
    url = quat2 + "1"
    requests.get(url)
    return " "

@app.route("/tat_nac_2")
def tat_nac_2():
    url = quat2 + "0"
    requests.get(url)
    return " "

@app.route("/nac_3")
def nac_3():
    url = quat3 + "1"
    requests.get(url)
    return " "

@app.route("/tat_nac_3")
def tat_nac_3():
    url = quat3 + "0"
    requests.get(url)
    return " "

@app.route('/bat_den1')
def bat_den1():
    url = den1 + "1"
    requests.get(url)
    return "Đèn 1 đã được bật"

@app.route('/tat_den1')
def tat_den1():
    url = den1 + "0"
    requests.get(url)
    return "Đèn 1 đã được tắt"

@app.route('/bat_den2')
def bat_den2():
    url = den2 + "1"
    requests.get(url)
    return "Đèn 2 đã được bật"

@app.route('/tat_den2')
def tat_den2():
    url = den2 + "0"
    requests.get(url)
    return "Đèn 2 đã được tắt"

@app.route('/mo_cua')
def mo_cua():
    url = cua + "1"
    requests.get(url)
    return "Cửa đã được mở"

@app.route('/dong_cua')
def dong_cua():
    url = cua + "0"
    requests.get(url)
    return "Cửa đã được đóng"

@app.route('/nhap_lenh', methods=['POST'])
def nhap_lenh():
    text = request.form['text-input']
    file = open('voice.txt','a+',encoding='utf-8')

    current_time = datetime.datetime.now()
    formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")

    file.write(formatted_time + " - " + text + "\n")
    file.close()
    if 'bật đèn 1' in text:
        return bat_den1()
    elif 'tắt đèn 1' in text:
        return tat_den1()
    elif 'mở cửa' in text:
        return mo_cua()
    elif 'đóng cửa' in text:
        return dong_cua()
    elif 'bật đèn 2' in text:
        return bat_den2()
    elif 'tắt đèn 2' in text:
        return tat_den2()
    elif 'bật quạt' in text:
        return bat_quat()
    elif 'tắt quạt' in text:
        return tat_quat()
    elif 'quạt nấc 1' in text:
        return nac_1()
    elif 'tắt nấc 1' in text:
        return tat_nac_1()
    elif 'quạt nấc 2' in text:
        return nac_2()
    elif 'tắt nấc 2' in text:
        return tat_nac_2()
    elif 'quạt nấc 3' in text:
        return nac_3()
    elif 'tắt nấc 3' in text:
        return tat_nac_3()
    elif 'mở cầu dao' in text:
        return mo_cau_dao()
    elif 'đóng cầu dao' in text:
        return dong_cau_dao()
    
    else:
        message = "Không tìm thấy lệnh"
        return render_template('a.html', message=message)

    
if __name__ == '__main__':
    
    app.run(debug=True, port=8080)