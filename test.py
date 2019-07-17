# -*- coding:utf-8 -*-
from logging import basicConfig, DEBUG
basicConfig(level=DEBUG)

import sys

import pypapero

def my_func(papero):
    papero.send_move_head(["A-15T1000L", "A0T1000L"],
                          ["A0T1000L", "R0T1000L"])
    papero.send_turn_led_on("mouth",
                            ["NNNG3G3G3NNN", "2", "NNG3NG3NG3NN", "2", "G3NG3NG3NG3NG3", "2", "G3NG3NG3NG3NG3", "2", "NG3G3G3G3G3G3G3N", "2", "NNNG3G3G3NNN", "2"])
    papero.send_start_speech('おつかれさまです')

if __name__ == "__main__":
    papero = pypapero.Papero("", "", "ws://192.168.1.1:8088/papero")
    if papero.errOccurred == 0:
        while True:
            messages = papero.papero_robot_message_recv(1.0)
            if (messages is not None) and (messages[0]["Name"] == "detectButton"):
                if messages[0]["Status"]=="C":
                    my_func(papero)
                else:
                    break;
    papero.papero_cleanup()

