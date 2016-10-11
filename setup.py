#from distutils.core import setup
from setuptools import setup, find_packages


VERSION = __import__("libopenvas").__version__

CLASSIFIERS = [
    'Environment :: Console',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent',
    'Topic :: System :: Networking',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 2.7',
]

install_requires = [
    'xmltodict',
]

setup(
    name="python-libopenvas",
    description="OMP python API and report parser",
    version=VERSION,
    author="bGN4",
    author_email="git@github.com",
    license='MIT License',
    platforms=['OS Independent'],
    url="https://github.com/bGN4/python-libopenvas",
    packages=['libopenvas',],
    include_package_data=True,
    install_requires=install_requires,
    classifiers=CLASSIFIERS,
)
