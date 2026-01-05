from setuptools import setup, find_packages

setup(
    name='YData_baseball',
    version='2026.7',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='A package to download YData Baseball files',
    # long_description=open('README.md').read(),
    install_requires=['numpy'],
    url='https://github.com/emeyers/SDS1730',
    author='Ethan Meyers',
    author_email='ethan.meyers@yale.edu'
)
