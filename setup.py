from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in vat_register/__init__.py
from vat_register import __version__ as version

setup(
	name="vat_register",
	version=version,
	description="Sales and Purchase VAT Register",
	author="Ajira Group",
	author_email="support@ajiragroup.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
