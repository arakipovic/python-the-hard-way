try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup

config = {
		'description' : 'Example Project',
		'author' : 'arakipovic',
		'url' : 'https://arakipovic@github.com/example',
		'downolad_url' : 'url',
		'author_email' : 'alen.rakipovic@gmail.com', 
		'version' : '1.0',
		'install_requires' : ['nose'],
		'packages' : ['Example'],
		'scripts' : [],
		'name' : 'example'
}

setup(**config)


