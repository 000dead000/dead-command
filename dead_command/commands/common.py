#!/usr/bin/env python

import os
import shutil
import subprocess


class Common(object):
    DEAD_COMMAND_PACKAGE = "git+https://github.com/000dead000/dead-command.git"
    DEFAULT_PORT = 9500

    @staticmethod
    def get_current_dir():
        return os.getcwd()

    @staticmethod
    def go_uplevel(path):
        return os.path.dirname(path)

    @staticmethod
    def get_package_dir():
        current_file = os.path.abspath(__file__)
        commands_dir = Common.go_uplevel(current_file)
        dead_command_dir = Common.go_uplevel(commands_dir)

        return dead_command_dir

    @staticmethod
    def directory_exists(path):
        return os.path.isdir(path)

    @staticmethod
    def remove_directory(path):
        shutil.rmtree(path)

    @staticmethod
    def goto_directory(path):
        os.chdir(path)

    @staticmethod
    def run_command(arguments):
        subprocess.call(arguments)

    @staticmethod
    def mv(source, target):
        for item in os.listdir(source):
            source_item = os.path.join(
                source,
                item
            )
            target_item = os.path.join(
                target,
                item
            )
            shutil.move(source_item, target_item)
