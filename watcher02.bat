@echo OFF
::
:: Simple Ticker 'watcher02.bat'
::                version v01
::
:: Keep an overview of ~10 coins on a market parameter from coinmarketcap
::
:: uses coinquery, which queries Altfolio Dataserver
::                               altfolio.ddns.net
::
:: manual: https://github.com/altsheets/coinquery
:: and:    coinq --help
::

:: Do not overdo this, please do not hammer my server. 900 seconds = 15 minutes.
set CHECK_EVERY=900

:: These comma separated lists must not have whitespaces:
set COINS=HYP,XRA,NOBL,NXT,XEM,RDD,SC,BURST,XPB,BTS,XMR,FLO,HZ,PPC,VIRAL,ADC

:: choose one parameter for coinmarketcap table
:: (position, name, price, marketCap, volume24, change1h, change7h, change7d)
set CMC_PARAM=change1h 

:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

coinq --only serial
echo .


:LOOP

coinq   cmc   --param %CMC_PARAM%               %COINS% 

time /T

sleep %CHECK_EVERY%

GOTO LOOP