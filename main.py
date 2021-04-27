#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

class Trading:
    _input_str = ""
    _settings_array = dict()
    _current_stack = 0
    _timebank = 0
    _BTC_ETH_array = [{}]
    _USDT_ETH_array = [{}]
    _USDT_BTC_array = [{}]


    def get_input(self):
        self._input_str = input()

    def get_settings(self):
        for i in range(10):
            self.get_input()
            print("le input str :" + self._input_str, file=sys.stderr)
            array = self._input_str.split(" ")
            if (len(array) < 3):
                print("settings pas bon", file=sys.stderr)
                exit(84);
            # if (array[0] != "settings") break;
            self._settings_array[array[1]] = array[2]
            print("self._settings_array[1] :" + self._settings_array[array[1]], file=sys.stderr)

            # print("le amount askip : " + self._settings_array[array[9]], file=sys.stderr)
        


    def set_settings(self):
        self._timebank = int(self._settings_array["timebank"])
        self._current_stack = int(self._settings_array["initial_stack"])
        
        print("current timebank: " + str(self._timebank), file=sys.stderr);
        print("current stack: " + str(self._current_stack), file=sys.stderr);


    def next_candles(self, input_str):
        print("l(input candle) =" + input_str, file=sys.stderr)
        array = input_str.split(";")
        for i in array:
            splited_str = i.split(",")
            if (splited_str[0] == "BTC_ETH"):
                print("BTC_ETH !!!", file=sys.stderr)
                self._BTC_ETH_array[-1]["date"] = float(splited_str[1])
                self._BTC_ETH_array[-1]["high"] = float(splited_str[2])
                self._BTC_ETH_array[-1]["low"] = float(splited_str[3])
                self._BTC_ETH_array[-1]["open"] = float(splited_str[4])
                self._BTC_ETH_array[-1]["close"] = float(splited_str[5])
                self._BTC_ETH_array[-1]["volume"] = float(splited_str[6])
                # print(self._BTC_ETH_array[-1], file=sys.stderr)
                # print(self._BTC_ETH_array[0], file=sys.stderr)

            # if (splited_str[0] == "USDT_BTC"):
            #     print("USDT_BTC !!", file=sys.stderr)
            # if (splited_str[0] == "USDT_ETH"):
            #     print("USDT_ETH !", file=sys.stderr)

    def buy_crypto(self, currency, amount):
        self._current_stack = self._current_stack / 2
        print("buy USDT_BTC 0.001")

    def sell_crypto(self, currency, amount):
        print("sell USDT_BTC 0.001")



    def loop(self):
        i = 0
        while True:
            self.get_input()
            array = self._input_str.split(" ")
            if (array[0] == "update"):
                if (array[1] == "game"):
                    if (array[2] == "next_candles"):
                        self.next_candles(array[3])

                    # else if (array[2] == "stacks"):

            print("buy USDT_BTC 0.002")
            # print("buy BTC_ETH 0.000001")
            i += 1
            # print("le int i =" + str(i), file=sys.stderr)


    def entrypoint(self):
        self.get_settings()
        self.set_settings()
        self.loop()



def main():
    trade = Trading()
    trade.entrypoint()

if __name__ == '__main__':
    main()
