from yaml import safe_load
from csv import reader
from jinja2 import Template
from argparse import ArgumentParser

from dispatch.send import Send

class Dispatch:
    def __init__(self, configuration: dict, content: str, recieversFile: str) -> None:
        with open(content) as content:
            content = content.read()
            self.template = Template(content)
        self.configuration = configuration
        self.recieversFile = recieversFile
        self.recievers = self.retrieveRecievers()

    def retrieveRecievers(self) -> dict:
        recievers = {}
        with open(self.recieversFile) as recieversFile:
            parsedRecieversFile = reader(recieversFile)
            for row in list(parsedRecieversFile)[1:]:
                name, email = row
                recievers[name] = email
        return recievers
    
    def parseSubject(self, subject: str, name: str, email: str) -> None:
        template = Template(subject)
        parsedSubject = template.render(name = name, subject = subject)
        self.configuration["subject"] = parsedSubject

    def dispatch(self) -> None:
        for name in self.recievers:
            email = self.recievers[name]
            content = self.template.render(name = name, email = email)
            self.parseSubject(
                self.configuration["subject"],
                name,
                email
            )
            send = Send(
                self.configuration["from"],
                self.configuration["password"],
                email,
                self.configuration["subject"],
                content
            )
            send.send()

def retrieveConfigurationFile() -> str:
    argumentParser = ArgumentParser(
        prog = "dispatch",
        description = "mass-emailing made simple and affordable"
    )
    argumentParser.add_argument("configuration", help = "the name of the configuration file")
    arguments = argumentParser.parse_args()
    return arguments.configuration

def main() -> None:
    configuration = retrieveConfigurationFile()
    with open(configuration) as configuration:
        configuration = safe_load(configuration)
    content = configuration["content"]
    recievers = configuration["recievers"]
    dispatch = Dispatch(configuration, content, recievers)
    dispatch.dispatch()