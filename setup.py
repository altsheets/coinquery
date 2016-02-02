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
	'''
)

