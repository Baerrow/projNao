try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'My Project',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['projNao'],
    'scripts': [],
    'name': 'projNao'
}

setup(**config)