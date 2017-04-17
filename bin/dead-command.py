#!/usr/bin/env python

from dead_command import DEADCommand


def main():
    """ DEAD Command line interface
    """
    dead_command = DEADCommand()
    dead_command.parse()

if __name__ == "__main__":
    main()