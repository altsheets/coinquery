import requests # pip install requests 
import click # pip install Click

import os, webbrowser

import altsheets


class Config(object):
	"""Container to pass data across"""
	def __init__(self):
		self.key="0"
		self.only=False
		
pass_config=click.make_pass_decorator(Config, ensure=True)
	
	
@click.group()
@click.option('--key', help='Use the ENV variable: set COINQ_KEY=yourserialkey')
@click.option('--only', is_flag=True, help='Only result, not full sentence.')
@pass_config
def cli(config, key, only):
	"""coinq needs a valid serial key for the altfolio dataserver.     
	
See github.com/altsheets/coinquery for details how to use this."""

	config.key=key
	config.only=only


@click.command()
@pass_config
def serial(config):
	"""What the dataserver says about your key."""
	if not config.only: 
		click.echo( "serial key dataserver answer:")
	what="serial"
	click.echo( altsheets.askDataserver(what, config.key), nl=False )
	if not config.only: 
		click.echo("")
		

@click.command()
@pass_config
def getkey(config):
	"""Get a trial serial key."""
	
	urls=["http://altfolio.ddns.net", "http://altsheets.ddns.net/customer/new.html"]
	if not config.only: 
		click.echo( "To get a trial key, open(s) a browser on these pages:")
	for url in urls: 
		if not config.only: click.echo(url)
		webbrowser.open(url, new=0, autoraise=True)


def toSatoshi(bitcoin):
	return int(float(bitcoin)*100000000)
	
	
@click.command()
@click.option('--exchange', default='cmc', help='Where do you want the data from?')
@click.option('--satoshi', is_flag=True)
@click.argument('acronym', default='BTC', required=False)
@pass_config
def price(config, exchange, acronym, satoshi):
	"""Cryptocurrency prices: coinq price LTC"""
	several=("," in exchange or "," in acronym)  
	
	if not several and not config.only: 
		click.echo( "%-5s at %-9s: " % (acronym.upper(), exchange), nl=False)
	
	what="%s/%s/price" % (acronym, exchange)
	answer=altsheets.askDataserver(what, config.key)
	
	if not several:
		if satoshi: answer=toSatoshi(answer)
		click.echo(answer)
	else:
		if config.only: 
			if satoshi: answer=toSatoshi(answer)
			click.echo( answer)
			
		else:
			answers=answer.split("\n")
			for e,a,p in zip(exchange.split(","), acronym.split(","), answers):
				if satoshi: p=toSatoshi(p)
				click.echo("%-5s at %-9s: %8s" % (a,e,p) )
	
	
@click.command()
@click.option('--param', default='position', 
			help='position, name, marketCap, price, volume24, change7d, change7h,change1h')
@click.argument('acronym', default='BTC', required=False)
@pass_config
def cmc(config, param, acronym):
    """Coinmarketcap data: coinq cmc doge"""
    several=("," in acronym)
    if not several and not config.only: 
        click.echo( "%-5s %-9s: " % (acronym.upper(), param), nl=False)

    what="%s/cmc/%s" % (acronym, param)
    answer=altsheets.askDataserver(what, config.key)
    
    if not several: click.echo( answer )
    else:
    	if config.only: click.echo( answer )
    	else:
    		answers=answer.split("\n")
    		for coin, a in zip(acronym.split(","), answers):
    			click.echo( "%-5s %-9s: %6s" % (coin.upper(), param, a))
    

# add the commands to the main command group
cli.add_command(serial)
cli.add_command(getkey)
cli.add_command(price)
cli.add_command(cmc)

# environment variable prefix
cli(auto_envvar_prefix='COINQ')

	
