#!/usr/bin/env python

import os

from ..common import DARCommandCommon


class DARCommandCommandsLive(DARCommandCommon):
    def __init__(self, args):
        """ Constructor
        """
        self.args = args

    @staticmethod
    def get_definition():
        """
        * Run live server port 9500:
            ```bash
            # This runs liverserver at port 9500
             
            dar-command.py liveserver
            ```
        """
        return {
            "name": "liveserver",
            "description": """This runs liveserver at port 9500""",
            "arguments": [],
        }

    def execute(self):
        """ Execute
        """
        command_arguments = [
            "python",
            "manage.py",
            "runserver",
            "0.0.0.0:{}".format(self.DEFAULT_PORT),
        ]
        self.run_command(command_arguments)