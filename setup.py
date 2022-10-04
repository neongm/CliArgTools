from setuptools import setup, find_packages

setup(
    name='CliArgTools',
    version='0.1',
    license='MIT',
    author="Vologin Alexander",
    author_email='chura2013c@gmail.com',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    url='https://https://github.com/neongm/CliArgTools',
    keywords='cli arguments parsing parser command line',
    install_requires=[
      ],
)