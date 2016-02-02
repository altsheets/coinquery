# https://www.youtube.com/watch?v=kNke39OZ2k0
# pip install --editable .

from setuptools import setup


setup(
	name="altcoins",
	version="0.1",
	py_modules=['hello','altcoin'],
	install_requires=['Click','requests'],
	entry_points='''
		[console_scripts]
		hello=hello:cli
		altcoin=altcoin:cli
	''',
	
	# metadata for upload to PyPI
  author = "AltSheets Dev",
  author_email = "altsheets+coding@gmail.com",
  description = "CLI client for AltFolio dataserver.",
  license = "TODO. Probably something alike http://altsheets.ddns.net/assetgraphs/v2/LICENSE.txt",
  keywords = "altcoins altcoin cryptocurrency cryptocurrencies bitcoin api trading data aggregator",
  url = "http://altfolio.ddns.net/",   
  classifiers = [
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        ],
	long_description = ("altcoin price"
										"altcoin price DOGE"
										"altcoin price --exchange bittrex DOGE"
										"altcoin cmc --param volume24 DOGE"
										"altcoin cmc --param price doge"
										),
)

