#!/usr/bin/env python

import os

from ..common import DARCommandCommon


class DARCommandCommandsUpdatePackage(DARCommandCommon):
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
            self.DAR_COMMAND_PACKAGE,
        ]
        self.run_command(command_arguments)