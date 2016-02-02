# coinquery
Work in progress - NOT READY.

### Problem
I want to generate a file ``UID.py`` during ``setuptools.setup``, but I just cannot get it working.

Please try this (in virtualenv so not to dirty your python installation): 


### quickstart
	mkdir a
	cd a
    pip install virtualenv
    virtualenv venv
    venv\Scripts\activate
or on Linux

	. venv/bin/activate
	
Then

    git clone https://github.com/altsheets/coinquery.git
    cd coinquery
    pip install --editable .
    
My small scripts are getting installed - but the custom installer is never called, seemingly? 

### preinstall

My attempts to create a **preinstall routine**:
* setup.py line 15 ``cmdclass={'install': setupCustom.my_install}``
* setupCustom.py line 31 ``class my_install(ORIG_install)``
    

---
---
---
---

from here onwards: Not ready.

### Examples
	coinquery
	coinquery --help
	 
	coinquery price
	coinquery --only price
	
	coinquery price DOGE
	coinquery price --exchange bittrex DOGE
	
	coinquery --only price --exchange bittrex dash && coinquery --only price --exchange bittrex doge
	
	coinquery price --exchange bittrex doge && coinquery cmc --param marketCap doge && coinquery cmc --param volume24 doge
	
	coinquery cmc --param marketCap doge && coinquery cmc --param volume24 doge && coinquery cmc --param change7h doge && coinquery cmc --param position doge && coinquery cmc --param price doge && coinquery cmc --param name doge
