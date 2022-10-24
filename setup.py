from setuptools import setup
from setuptools import find_packages


setup(
	name="gen",
	version='0.0.1',
	packages=find_packages(),
	install_requires=[
	"click",
	"typer",
	"rich",
	"emoji",
	"watchdog",
	"PyYAML"
	],
	entry_points='''
	[console_scripts]
	gen=gen:app
	'''
)
