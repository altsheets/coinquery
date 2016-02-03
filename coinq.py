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


@click.command()
@click.option('--exchange', default='cmc', help='Where do you want the data from?')
@click.argument('acronym', default='BTC', required=False)
@pass_config
def price(config, exchange, acronym):
	"""Cryptocurrency prices: coinq price LTC"""
	if not config.only: 
		click.echo( "%s price from %s: " % (acronym.upper(), exchange), nl=False)
		# if several prices, then newline after sentence
		if "," in exchange or "," in acronym: click.echo()
	
	what="%s/%s/price" % (acronym, exchange)
	click.echo( altsheets.askDataserver(what, config.key), nl=False )
	
	if not config.only: 
		click.echo("")
	
	
@click.command()
@click.option('--param', default='position', 
			help='position, name, marketCap, price, volume24, change7d, change7h,change1h')
@click.argument('acronym', default='BTC', required=False)
@pass_config
def cmc(config, param, acronym):
    """Coinmarketcap data: coinq cmc doge"""
    if not config.only: 
        click.echo( "%s %s from CMC: " % (acronym.upper(), param), nl=False)
        # if several prices, then newline after sentence
        if "," in acronym: click.echo()

    what="%s/cmc/%s" % (acronym, param)
    click.echo( altsheets.askDataserver(what, config.key), nl=False )
    
    if not config.only: click.echo("")
	

# add the commands to the main command group
cli.add_command(serial)
cli.add_command(getkey)
cli.add_command(price)
cli.add_command(cmc)

# environment variable prefix
cli(auto_envvar_prefix='COINQ')

	
