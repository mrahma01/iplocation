# python setup.py register
# python setup.py sdist upload
from setuptools import setup

setup(
     name='ip2location',
     version='0.1',
     description='Return city, country, location, business details of given/outgoing ip',
     author='Muhammad M Rahman',
     author_email='mmrs151@gmail.com',
     url='https://github.com/mrahma01/ip2location',
     py_modules=['ip2location'],
     classifiers=[
          "License :: OSI Approved :: GNU General Public License (GPL)",
          "Programming Language :: Python",
          "Development Status :: 4 - Beta",
          "Intended Audience :: Developers",
          "Topic :: Internet",
      ],
     keywords='iptolocaiton geoip',
     license='GPL',
     install_requires=[
         'setuptools',
         'beautifulsoup4>=4.0.5',
         'outgoingip>=1.0',
         ],
     )
