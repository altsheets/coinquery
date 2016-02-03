@echo OFF
::
:: Simple Ticker 'watcher01.bat'
::                version v01
::
:: Keep an overview of ~10 coins prices
::
:: uses coinquery, which queries Altfolio Dataserver
::                               altfolio.ddns.net
::
:: manual: https://github.com/altsheets/coinquery
:: and:    coinq --help
::

:: Do not overdo this, please do not hammer my server. 900 seconds = 15 minutes.
set CHECK_EVERY=900

:: These comma separated lists (without whitespaces!) should be equally long:
set COINS=HYP,XRA,NOBL,NXT,XEM,RDD,SC,BURST,XPB,BTS,XMR,FLO,HZ,PPC,VIRAL,ADC
set EXCHANGES=poloniex,yobit,poloniex,poloniex,poloniex,poloniex,poloniex,poloniex,poloniex,poloniex,poloniex,poloniex,poloniex,poloniex,bittrex,bleutrade

:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

coinq --only serial
echo .


:LOOP

coinq  price  --exchange %EXCHANGES% --satoshi  %COINS%

time /T

sleep %CHECK_EVERY%

GOTO LOOP