#!/usr/bin/env python

import argparse

from .commands import Commands


class DEADCommand(object):
    def __init__(self):
        self.args = None
        self.parser = argparse.ArgumentParser(
            "DEAD Command Line Interface"
        )
        self.subparsers = self.parser.add_subparsers(
            dest='subparser_name'
        )

    def parse(self):
        # Get available commands
        commands = Commands(self.subparsers)

        # Get arguments
        self.args = self.parser.parse_args()

        # Identify command
        command = commands.identify_command(self.args)

        # Execute command
        command.execute()