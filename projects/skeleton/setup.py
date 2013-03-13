try:
  from setuptools import setup
except ImportError:
  from distutils.core import setup

config = {
  'description' : 'My project',
  'author':'xphan',
  'url' : 'url to get it at.',
  'download url' : 'where to download it.',
  'author_email' : 'my email',
  'version' : '0.1',
  'install_requires' : ['nose'],
  'packages':[],
  'name':'projectname'
}

setup(**config)
