# -*- coding: utf-8 -*-
import sys

from vnhuobi import *

reload(sys)
sys.setdefaultencoding("utf-8")
# 上面这种代码曾经（现在依然）是解决中文编码的万能钥匙。解决编码错误问题一劳永逸，
# 从此和 UnicodeEncodeError: 'ascii' codec can't encode characters in position 0-5: ordinal not in range(128) 说 byebye 。


## 订阅 KLine 数据
##tradeStr="""{"sub": "market.ethusdt.kline.1min","id": "id10"}"""

## 请求 KLine 数据
## tradeStr="""{"req": "market.ethusdt.kline.1min","id": "id10", "from": 1513391453, "to": 1513392453}"""

##订阅 Market Depth 数据
# tradeStr="""{"sub": "market.ethusdt.depth.step5", "id": "id10"}"""

##请求 Market Depth 数据
## tradeStr="""{"req": "market.ethusdt.depth.step5", "id": "id10"}"""

##订阅 Trade Detail 数据
## tradeStr="""{"sub": "market.ethusdt.trade.detail", "id": "id10"}"""

##请求 Trade Detail 数据
## tradeStr="""{"req": "market.ethusdt.trade.detail", "id": "id10"}"""

##请求 Market Detail 数据
## tradeStr="""{"req": "market.ethusdt.detail", "id": "id12"}"""

# ws.send(tradeStr)
# while(1):
# compressData=ws.recv()
##print compressData
# result=zlib.decompress(compressData, 15+32).decode('utf-8')
# if result[:7] == '{"ping"':
# ts=result[8:21]
# pong='{"pong":'+ts+'}'
# ws.send(pong)
# ws.send(tradeStr)
# else:
# print(result)


def testTrade():
    """测试交易"""
    accessKey = '24cfa2dc-88140ff7-9f536d15-efb74'
    secretKey = '458867e2-2f4cd582-80ea978d-396b3'

    # 创建API对象并初始化
    api = TradeApi()

    api.init(api.MATOU, accessKey, secretKey, mode=api.SYNC_MODE)
    api.start()

    # 查询
    # print api.getSymbols()

    symbol = 'btc_usdt'
    # accountid, amount, symbol, type_
    # 下单
    # print api.placeOrder('', amount, symbol, type_, price, 'api')
    print api.placeOrder('', 0.0025, symbol, "buy-limit", 6535.06, 'api')
    # (True, {u'status': u'ok', u'code': 200, u'data': 3119})


def testData():
    """测试行情"""
    # {u'ch': u'market.btcusdt.trade.detail',
    #  u'tick': {u'data': [{u'amount': 0.0004,
    #                       u'direction': u'sell',
    #                       u'id': 141150651318851143732L,
    #                       u'price': 8204.92,
    #                       u'ts': 1532847725175L}],
    #            u'id': 14115065131L,
    #            u'ts': 1532847725175L},
    #  u'ts': 1532847725259L}
    symbol = 'btcusdt'
    api = DataApi()
    api.connect("wss://api.huobipro.com/ws")
    # api.subscribeMarketDepth(symbol)
    # data = api.subscribeTradeDetail(symbol)

    # 成交
    api.subscribeTradeDetail(symbol)

    # 深度
    # api.subscribeMarketDepth(symbol)

    # api.subscribeTradeDetail('ethusdt')
    # api.subscribeMarketDetail('ethusdt')
    # input()


if __name__ == '__main__':
    testData()
    # testTrade()
