#!/usr/bin/env python

import os

from .common import Common
from .exceptions import DEADException


class BowerDependenciesCommand(Common):
    def __init__(self, args):
        """ Constructor
        """
        self.args = args

    @staticmethod
    def get_definition():
        """
        * Install bower dependencies:
            ```bash
            dar-command.py bower_dependencies
            ```
        """
        return {
            "name": "bower_dependencies",
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

        files_to_check = [
            ".bowerrc",
            "bower.json"
        ]

        for file_to_check in files_to_check:
            ftc = os.path.join(
                self.get_current_dir(),
                file_to_check
            )

            if not os.path.isfile(file_to_check):
                raise DEADException({
                    "message": "{} not exists".format(
                        ftc
                    )
                })

        self.run_command(command_arguments)
