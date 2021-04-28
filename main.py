#!/usr/bin/env python3
# -*- coding: utf-8 -*-

        # if os.path.isfile(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'values.txt')):
        #     os.remove(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'values.txt'))
        # labels = [
        #     "date",
        #     "high",
        #     "low",
        #     "open",
        #     "close",
        #     "volume",
        # ]
        # arr_len = len(self._BTC_ETH_array)
        # for i in range(arr_len):
        #     try:
        #         ts = int(self._BTC_ETH_array[i]["date"])
        #         readable = datetime.datetime.fromtimestamp(ts).isoformat()
        #         with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), "values.txt"), "a") as value_file:
        #             value_file.write(f"\nIndex {i} - Date: {readable}\n")
        #     except KeyError:
        #         with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), "values.txt"), "a") as value_file:
        #             value_file.write(f"\nIndex {i} - Date: N/A\n")
        #     for label in labels:
        #         try:
        #             with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), "values.txt"), 'a') as value_file:
        #                 value_file.write(f"self._BTC_ETH_array[{i}][{label}]: {self._BTC_ETH_array[i][label]}\n")
        #             # print(f"self._BTC_ETH_array[{i}][{label}]: {self._BTC_ETH_array[i][label]}", file=sys.stderr)
        #         except KeyError:
        #             pass

import sys
import os
import datetime
import statistics


class Trading:
    _input_str = ""
    _settings_array = dict()
    _current_stack = 0
    _timebank = 0
    _test = 0
    _BTC_stack = 0
    _ETH_stack = 0
    _USDT_stack = 0
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
            # print("self._settings_array[1] :" + self._settings_array[array[1]], file=sys.stderr)

        


    def set_settings(self):
        self._timebank = int(self._settings_array["timebank"])
        self._current_stack = int(self._settings_array["initial_stack"])



    def next_candles(self, input_str):
        # print("l(input candle) =" + input_str, file=sys.stderr)
        array = input_str.split(";")
        for i in array:
            splited_str = i.split(",")
            if (splited_str[0] == "BTC_ETH"):
                # print("BTC_ETH !!!", file=sys.stderr)
                self._BTC_ETH_array.append({
                    'date': float(splited_str[1]),
                    'high': float(splited_str[2]),
                    'low': float(splited_str[3]),
                    'open': float(splited_str[4]),
                    'close': float(splited_str[5]),
                    'volume': float(splited_str[6]),
                })


            if (splited_str[0] == "USDT_BTC"):
                self._USDT_BTC_array.append({
                    'date': float(splited_str[1]),
                    'high': float(splited_str[2]),
                    'low': float(splited_str[3]),
                    'open': float(splited_str[4]),
                    'close': float(splited_str[5]),
                    'volume': float(splited_str[6]),
                })

            if (splited_str[0] == "USDT_ETH"):
                self._USDT_ETH_array.append({
                    'date': float(splited_str[1]),
                    'high': float(splited_str[2]),
                    'low': float(splited_str[3]),
                    'open': float(splited_str[4]),
                    'close': float(splited_str[5]),
                    'volume': float(splited_str[6]),
                })

    def buy_crypto(self, currency, amount, stack):
        # print("SEND: buy USDT_BTC {0}".format(self._current_stack), file=sys.stderr)
        if stack > amount:
            print(f'buy {currency} {amount}')

    def sell_crypto(self, currency, amount):
        print("sell USDT_BTC 0.001")

    def find_average(self, array):
        tmp_list = []
        for x in array:
            if x.get('close') is not None:
                tmp_list.append(x.get('close'))
        return sum(tmp_list) / len(tmp_list)

    def buy_or_sell(self):
        avg_USDT_BTC = self.find_average(self._USDT_BTC_array)
        avg_USDT_ETH = self.find_average(self._USDT_ETH_array)
        avg_BTC_ETH = self.find_average(self._BTC_ETH_array)


        try:

            if (avg_USDT_BTC > self._USDT_BTC_array[-1]["close"] and self._current_stack > 0.0001):
                self.buy_crypto("USDT_BTC", 0.001, self._USDT_stack)

            elif(avg_USDT_ETH > self._USDT_ETH_array[-1]["close"] and self._current_stack > 0.0001):
                self.buy_crypto("USDT_ETH", 0.001, self._USDT_stack)

            elif(avg_BTC_ETH > self._USDT_ETH_array[-1]["close"] and self._current_stack > 0.0001):
                self.buy_crypto("BTC_ETH", 0.001, self._BTC_stack)

            else:
                print("pass")

        except KeyError:
            pass



    def current_stack(self, string):
        array = string.split(",")
        for i in array:
            splited_str = i.split(":")
            if (splited_str[0] == "BTC"):
                self._BTC_stack = float(splited_str[1])
            elif (splited_str[0] == "ETH"):
                self._ETH_stack = float(splited_str[1])
            elif (splited_str[0] == "USDT"):
                self._USDT_stack = float(splited_str[1])
            else:
                exit(84)
            print("fucking " + splited_str[0] + " stacks : " + splited_str[1], file=sys.stderr)

    def loop(self):
        i = 0
        while True:
            self.get_input()
            array = self._input_str.split(" ")
            if (array[0] == "update"):
                if (array[1] == "game"):
                    if (array[2] == "next_candles"):
                        self.next_candles(array[3])
                    elif (array[2] == "stacks"):
                        self.current_stack(array[3])

            elif (array[0] == "action" and array[1] == "order"):
                self.buy_or_sell()
            else :
                print("caca pas bon", file=sys.stderr)

            # print("buy USDT_BTC 0.002")
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
