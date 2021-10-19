#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages
from newlinecharacterconv.version import version
with open('README.rst',encoding='utf8') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [ ]

test_requirements = [ ]

setup(
    author="NewlineCharacterConv",
    author_email='qin__xuan@yeah.net',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="Windows下对文本文件的换行符转换为Linux下格式",
    entry_points={
        'console_scripts': [
            'd2u=newlinecharacterconv.cli:main',
        ],
    },
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='newlinecharacterconv',
    name='newlinecharacterconv',
    packages=find_packages(include=['newlinecharacterconv', 'newlinecharacterconv.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/qinxian1989/newlinecharacterconv',
    version=version,
    zip_safe=False,
)
