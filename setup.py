from setuptools import setup
setup(
    name = 'amacron',
    version = '0.2.4',
    packages = ['amacron'],
    entry_points = {
        'console_scripts': [
            'amacron = amacron.__main__:main'
        ]
    })