try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup

config = {
		'description' : 'excercise 47',
		'author' : 'arakipovic',
		'url' : 'https://arakipovic@github.com/example',
		'downolad_url' : 'url',
		'author_email' : 'alen.rakipovic@gmail.com', 
		'version' : '1.0',
		'install_requires' : ['nose'],
		'packages' : ['ex47'],
		'scripts' : [],
		'name' : 'ex47'
}

setup(**config)


