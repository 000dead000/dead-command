#!/usr/bin/env python

from .common import Common

from .startproject import StartprojectCommand
from .os_dependencies import OSDependenciesCommand
from .pip_dependencies import PIPDependenciesCommand
from .update_package import UpdatePackageCommand
from .migrations import MigrationsCommand
from .bower_dependencies import BowerDependenciesCommand


class Commands(Common):
    def __init__(self, subparsers):
        """ Constructor
        """
        self.subparsers = subparsers
        self.register_commands()

    @staticmethod
    def get_commands_list():
        return [
            StartprojectCommand,
            OSDependenciesCommand,
            PIPDependenciesCommand,
            UpdatePackageCommand,
            MigrationsCommand,
            BowerDependenciesCommand,
        ]

    def register_commands(self):
        """ Register each command class to subparser
        """
        commands_classes = self.get_commands_list()

        for command_class in commands_classes:
            definition = command_class.get_definition()

            subparser = self.subparsers.add_parser(
                definition.get("name"),
                description=definition.get("description")
            )

            for argument in definition.get("arguments"):
                if argument.get("type"):
                    parameters = {
                        "type": argument.get("type"),
                    }
                else:
                    parameters = {
                        "action": "store_true",
                    }

                subparser.add_argument(
                    argument.get("short_flag"),
                    argument.get("long_flag"),
                    help=argument.get("help"),
                    **parameters
                )

    def identify_command(self, args):
        """ Get command class instance
        """
        subparser_name = args.subparser_name

        for command_class in self.get_commands_list():
            definition = command_class.get_definition()
            name = definition.get("name")

            if subparser_name == name:
                return command_class(args)

        return None
