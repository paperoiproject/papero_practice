# -*- coding:utf-8 -*-
from logging import basicConfig, DEBUG
basicConfig(level=DEBUG)




import sys

import pypapero

def my_funcB(papero):
    papero.send_move_head(["A-15T200L", "A15T500L", "A-15T500L", "A15T500L", "A0T300L", "A0T500L"],["A0T200L", "R0T1800L", "A0T500L"])
    papero.send_turn_led_on("cheek", ["R3R3", "2", "R3R3", "2", "R3R3", "2", "R3R3", "2", "R3R3", "2", "R3R3", "2", "R3R3", "2", "R3R3", "2", "R3R3", "2", "R3R3", "2"])
    papero.send_start_speech('びー')



def my_func(papero):
    papero.send_turn_led_on("mouth",
                            ["NNNG3G3G3NNN", "2", "NNG3NG3NG3NN", "2", "G3NG3NG3NG3NG3", "2", "G3NG3NG3NG3NG3", "2", "NG3G3G3G3G3G3G3N", "2"])
    papero.send_start_speech('こんにちは', "0", "3", "100", "100","100", "1000", "1000", "0", "higher")


if __name__ == "__main__":
    papero = pypapero.Papero("", "", "ws://192.168.1.1:8088/papero")
    if papero.errOccurred == 0:
        my_func(papero)
        cnt = 0
        while cnt < 2:
            messages = papero.papero_robot_message_recv(1.0)
            if messages is not None:
                cnt += 1
    papero.papero_cleanup()
