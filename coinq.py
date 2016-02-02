import requests, os

import altsheets

class Config(object):
	def __init__(self):
		self.key=None
		
pass_config=click.make_pass_decorator(Config, ensure=True)
	
@click.group()
@click.option('--key', default=None, help='Use the ENV variable: set ALTSHEETSKEY=yourserialkey')
@click.option('--only', is_flag=True, help='Only result, not full sentence')
@pass_config
def cli(config, key, only):
	if key==None: key=os.environ["ALTSHEETSKEY"]
	config.key=key
	config.only=only
	# config.acronym=acronym

@cli.command()
@click.option('--exchange', default='cmc', help='Where do you want the data from')
@click.argument('acronym', default='BTC', required=False)
@pass_config
def price(config, exchange, acronym):
	"""
	get cryptocoin data: coinq price LTC
	"""
	if not config.only: 
		click.echo( "%s price from %s: " % (acronym.upper(), exchange), nl=False)
	
	what="%s/%s/price" % (acronym, exchange)
	click.echo( altsheets.askDataserver(what, config.key), nl=False )
	
	if not config.only: 
		click.echo("")
	
	
@cli.command()
@click.option('--param', default='position', help='position, name, marketCap, price, volume24, change7d, change7h,change1h')
@click.argument('acronym', default='BTC', required=False)
@pass_config
def cmc(config, param, acronym):
    """
    Get coinmarketcap data: coinq cmc --param volume24 doge
    """
    if not config.only: 
        click.echo( "%s %s from CMC: " % (acronym.upper(), param), nl=False)

    what="%s/cmc/%s" % (acronym, param)
    click.echo( altsheets.askDataserver(what, config.key), nl=False )
    
    if not config.only: click.echo("")
	
