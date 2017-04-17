#!/usr/bin/env python

import os

from .common import Common
from .exceptions import DEADException
# from .bower_dependencies import DARCommandCommandsBower
# from os_dependencies import DARCommandCommandsOS
# from pip_dependencies import DARCommandCommandsPIP


class StartprojectCommand(Common):
    # Constants
    DEFAULT_NAME = "deadproject"
    DEFAULT_BASEDIR = None
    DEFAULT_OVERWRITE = False
    DJANGO_ADMIN = "django-admin.py"
    SKELETON_REPO = "https://github.com/000darfw000/dar-skeleton.git"

    def __init__(self, args):
        """ Constructor
        """
        self.DEFAULT_BASEDIR = self.get_instance_dir()

        self.args = args

        # Arguments
        self.name = None
        self.basedir = None
        self.overwrite = None

        self.parse_arguments()

    def parse_arguments(self):
        """ Parse arguments received from command line
        """
        # name
        name = getattr(self.args, "name")
        self.name = name if name else self.DEFAULT_NAME

        # basedir
        basedir = getattr(self.args, "basedir")
        self.basedir = basedir if basedir else self.DEFAULT_BASEDIR
        self.validate_basedir()

        # overwrite
        overwrite = getattr(self.args, "overwrite")
        self.overwrite = overwrite if overwrite else self.DEFAULT_OVERWRITE

    def validate_basedir(self):
        """ Validate base directory
        """
        if not self.directory_exists(self.basedir):
            raise DEADException({
                "message": "Invalid basedir",
                "path": self.basedir
            })

    @staticmethod
    def get_definition():
        return {
            "name": "startproject",
            "description": """Start a new project. This will create a project in the current directory where the command is 
                           executed. If no name is provided this will use 'deadproject'""",
            "arguments": [
                {
                    "short_flag": "-n",
                    "long_flag": "--name",
                    "help": """Directory name""",
                    "type": str,
                },
                {
                    "short_flag": "-b",
                    "long_flag": "--basedir",
                    "help": """Base directory, if not specified the project will be created in the
                            current location.""",
                    "type": str,
                },
                {
                    "short_flag": "-o",
                    "long_flag": "--overwrite",
                    "help": """If project directory exists, overwrite it."""
                },
            ],
        }

    @property
    def project_directory(self):
        """ Get project directory
        """
        return os.path.join(
            self.basedir,
            self.name
        )

    def execute(self):
        """ Execute
        """
        self.create_project_directory()
        self.goto_project_directory()
        self.create_django_project()
        # self.export_skeleton()
        # self.install_os_dependencies()
        # self.install_pip_dependencies()
        # self.install_bower()

    def create_project_directory(self):
        """ Create the project directory
        """
        path = self.project_directory

        if self.overwrite and self.directory_exists(path):
            try:
                self.remove_directory(path)
            except Exception as e:
                raise DEADException({
                    "message": "Error removing the project directory",
                    "path": path,
                    "exception_message": str(e),
                })

        try:
            os.mkdir(path)
        except Exception as e:
            raise DEADException({
                "message": "Error creating the project directory",
                "path": path,
                "exception_message": str(e),
            })

    def create_django_project(self):
        """ Create django project
        """
        self.run_command([
            self.DJANGO_ADMIN,
            "startproject",
            "conf",
            self.project_directory
        ])

    def goto_project_directory(self):
        """ Go to project directory
        """
        self.goto_directory(self.project_directory)

    def export_skeleton(self):
        """ Export dar-skeleton to the project
        """
        # url = u"{}/trunk/dar_skeleton/".format(
        #     self.SKELETON_REPO
        # )
        #
        # command_arguments = [
        #     "svn",
        #     "export",
        #     url
        # ]
        #
        # self.run_command(command_arguments)
        #
        # # Copy dar_skeleton content and remove this directory
        # dar_skeleton_dir = os.path.join(self.project_directory, "dar_skeleton")
        # self.mv(dar_skeleton_dir, self.project_directory)
        # self.remove_directory(dar_skeleton_dir)
        pass

    def install_os_dependencies(self):
        # DARCommandCommandsOS(self.args).execute()
        pass

    def install_pip_dependencies(self):
        # DARCommandCommandsPIP(self.args).execute()
        pass

    def install_bower(self):
        # DARCommandCommandsBower(self.args).execute()
        pass

