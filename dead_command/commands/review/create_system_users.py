#!/usr/bin/env python

import os

from ..common import DARCommandCommon


class DARCommandCommandsSystemUsers(DARCommandCommon):
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
            "name": "create_system_users",
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

        command_arguments = [
            "python",
            "manage.py",
            "loaddata",
            users,
        ]
        self.run_command(command_arguments)