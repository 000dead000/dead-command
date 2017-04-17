#!/usr/bin/env python

from .common import Common


class UpdatePackageCommand(Common):
    def __init__(self, args):
        """ Constructor
        """
        self.args = args

    @staticmethod
    def get_definition():
        """
        * Update dar-command package:
            ```bash
            dar-command.py update
            ```
        """
        return {
            "name": "update",
            "description": """Update dar-command package""",
            "arguments": [],
        }

    def execute(self):
        """ Execute
        """
        command_arguments = [
            "pip",
            "install",
            "-U",
            self.DEAD_COMMAND_PACKAGE,
        ]
        self.run_command(command_arguments)