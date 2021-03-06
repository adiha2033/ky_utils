from setuptools import setup, find_packages

classifiers = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Eduction',
    'Operating System :: Microsoft :: Windows :: Windows 10',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3'
]

setup(
    name='ky_utils',
    version='0.0.1',
    description='KayHut DevOps Utils package',
    long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
    url='',
    author='Adi Haim',
    author_email='adi.shimon.haim@gmail.com',
    license='MIT',
    classifiers=classifiers,
    keywords='',
    packages=find_packages(),
    install_requires=[''],
    python_requires='>=3.6'
)
