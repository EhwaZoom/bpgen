import setuptools


setuptools.setup(
    name             = 'bpgen',
    version          = '0.1.0',
    description      = 'Boilerplate generator.',
    url              = 'https://github.com/EhwaZoom/bpgen',
    author           = 'EhwaZoom',
    author_email     = 'ehwazoom@gmail.com',
    maintainer       = 'EhwaZoom',
    maintainer_email = 'ehwazoom@gmail.com',
    packages         = setuptools.find_packages(),
    entry_points     = {
        'console_scripts': ['bpgen=bpgen.main:main']
    }
)