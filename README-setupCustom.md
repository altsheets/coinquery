# setupCustom.py

### Problem
I want to generate a file ``UID.py`` during ``setuptools.setup``, but I just cannot get it working.

Please try this: 


### quickstart
(in virtualenv so not to dirty your python installation)

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
    
My small scripts are getting installed (try ``hello Earth``) - but the custom installer (with my preinstall routine) is never called, seemingly? 

### purpose
Later I want to be able to load an (always-same):
* **UID.py** file with a machine-specific (or rather installation-specific) user-ID
* see altsheets.py [line 4](https://github.com/altsheets/coinquery/blob/d8a1b11c6b68a9d923de21c10e6c0081c55dc8c1/altsheets.py#L3-L6): ``from UID import UID``

### preinstall

My attempts to create a **preinstall routine**
* setup.py [line 15](https://github.com/altsheets/coinquery/blob/c14d1343daa9b18d1f8c5e14c89591dbccd06ae5/setup.py#L10-L16) ``cmdclass={'install': setupCustom.my_install}``
* setupCustom.py [line 31](https://github.com/altsheets/coinquery/blob/c14d1343daa9b18d1f8c5e14c89591dbccd06ae5/setupCustom.py#L31-L40) ``class my_install(ORIG_install)``

are all not working yet.

    
Please help me: How to execute my own python subroutine during the offical setuptools.setup install procedure?

N.B.: I would like to **always** execute that custom subroutine, that is why I am not introducing an additional verb (or switch) into setup.py

But perhaps I am not yet understanding all this well enough.   My first day with setuptools, actually :-)  
Always wanted to, never needed to. Until now. Great opportunity!



