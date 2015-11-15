from __future__ import print_function
from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand
import io
import codecs
import os
import sys

import backprojectionPy

here = os.path.abspath(os.path.dirname(__file__))

def read(*filenames, **kwargs):
    encoding = kwargs.get('encoding', 'utf-8')
    sep = kwargs.get('sep', '\n')
    buf = []
    for filename in filenames:
        with io.open(filename, encoding=encoding) as f:
            buf.append(f.read())
    return sep.join(buf)

long_description = read('README.md', 'TODO.md')

class PyTest(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import pytest
        errcode = pytest.main(self.test_args)
        sys.exit(errcode)

setup(
    name='backprojectionPy',
    version=backprojectionPy.__version__,
    url='https://github.com/qingkaikong/backprojectionPy.git',
    license='BSD License',
    author='Qingkai Kong',
    tests_require=['Add later'],
    install_requires=['Add later',
                    ],
    cmdclass={'test': PyTest},
    author_email='qingkai.kong@gmail.com',
    description='Seismic backprojection using python',
    long_description=long_description,
    packages=['backprojectionPy'],
    include_package_data=True,
    platforms='any',
    test_suite='backprojectionPy.test.test_backprojection',
    classifiers = [
        'Programming Language :: Python',
        'Development Status :: 0 - Alpha',
        'Natural Language :: English',
        'Environment :: Web Environment',
        'Intended Audience :: Seismologist',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Seismology :: Application :: BackProjection',
        ],
    extras_require={
        'testing': ['pytest'],
    }
)
