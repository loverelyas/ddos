from setuptools import setup,find_packages
setup(
    name='ddos_xr',
    version='1.0',
    description='DDos any site',
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url='https://github.com',
    packages=find_packages(),
    license='MIT',
    author='spiderXR',
    classifiers=['Programming Language :: Python :: 3'],
    entry_points={ 'console_scripts': [ 'ddos=DDos.__main__:main', 'DDos=DDos.__main__:main' ] }
)
