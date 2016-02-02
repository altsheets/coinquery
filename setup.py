# inspired by:
# https://www.youtube.com/watch?v=kNke39OZ2k0
# pip install --editable .

from setuptools import setup

import os
print "DEBUG: %s is loaded" % os.path.split(__file__)[1]

import setupCustom


setup(
	
	cmdclass={'install': setupCustom.my_install},
	
	name="coinquery",
	version="0.2",
	py_modules=['hello', 'coinq', 'altsheets'],
	install_requires=['Click','requests'],
	entry_points='''
		[console_scripts]
		hello=hello:cli
		coinq=coinq:cli
	''',
	
	# metadata for upload to PyPI
  author = "AltSheets Dev",
  author_email = "altsheets(plus)coding(at)gmail.com",
  description = "CLI client for AltFolio dataserver.",
  keywords = "altcoin altcoins coinq coinquery cryptocurrency cryptocurrencies bitcoin api trading data aggregator",
  url = "http://altfolio.ddns.net/",   
  classifiers = [
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Operating System :: OS Independent",
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Intended Audience :: Financial and Insurance Industry",
        "Topic :: Office/Business :: Financial :: Spreadsheet",
        "Topic :: Software Development",
        "Topic :: Software Development :: Object Brokering",
        "Topic :: Software Development :: API",
        "Topic :: Internet :: WWW/HTTP :: API",
        "Topic :: Internet :: WWW/HTTP :: WSGI",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        ],
	long_description = ("coinq price"
					"coinq price DOGE"
					"coinq price --exchange bittrex DOGE"
					"coinq cmc --param volume24 DOGE"
					"coinq cmc --param price doge"
					),
)

