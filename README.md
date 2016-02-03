# coinquery
Work in progress - NOT READY.

### Problem: custom setup.py not working yet.

See [README-setupCustom.md](README-setupCustom.md).

---
---
---
---

from here onwards: **Not** ready.

### Examples

#### Prices

General info

	coinq
	coinq --help

You must authorize at my dataserver. Get a key with your [AltFolio license](http://altfolio.ddns.net). Free trial!
	
	coinq --key 0123456789
	
It becomes really easy if you set/export an environment variable: 
	
	set COINQ_KEY=0123456789
	coinq
	
Have my dataserver pull coin data for you:
	 
	coinq price
	coinq --only price
	
Specify the coin, and the exchange (bittrex, bleutrade, btce, bter, ccex, cryptsy, hitbtc, poloniex, yobit), or cmc
	
	coinq price DOGE
	coinq price --exchange bittrex DOGE
	
	set COINQ_PRICE_EXCHANGE=poloniex
	coinq price DOGE
	
	set COINQ_PRICE_EXCHANGE=
	coinq price DOGE

Only answer, not sentence (Useful for creating complex batch files, and apps from this):

	coinq --only price DASH && coinq --only price DOGE
	
Several questions at the same time:

	coinq price --exchange bittrex,bittrex,poloniex DOGE,DASH,DASH

#### Fiat Prices
Fiat prices (usd/bitstamp, usd/btcefiat, usd/krakenfiat, usd/hitbtcfiat, eur/krakenfiat, eur/btcefiat, eur/hitbtcfiat, rur/btcefiat, gbp/krakenfiat, jpy/krakenfiat, cad/krakenfiat):

	coinq price --exchange bitstamp dummy
	coinq price --exchange bitstamp,btcefiat,krakenfiat,hitbtcfiat USD,USD,USD,USD
	coinq price --exchange krakenfiat,btcefiat,hitbtcfiat EUR,EUR,EUR
	
	set COINQ_PRICE_EXCHANGE=krakenfiat
	coinq price JPY
	coinq price CAD
	coinq price GBP
	set COINQ_PRICE_EXCHANGE=
	
	coinq --only price --exchange bitstamp USD
	

#### CoinMarketCap

CoinMarketCap parameters (position, name, price, marketCap, volume24, change1h, change7h, change7d)

	coinq cmc --param marketCap DOGE
	coinq cmc --param volume24 DOGE
	coinq cmc --param change7h DOGE
	
	set COINQ_CMC_PARAM=position
	coinq cmc DOGE
	coinq cmc NXT,HZ,BURST,FIMK
	

#### serial key
Check what the dataserver says about your serial key:

    coinq serial
    coinq --only serial

Get a trial serial key, as part of your [AltFolio](http://altfolio.ddns.net) subscription. 

    coinq getkey
    
