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

        current_directory = self.get_current_dir()

        dead_common = os.path.join(
            self.other_package_dir("dead_common"),
            "static",
            "dead-common"
        )

        paths = [
            current_directory,
            dead_common,
        ]

        for path in paths:
            found = True
            for file_to_check in files_to_check:
                ftc = os.path.join(
                    path,
                    file_to_check
                )

                if not os.path.isfile(ftc):
                    found = False

            if found:
                self.goto_directory(path)
                self.run_command(command_arguments)

        self.goto_directory(current_directory)
