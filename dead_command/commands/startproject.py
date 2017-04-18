#!/usr/bin/env python

import os

from .common import Common
from .exceptions import DEADException
from .os_dependencies import OSDependenciesCommand
from .pip_dependencies import PIPDependenciesCommand
# from .bower_dependencies import DARCommandCommandsBower


class StartprojectCommand(Common):
    # Constants
    DEFAULT_NAME = "deadproject"
    DEFAULT_BASEDIR = None
    DEFAULT_OVERWRITE = False
    DJANGO_ADMIN = "django-admin.py"
    SKELETON_REPO = "https://github.com/000dead000/dead-skeleton.git"

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
        self.export_skeleton()
        self.os_dependencies()
        self.pip_dependencies()
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

        def adjust_settings(self):
            conf_orig = os.path.join(
                self.project_directory,
                "conf.orig"
            )

            conf = os.path.join(
                self.project_directory,
                "conf"
            )

            self.mv(conf_orig, conf)
            self.remove_directory(conf_orig)

            # add custom_settings call in settings.py
            settings = os.path.join(
                self.project_directory,
                "conf",
                "settings.py"
            )

            f = open(settings, "r")
            contents = f.read()
            f.close()

            contents += """
    try:
        execfile(os.path.join(BASE_DIR, 'conf', 'custom_settings.py'))
    except IOError:
        pass"""

            f = open(settings, "w")
            f.write(contents)
            f.close()

            """
            settings = os.path.join(
                self.project_directory,
                "conf",
                "custom_settings.py"
            )

            f = open(settings, "r")
            contents = f.read()
            f.close()

            contents = contents.replace("SLUG_PLACEHOLDER", self.slug)
            contents = contents.replace("SHORT_TITLE_PLACEHOLDER", self.short_title)
            contents = contents.replace("LONG_TITLE_PLACEHOLDER", self.long_title)
            contents = contents.replace("DOMAIN_PLACEHOLDER", self.domain)
            contents = contents.replace("EMAIL_USER_PLACEHOLDER", self.email)
            contents = contents.replace("EMAIL_PASSWORD_PLACEHOLDER", self.password)
            contents = contents.replace("EMAIL_BCC_RECIPIENT_PLACEHOLDER", self.email_bcc_recipient)

            f = open(settings, "w")
            f.write(contents)
            f.close()
            """

    def export_skeleton(self):
        """ Export dar-skeleton to the project
        """
        url = u"{}/trunk/dead_skeleton/".format(
            self.SKELETON_REPO
        )

        command_arguments = [
            "svn",
            "export",
            url
        ]

        self.run_command(command_arguments)

        # Copy dead_skeleton content and remove this directory
        dead_skeleton_dir = os.path.join(self.project_directory, "dead_skeleton")
        self.mv(dead_skeleton_dir, self.project_directory)
        self.remove_directory(dead_skeleton_dir)
        self.register_settings()

    def os_dependencies(self):
        OSDependenciesCommand(self.args).execute()

    def pip_dependencies(self):
        PIPDependenciesCommand(self.args).execute()

    def install_bower(self):
        # DARCommandCommandsBower(self.args).execute()
        pass

