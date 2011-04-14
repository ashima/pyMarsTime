#!/usr/bin/env python

from setuptools import setup

setup(name="Mars24",
      version='0.3.0',
      description='Mars24 library, implements the Mars24 algorithm [Allison and McEwan, 2000]',
      author="Christopher Lee",
      url="http://code.foldmountain.com/mars24",
      author_email="lee@foldmountain.com",
      packages=["Mars24"],
      license="LICENSE.txt",
      install_requires=["setuptools"],
      long_description=open("README.txt").read(),
      classifiers=["License :: OSI Approved :: BSD License",
                  "Intended Audience :: Science/Research",
                  "Programming Language :: Python :: 2.7",
                  "Topic :: Scientific/Engineering :: Astronomy"],
      zip_safe=True,
)