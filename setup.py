from setuptools import setup, find_packages

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name='cbaxter1988_utils',
    version='0.2.0',
    url='https://github.com/byt3-m3/utils',
    description='A Package containing my utils',
    author='Courtney S Baxter Jr',
    author_email='cbaxtertech@gmail.com',
    packages=find_packages(),
    install_requires=required,
    include_package_data=True
)
