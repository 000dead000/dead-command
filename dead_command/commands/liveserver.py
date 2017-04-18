#!/usr/bin/env python

import os

from .common import Common
from .exceptions import DEADException


class LiveserverCommand(Common):
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
            "runserver",
            "0.0.0.0:{}".format(self.DEFAULT_PORT),
        ]
        self.run_command(command_arguments)