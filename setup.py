from distutils.core import setup
from setuptools import find_packages

with open('README.rst') as readme:
    long_description = readme.read()

with open('requirements.txt') as reqs:
    install_requires = [
        line for line in reqs.read().split('\n') if (line and not
                                                     line.startswith('--'))
    ]

setup(
    name='Playlists',
    version=__import__('Playlists').__version__,
    author='Eshaan Bhattad',
    author_email='eshaan2@illinois.edu',
    packages=find_packages(),
    include_package_data=True,
    url='',
    license='BSD',
    description='Spotify User Analyzer App',
    long_description=long_description,
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
    ],
    zip_safe=False,
    install_requires=install_requires,
)
