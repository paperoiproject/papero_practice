import sys
from flask import Flask, request, jsonify
from flask_cors import CORS

import time

import pypapero
papero = pypapero.Papero("", "", "ws://192.168.1.1:8088/papero")

app = Flask(__name__)
CORS(app)

def timeKeep(x):
    t1 = time.time();
    t2 = time.time();
    while t2 - t1 < x:
        t2 = time.time();

def my_funcA(papero, text):
    papero.send_move_head(["A0T500L", "A15T500L", "A0T500L", "A15T500L"],["A0T500L"])
    papero.send_turn_led_on("cheek", ["R3R3", "2", "R3R3", "2", "R3R3", "2", "R3R3", "2", "R3R3", "2", "R3R3", "2", "R3R3", "2", "R3R3", "2", "R3R3", "2", "R3R3", "2"])
    papero.send_start_speech(text)
    timeKeep(2.5);

def my_funcB(papero, text):
    papero.send_move_head(["A15T500L"],["A-30T1000L", "A30T1000L", "A-30T1000L", "A30T1000L", "A0T1000L", "A0T500L"])
    papero.send_start_speech(text)
    timeKeep(2.3);
def my_funcC(papero, text):
    papero.send_move_head(["A15T500L", "R0T300L","R0T500L","R0T300L","R0T1000L","R0T300L","R0T500L","R0T300L","A15T500L"],["A-20T500L", "R0T300L","A-40T500L","R0T300L","A20T1000L","R0T300L","A40T500L","R0T300L","A0T500L"])
    papero.send_turn_led_on("cheek", ["R3R3", "2", "R3R3", "2", "R3R3", "2", "R3R3", "2", "R3R3", "2", "R3R3", "2", "R3R3", "2", "R3R3", "2", "R3R3", "2", "R3R3", "2", "R3R3", "2", "R3R3", "2", "R3R3", "2", "R3R3", "2", "R3R3", "2", "R3R3", "2", "R3R3", "2", "R3R3", "2", "R3R3", "2", "R3R3", "2", "R3R3", "2", "R3R3", "2"])
    papero.send_start_speech(text)
    timeKeep(4.2)
def my_funcD(papero, text):
    papero.send_move_head(["A15T2000M", "A19T1000L", "A11T500L", "A19T500L", "A19T500L", "R0T1000L", "A23T500L", "A11T500L", "A19T500L", "A15T1000L"],
                        ["A0T2000M", "A-46T1000L", "R0T1500L", "A40T1000L", "R0T1500L", "A0T1000L"])
    papero.send_turn_led_on("ear",
                        ["W3W3", "5", "NN", "5", "W3W3", "5", "NN", "5", "NN", "60"])
    papero.send_turn_led_on("cheek",
                        ["NN", "20", "NN", "60", "R3R3", "5", "R3R3", "5"])
    papero.send_start_speech(text)
    timeKeep(9)
def my_funcE(papero, text):
    papero.send_move_head(["A15T1800M", "A-15T1000L", "A0T1000L", "A-15T1000L", "A15T1000L"],
                        ["A0T1800M", "R0T4000L"])
    papero.send_turn_led_on("cheek",
                        ["NN", "18","R3R3","10","NN","10","R3R3","10","NN","10"])
    papero.send_turn_led_on("mouth",
                        ["NNR3R3R3R3R3NN", "2", "R3R3R3R3R3R3R3R3R3", "2", "NNR3R3R3R3R3NN", "2", "NNNR3R3R3NNN", "2", "NNR3R3R3R3R3NN", "2", "NR3R3R3R3R3R3R3N", "2", "R3R3R3R3R3R3R3R3R3", "2", "NNR3R3R3R3R3NN", "2", "NNNR3R3R3NNN", "2"])
    papero.send_start_speech(text)
    timeKeep(5.6)

def my_funcF(papero, text):#右を向く #マイナスが右
    papero.send_move_head(["A25T500L", "R0T3000L","A15T500L"],#縦の動き
                          ["A-30T500L", "R0T3000L","A0T500L"])#横の動き
    papero.send_start_speech(text)
    timeKeep(4)
def my_funcG(papero, text):#左を向く #プラスを左
    papero.send_move_head(["A25T500L", "R0T3000L","A15T500L"],#縦の動き
                          ["A30T500L", "R0T3000L","A0T500L"])#横の動き
    papero.send_start_speech(text)
    timeKeep(4)
def my_funcH(papero, text):#上を向く
    papero.send_move_head(["A25T500L","R0T3000L","A15T500L"],#縦の動き
                          ["A0T500L", "R0T3000L","A0T500L"])#横の動き
    papero.send_start_speech(text)
    timeKeep(4)

def my_funcI(papero, text):#下を向く
    papero.send_move_head(["A-15T500L", "R0T3000L","A15T500L"],#縦の動き
                          ["A0T500L", "R0T3000L","A0T500L"])#横の動き
    papero.send_start_speech(text)
    timeKeep(4)

def my_funcEnd(papero, text):
    papero.send_move_head(["A15T500L"], ["A0T500L"])

def my_funcZ(papero):#下を向く
    papero.papero_cleanup()

def my_funcAlf(papero, c, text):
    if c == '1':
        my_funcA(papero, text)
    if c == '2':
        my_funcB(papero, text)
    if c == '3':
        my_funcC(papero, text)
    if c == '4':
        my_funcD(papero, text)
    if c == '5':
        my_funcE(papero, text)
    if c == '6':
        my_funcF(papero, text)
    if c == '7':
        my_funcG(papero, text)
    if c == '8':
        my_funcH(papero, text)
    if c == '9':
        my_funcI(papero, text)
    if c == 'E':
        my_funcEnd(papero, text)
    if c == 'Z':
        my_funcZ(papero, text)

@app.route("/", methods=["GET", "POST"])
def test():
    if request.method == "GET":
        return "aaaaa"
    else:
        print("post")
        post_data = request.get_json()
        print(post_data)
        post_data.append({'act': 'E', 'text': ''})
        for v in post_data:
            my_funcAlf(papero, v['act'], v['text'])
        return jsonify({"state": "End"})

@app.route("/command/<command>", methods=["GET", "POST"])
def command(command):
    if request.method == "GET":
        my_funcAlf(papero, command)
        return command
    else:
        print("post")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080, threaded=True)



















