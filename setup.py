from setuptools import setup, find_packages

setup(
    name='alephclient',
    version='0.10.7',
    description='Command-line client for Aleph API',
    author='Organized Crime and Corruption Reporting Project',
    author_email='data@occrp.org',
    url='http://github.com/alephdata/alephclient',
    license='MIT',
    classifiers=[
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7'
    ],
    packages=find_packages(exclude=['alephclient.tests']),
    install_requires=[
        'six',
        'banal >= 0.4.2',
        'pyyaml',
        'pathlib2; python_version<"3"',
        'requests >= 2.20.0',
        'requests_toolbelt >= 0.8.0',
        'click >= 6.7'
    ],
    extras_require={
        'dev': [
            'pytest',
            'pytest-mock >= 1.10.0',
        ]
    },
    entry_points={
        'console_scripts': [
            'alephclient = alephclient.cli:cli'
        ]
    },
)
