#!/usr/bin/env python

import os

from .common import Common


class MigrationsCommand(Common):
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
             
            dead-command.py migrate
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

        manage = os.path.join(
            self.get_instance_dir(),
            "manage.py"
        )

        command_arguments = [
            "python",
            manage,
            "makemigrations",
        ]
        self.run_command(command_arguments)

        command_arguments = [
            "python",
            manage,
            "migrate",
        ]
        self.run_command(command_arguments)
