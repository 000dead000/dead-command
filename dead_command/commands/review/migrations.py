#!/usr/bin/env python

import os

from ..common import DARCommandCommon


class DARCommandCommandsMigrations(DARCommandCommon):
    def __init__(self, args):
        """ Constructor
        """
        self.args = args

    @staticmethod
    def get_definition():
        """
        * Run migrations:
            ```bash
            # This runs makemigrations and migrate
             
            dar-command.py migrate
            ```
        """
        return {
            "name": "migrate",
            "description": """This runs makemigrations and migrate""",
            "arguments": [],
        }

    def execute(self):
        """ Execute
        """
        command_arguments = [
            "python",
            "manage.py",
            "makemigrations",
        ]
        self.run_command(command_arguments)

        command_arguments = [
            "python",
            "manage.py",
            "migrate",
        ]
        self.run_command(command_arguments)