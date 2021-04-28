from setuptools import setup

setup(
    name = "ashmail",
    version = "v2.1.0",
    author_email = "aarush@theaarushgupta.com",
    packages = ["ashmail"],
    package_data = {},
    install_requires = ["jinja2", "pyyaml"],
    entry_points = {
    "console_scripts": ["ashmail = ashmail.ashmail:main"]
    }
)