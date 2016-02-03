"""Custom preinstall - creates a UID.py"""

from distutils.command.install import install as ORIG_install

import string, random, os

# print "DEBUG: %s is loaded" % os.path.split(__file__)[1]


def randomString(UID_LENGTH=20):
	"""random string of lowercase ascii plus digits"""
	chars=string.ascii_lowercase + string.digits
	return "".join([random.choice(chars) for _ in xrange(UID_LENGTH)]) 


def createUIDfile(filepath):
	"""
	Creates a file UID.py with a UID which can later be imported:
	from UID import UID
	"""
	
	target_file = os.path.join(filepath, 'UID.py')
	
	with open(target_file, 'w') as fobj:
		fobj.write('UID="%s"\n' % randomString())
			
	# print "Written UID file:", target_file
	

def createUIDfileIntoSourcePath():
	"""
	Current absolute path, then create UID.py
	Then try to import to see if it succeeded.
	"""
	here=os.path.dirname( os.path.abspath(__file__) )
	createUIDfile(here)
	try:
		from UID import UID
		# print "UID.py could be found, UID is: ", UID
		return True
	except:
		return False


def deleteUIDfromSourcePath():
	here=os.path.dirname(__file__)
	try:
		os.remove(os.path.join(here,"UID.py"))
		return True
	except:
		return False
	

def testSubroutines():
	"""just testing the functions"""
	print randomString()
	
	import tempfile
	fp=tempfile.mkdtemp()
	print fp
	createUIDfile(fp)
	

if __name__ == '__main__':
	testSubroutines()
