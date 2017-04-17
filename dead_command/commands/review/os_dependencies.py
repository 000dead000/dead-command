#!/usr/bin/env python

import os

from ..common import DARCommandCommon


class DARCommandCommandsOS(DARCommandCommon):
    def __init__(self, args):
        """ Constructor
        """
        self.args = args

    @staticmethod
    def get_definition():
        """
        * Install Operating System dependencies:
            ```bash
            dar-command.py install_os_dependencies
            ```
        """
        return {
            "name": "install_os_dependencies",
            "description": """Install Operating System dependencies""",
            "arguments": [],
        }

    def execute(self):
        """ Execute
        """
        os_file = os.path.join(
            self.get_package_dir(),
            "dependencies",
            "os.sh"
        )

        command_arguments = [
            "sh",
            os_file
        ]
        self.run_command(command_arguments)