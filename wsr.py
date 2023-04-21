from flask import Flask, render_template, request
import speech_recognition as sr
import pyautogui
import requests
import os

app = Flask(__name__)

url0 = "https://sgp1.blynk.cloud/external/api/update?token=rAG4ADhrMioce3oAk8IdiVXMcqmoMvQl&V0="
url1 = "https://sgp1.blynk.cloud/external/api/update?token=rAG4ADhrMioce3oAk8IdiVXMcqmoMvQl&V1="
url2 = "https://sgp1.blynk.cloud/external/api/update?token=rAG4ADhrMioce3oAk8IdiVXMcqmoMvQl&V2="

# thiet lap tham so chunk_duration
chunk_duration = 5 # thoi gian moi chunk(giay)

record_duration = 5 # thoi gian ghi am(giay)

@app.route("/")
def index():
    return render_template("b.html")

@app.route('/bat_den')
def bat_den():
    url = url0 + "1"
    requests.get(url)
    pyautogui.press('q')
    return "Đèn đã được bật"

@app.route('/tat_den')
def tat_den():
    url = url0 + "0"
    requests.get(url)
    pyautogui.press('q')
    return "Đèn đã được tắt"

@app.route('/mo_cua')
def mo_cua():
    url = url1 + "1"
    requests.get(url)
    pyautogui.press('q')
    return "Cửa đã được mở"

@app.route('/dong_cua')
def dong_cua():
    url = url1 + "0"
    requests.get(url)
    pyautogui.press('q')
    return "Cửa đã được đóng"

@app.route('/nhap_lenh', methods=['POST'])
def nhap_lenh():
    text = request.form['text-input']
    file = open('voice.txt','a+',encoding='utf-8')
    file.write(text)
    if 'bật đèn' in text:
        return bat_den()
    elif 'tắt đèn' in text:
        return tat_den()
    elif 'mở cửa' in text:
        return mo_cua()
    elif 'đóng cửa' in text:
        return dong_cua()
    else:
        message = "Không tìm thấy lệnh"
        return render_template('a.html', message=message)
    # r = sr.Recognizer()
    # audio_file = request.files["audio"]
    # audio_file.save("name.wav")
    # # test_file = audio_file
    # audio_data = b''
    # chunk_size = 4096 # adjust this to your needs
    # audio_format = mimetypes.guess_extension(audio_file.content_type)

    # while True:
    #     chunk = audio_file.read(chunk_size)
    #     if not chunk:
    #         break
    #     audio_data += chunk
    # audio = sr.AudioData(audio_data, sample_rate=16000, sample_width=2)
    # print(audio)

    # print(f"Received audio file: {audio_file.filename}")
    # print(f"Received audio file in {audio_format} format.")
    # print(f"Audio data length: {len(audio_data)} bytes")
    
    # with sr.AudioFile('myFile.wav') as source:
    # # Thu âm nguồn từ microphone hoặc tệp
    #     audio_text = r.listen(source)
    #     print(audio_text)
    #     try:
    #         text = r.recognize_google(audio_text, language="vi-VN")
    #         file = open("voice.txt", "w", encoding="utf-8")
    #         file.write(text)
    #         file.close()
    #         if 'stop' in text:
    #             return bat_den()
    #         elif 'tắt đèn' in text:
    #             return tat_den()
    #         elif 'mở cửa' in text:
    #             return mo_cua()
    #         elif 'đóng cửa' in text:
    #             return dong_cua()
    #         else:
    #             message = "Không tìm thấy lệnh"
    #             return render_template('a.html', message=message)
    #     except sr.UnknownValueError:
    #         message = "Không nhận dạng được giọng nói"
    #         return "Không nhận dạng được giọng nói"
    
if __name__ == '__main__':
    
    app.run(debug=True, port=8080)