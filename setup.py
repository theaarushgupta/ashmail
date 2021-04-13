from setuptools import setup

setup(
    name = "dispatch",
    version = "0.1",
    author_email = "hiaarushgupta@gmail.com",
    packages = ["dispatch"],
    package_data = {},
    install_requires = ["jinja2", "pyyaml"],
    entry_points = {
    "console_scripts": ["dispatch = dispatch.dispatch:main"]
    }
)