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
import math


class Trading:
    _input_str = ""
    _settings_array = dict()
    _current_stack = 0
    _timebank = 0
    _test = 0
    _candles_given = 0
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
                exit(84)
            # if (array[0] != "settings") break;
            self._settings_array[array[1]] = array[2]
            # print("self._settings_array[1] :" + self._settings_array[array[1]], file=sys.stderr)


    def set_settings(self):
        self._timebank = int(self._settings_array["timebank"])
        self._current_stack = int(self._settings_array["initial_stack"])
        self._candles_given = int(self._settings_array["candles_given"])


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
                self._BTC_ETH_array.append({})


            if (splited_str[0] == "USDT_BTC"):
                self._USDT_BTC_array.append({
                    'date': float(splited_str[1]),
                    'high': float(splited_str[2]),
                    'low': float(splited_str[3]),
                    'open': float(splited_str[4]),
                    'close': float(splited_str[5]),
                    'volume': float(splited_str[6]),
                })
                self._USDT_BTC_array.append({})

            if (splited_str[0] == "USDT_ETH"):
                self._USDT_ETH_array.append({
                    'date': float(splited_str[1]),
                    'high': float(splited_str[2]),
                    'low': float(splited_str[3]),
                    'open': float(splited_str[4]),
                    'close': float(splited_str[5]),
                    'volume': float(splited_str[6]),
                })
                self._USDT_ETH_array.append({})

    def buy_crypto(self, currency, amount, stack):
        # print("SEND: buy USDT_BTC {0}".format(self._current_stack), file=sys.stderr)
        if stack > amount:
            print(f'buy {currency} {amount}')

    def sell_crypto(self, currency, amount):
        print("sell USDT_BTC 0.001", end='')

    # def find_middleBB(self, array, period = 0):
    #     tmp_list = array[:period]
    #     return statistics.mean(tmp_list)

    def find_middleBB(self, array, period):
        tmp_list = []
        for x in array[:period]:
            if x.get('close') is not None:
                tmp_list.append(x.get('close'))
        return (sum(tmp_list) / len(tmp_list))

    def getStandardDeviation(self, array, period):
        deviationSum = 0
        tmp_list = array[:period]
        average = statistics.mean(tmp_list)
        for i in tmp_list:
            deviationSum += pow((abs(i - average)), 2)
        return (math.sqrt(deviationSum / period))

    # def close_open_list(self, array, period, papa):
    #     tmp_list = []
    #     for x in array[:period]:
    #         if x.get(papa) is not None:
    #             tmp_list.append(x.get(papa))
    #     return tmp_list

    def close_open_list(self, array, period, papa):
        tmp_list = []
        for x in array:
            if x.get(papa) is not None:
                tmp_list.append(x.get(papa))
        return tmp_list

    def buy_or_sell(self, array, currency_string, currency_stack):
        period = self._candles_given
        middleBB = self.find_middleBB(array, period)

        close_list = self.close_open_list(array, period, "close")
        open_list = self.close_open_list(array, period, "open")

        # open_list = []

        # for x in array[:period]:
        #     if x.get('open') is not None:
        #         open_list.append(x.get('open'))

        get_StD = self.getStandardDeviation(close_list, period)
        # upperBB = (get_StD * 2)
        # lowerBB = (get_StD / 2)

        upper = middleBB + (get_StD * 2)
        lower = middleBB - (get_StD * 2)

        try:

            print("lower = " + str(lower), file=sys.stderr)
            print("self.array[-1][close] = " + str(close_list[-1]["close"]), file=sys.stderr)
            if (close_list[-1] < lower):
                self.buy_crypto(currency_string, 0.001, currency_stack)
            elif (close_list[-1] > upper):
                print("sell " + currency_string + " " + "0.001", end='')

            else:
                print("pass")
                print("je pass", file=sys.stderr)

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
                self.buy_or_sell(self._USDT_ETH_array, "USDT_ETH", self._USDT_stack)
                self.buy_or_sell(self._BTC_ETH_array, "BTC_ETH", self._BTC_stack)
                self.buy_or_sell(self._USDT_BTC_array, "USDT_BTC", self._USDT_stack)
            else :
                print("caca pas bon", file=sys.stderr)


    def entrypoint(self):
        self.get_settings()
        self.set_settings()
        self.loop()



def main():
    trade = Trading()
    trade.entrypoint()

if __name__ == '__main__':
    main()
