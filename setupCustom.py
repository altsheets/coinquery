"""Custom preinstall - but cannot get it working"""

from distutils.command.install import install as ORIG_install

import string, random, os

print "DEBUG: %s is loaded" % os.path.split(__file__)[1]


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
		fobj.write('UID=%s\n' % randomString())
			
	print "Written UID file:"
	print target_file


class my_install(ORIG_install):
    """Custom preinstall - but cannot get it working."""

    def run(self):
    	print "Custom preinstall:"
    	# honor the --dry-run flag
    	if not self.dry_run:
    		createUIDfile(self.build_lib)
		
    	ORIG_install.run(self)


def testSubroutines():
	"""just testing the functions"""
	print randomString()
	
	import tempfile
	fp=tempfile.mkdtemp()
	print fp
	createUIDfile(fp)
	

if __name__ == '__main__':
	testSubroutines()
