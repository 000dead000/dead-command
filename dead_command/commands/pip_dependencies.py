#!/usr/bin/env python

import os

from .common import Common
from .exceptions import DEADException


class PIPDependenciesCommand(Common):
    def __init__(self, args):
        """ Constructor
        """
        self.args = args

    @staticmethod
    def get_definition():
        """
        * Install pip dependencies:
            ```bash
            dar-command.py install_pip_dependencies
            ```
        """
        return {
            "name": "pip_dependencies",
            "description": """Install pip dependencies""",
            "arguments": [],
        }

    def execute(self):
        """ Execute
        """
        pip_file = os.path.join(
            self.get_package_dir(),
            "dependencies",
            "pip.txt"
        )

        command_arguments = [
            "pip",
            "install",
            "-U",
            "-r",
            pip_file
        ]

        self.run_command(command_arguments)

        pip_file = os.path.join(
            self.get_current_dir(),
            "requirements.txt"
        )

        if os.path.isfile(pip_file):
            raise DEADException({
                "message": "{} is not in the current location".format(
                    pip_file
                )
            })

        command_arguments = [
            "pip",
            "install",
            "-U",
            "-r",
            pip_file
        ]

        self.run_command(command_arguments)
