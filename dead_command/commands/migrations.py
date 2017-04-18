#!/usr/bin/env python

import os

from .common import Common
from .exceptions import DEADException


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
            self.get_current_dir(),
            "manage.py"
        )

        if not os.path.isfile(manage):
            raise DEADException({
                "message": "{} is not in the current location".format(
                    manage
                )
            })

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
