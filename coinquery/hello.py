# See https://www.youtube.com/watch?v=kNke39OZ2k0 for a 15 minute intro

import click

from coinquery import altsheets

@click.command()
@click.argument('greetee', default='World', required=False)
def cli(greetee):
	"""This hello'es something, or someone."""
	print "Hello %s!" % greetee
	print altsheets.UID