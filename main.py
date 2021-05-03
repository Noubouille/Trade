#!/usr/bin/env python3
# -*- coding: utf-8 -*-

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
            # print("le input str :" + self._input_str, file=sys.stderr)
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
                # self._BTC_ETH_array[-1]["date"] = float(splited_str[1])
                # self._BTC_ETH_array[-1]["high"] = float(splited_str[2])
                # self._BTC_ETH_array[-1]["low"] = float(splited_str[3])
                # self._BTC_ETH_array[-1]["open"] = float(splited_str[4])
                # self._BTC_ETH_array[-1]["close"] = float(splited_str[5])
                # self._BTC_ETH_array[-1]["volume"] = float(splited_str[6])

                self._BTC_ETH_array.append({
                    'date': float(splited_str[1]),
                    'high': float(splited_str[2]),
                    'low': float(splited_str[3]),
                    'open': float(splited_str[4]),
                    'close': float(splited_str[5]),
                    'volume': float(splited_str[6]),
                })
                # self._BTC_ETH_array.append({})


            if (splited_str[0] == "USDT_BTC"):

                # self._USDT_BTC_array[-1]["date"] = float(splited_str[1])
                # self._USDT_BTC_array[-1]["high"] = float(splited_str[2])
                # self._USDT_BTC_array[-1]["low"] = float(splited_str[3])
                # self._USDT_BTC_array[-1]["open"] = float(splited_str[4])
                # self._USDT_BTC_array[-1]["close"] = float(splited_str[5])
                # self._USDT_BTC_array[-1]["volume"] = float(splited_str[6])
                self._USDT_BTC_array.append({
                    'date': float(splited_str[1]),
                    'high': float(splited_str[2]),
                    'low': float(splited_str[3]),
                    'open': float(splited_str[4]),
                    'close': float(splited_str[5]),
                    'volume': float(splited_str[6]),
                })
                # self._USDT_BTC_array.append({})

            if (splited_str[0] == "USDT_ETH"):

                # self._USDT_ETH_array[-1]["date"] = float(splited_str[1])
                # self._USDT_ETH_array[-1]["high"] = float(splited_str[2])
                # self._USDT_ETH_array[-1]["low"] = float(splited_str[3])
                # self._USDT_ETH_array[-1]["open"] = float(splited_str[4])
                # self._USDT_ETH_array[-1]["close"] = float(splited_str[5])
                # self._USDT_ETH_array[-1]["volume"] = float(splited_str[6])
                self._USDT_ETH_array.append({
                    'date': float(splited_str[1]),
                    'high': float(splited_str[2]),
                    'low': float(splited_str[3]),
                    'open': float(splited_str[4]),
                    'close': float(splited_str[5]),
                    'volume': float(splited_str[6]),
                })
                # self._USDT_ETH_array.append({})

    def buy_crypto(self, currency, amount, stack):
        if stack > amount:
            print(f'buy {currency} {amount}', end='')

    def sell_crypto(self, currency, amount, stack):
        if stack > amount:
            print(f"sell {currency} {amount}", end='')

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

    def buy_or_sell(self, array, currency_string, currency_stack, order_bool):
        period = self._candles_given
        openArr = list()
        closeArr = list()

        for x in array[:-1]:
            if x.get('close') is not None:
                closeArr.append(x.get('close'))
            if x.get('open') is not None:
                openArr.append(x.get('open'))

        middleBB = self.find_middleBB(array, period)
        # middleBB2 = getmiddleBB(closeArr, period)

        # print("middleBB  =  " + str(middleBB), file=sys.stderr)
        # print("middleBB2  =  " + str(middleBB2), file=sys.stderr)
        close_list = self.close_open_list(array, period, "close")
        open_list = self.close_open_list(array, period, "open")


        get_StD = self.getStandardDeviation(close_list, period)

        upperBB = middleBB + (get_StD * 2)
        lowerBB = middleBB - (get_StD * 2)

        # buyValue = 
        print("lower bb value : " + str(lowerBB), file=sys.stderr)
        print("currency_stack : " + str(currency_stack), file=sys.stderr)

        if (closeArr[-1] < lowerBB):
            if (order_bool == True):
                print(";", end='')
            # print("I BUY LA STDX ", file=sys.stderr)
            # print("buy " + str(currency_string) + " " + "0.08", end='')
            self.buy_crypto(currency_string, 0.08, currency_stack)
            return True
        # elif (close_list[-1] > upperBB):
        #     if (order_bool == True):
        #         print(";", end='')
        #     self.sell_crypto(currency_string, 0.001, currency_stack)
        #     # print("sell " + str(currency_string) + " " + "0.005", end='')
        #     return True

        else:
            return False



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
            # print("fucking " + splited_str[0] + " stacks : " + splited_str[1], file=sys.stderr)

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
                order_bool = False
                statement_pass = False
                # statement_pass = order_bool or statement_pass
                order_bool = self.buy_or_sell(self._USDT_ETH_array, "USDT_ETH", self._USDT_stack, statement_pass)
                if (order_bool or statement_pass):
                    statement_pass = True
                else:
                    statement_pass = False

                order_bool = self.buy_or_sell(self._BTC_ETH_array, "BTC_ETH", self._BTC_stack, statement_pass)
                if (order_bool or statement_pass):
                    statement_pass = True
                else:
                    statement_pass = False

                order_bool = self.buy_or_sell(self._USDT_BTC_array, "USDT_BTC", self._USDT_stack, statement_pass)
                if (order_bool or statement_pass):
                    statement_pass = True
                else:
                    statement_pass = False

                if (statement_pass == False):
                    print("pass")
                else:
                    print("")
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
