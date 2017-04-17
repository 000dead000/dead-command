#!/usr/bin/env python

from ..common import DARCommandCommon


class DARCommandCommandsBower(DARCommandCommon):
    def __init__(self, args):
        """ Constructor
        """
        self.args = args

    @staticmethod
    def get_definition():
        """
        * Install bower dependencies:
            ```bash
            dar-command.py install_bower_dependencies
            ```
        """
        return {
            "name": "install_bower_dependencies",
            "description": """Install bower dependencies""",
            "arguments": [],
        }

    def execute(self):
        """ Execute
        """
        command_arguments = [
            "bower",
            "update",
            "--allow-root",
            "--save"
        ]
        self.run_command(command_arguments)