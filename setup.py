import re
import io

from setuptools import setup
from setuptools.command.test import test as TestCommand


class Tox(TestCommand):
    
    user_options = [('tox-args=', 'a', "Arguments to pass to tox")]
    
    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.tox_args = None

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        #import here, cause outside the eggs aren't loaded
        import tox
        import shlex
        args = self.tox_args
        if args:
            args = shlex.split(self.tox_args)
        tox.cmdline(args=args)


with io.open('swoopi/__init__.py', 'r') as pkg_init:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]',
                        pkg_init.read(), re.MULTILINE).group(1)

with io.open('README.rst', 'r', encoding='utf-8') as pkg_readme:
    readme = pkg_readme.read()

if not version:
    raise RuntimeError('Can\'t find version information in package __init__') 

if not readme:
    raise RuntimeError('Can\'t find README.rst file')


setup(
    name='swoopi',
    version=version,
    description='Camera interactions for the Raspberry Pi.',
    long_description=readme,
    url='https://github.com/swoopi/swoopi',
    author='Minn Soe',
    author_email='contributions@minn.io',
    packages=['swoopi'],
    install_requires=[],
    classifiers=[
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 2.7'
    ]
)
