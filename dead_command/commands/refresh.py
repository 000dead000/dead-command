#!/usr/bin/env python

from .common import Common
from .os_dependencies import OSDependenciesCommand
from .pip_dependencies import PIPDependenciesCommand
from .bower_dependencies import BowerDependenciesCommand
from .migrations import MigrationsCommand


class RefreshCommand(Common):
    def __init__(self, args):
        """ Constructor
        """
        self.args = args

    @staticmethod
    def get_definition():
        return {
            "name": "refresh",
            "description": """This command runs migrations, os_dependencies, pip_dependencies, bower_dependencies'""",
        }

    def execute(self):
        """ Execute
        """
        MigrationsCommand(self.args).execute()
        OSDependenciesCommand(self.args).execute()
        PIPDependenciesCommand(self.args).execute()
        BowerDependenciesCommand(self.args).execute()
