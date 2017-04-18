#!/usr/bin/env python

import os

from .common import Common
from .exceptions import DEADException


class SystemUsersCommand(Common):
    def __init__(self, args):
        """ Constructor
        """
        self.args = args

    @staticmethod
    def get_definition():
        """
        * Create system users (admin, system, prueba):
            ```bash
            # This command create system users
             
            dar-command.py create_system_users
            ```
        """
        return {
            "name": "system_users",
            "description": """Create system users (admin, system, prueba)""",
            "arguments": [],
        }

    def execute(self):
        """ Execute
        """
        users = os.path.join(
            self.get_package_dir(),
            "fixtures",
            "users.json"
        )

        manage = os.path.join(
            self.get_current_dir(),
            "manage.py"
        )

        if not os.path.isfile(manage) or not os.path.isfile(users):
            raise DEADException({
                "message": "{} or {} are not in the current location".format(
                    manage,
                    users
                )
            })

        command_arguments = [
            "python",
            manage,
            "loaddata",
            users,
        ]
        self.run_command(command_arguments)