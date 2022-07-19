import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
	   name='mysamplepackage',
	   packages=['mysamplepackage'],
	   version='0.0.1a0',
	   description=('This is a sample package.'),
	   url='https://github.com/sofia-scz/mysamplepackage',
	   author='Package Author',
	   install_requires=['numpy','matplotlib'], 
	   classifiers=[
		"Programming Language :: Python :: 3",
		"License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
		"Operating System :: POSIX :: Linux",]
)
