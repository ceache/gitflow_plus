#!/usr/bin/env python
"""
git-flow

.. program:: git flow

.. cmdoption:: -v, --verbose

       Produce more output.

.. cmdoption:: -h, --help

       Print usage, help and information on the available commands.

"""
#
# This file is part of `gitflow`.
# Copyright (c) 2010-2011 Vincent Driessen
# Copyright (c) 2012-2013 Hartmut Goebel
# Distributed under a BSD-like license. For full terms see the file LICENSE.txt
#

import argparse
import os
import sys

#from gitflow.core import GitFlow
from gitflow.util import itersubclasses
from gitflow.flow_exceptions import (GitflowError)
from gitflow.util import StringFormatter
from gitflow.flow_tasks import GitFlowCommand
from gitflow.config.configmanager import ConfigManager


__copyright__ = "2013 Willie Slepecki; Based on code written by: 2010-2011 Vincent Driessen; 2012-2013 Hartmut Goebel"
__license__ = "BSD"
__configFile__ = ".gitflow"


def die(*texts):
    raise SystemExit('\n'.join(map(str, texts)))


class NotEmpty(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        if not values:
            raise argparse.ArgumentError(self, 'must not by empty.')
        setattr(namespace, self.dest, values)




"""
class InitCommand(GitFlowCommand):
    @classmethod
    def register_parser(cls, parent):
        #flow = GitFlow()


        This code is more than just showing the init message.
        it also checks to see if the system is properly configured
        or not.  git flow plus stores its configs in a file on the
        file system, not the git configuration.  That way the configs
        can be shared between multiple developers.  The only thing stored
        in the local config is a flag indicating that the file on the
        file system was checked and the branches exist

        fullFileName = os.path.join(os.getcwd(), __configFile__)

        #initConfig = flow.is_set("gitflowPlus.initialized")
        initFile = os.path.exists(fullFileName)

        string = StringFormatter()

        #if not initConfig and not initFile:
        #    initMsg = string.colorText(string.LIGHT_RED,
        #                               "GitFlow config file and config flag not set, please run init to install gitflow plus in this repository")
        #elif initConfig and not initFile:
       #     initMsg = string.colorText(string.LIGHT_RED,
        #                               "GitFlow flag is set but config file is missing.  Please pull your code again as gitflow will not operate without the config file")
        #elif not initConfig and initFile:
        #    initMsg = string.colorText(string.LIGHT_RED,
        #                               "GitFlow config file found but has not been imported, please run init so initialize your repository")
        #else:
        #    initMsg = "Initialize a repository for gitflow."

        #p = parent.add_parser('init',
        #                      help=initMsg)
        #p.add_argument('-f', '--force', action='store_true',
        #               help='Force reinitialization of the gitflow preferences.')
        #p.add_argument('-d', '--defaults', action='store_true',
        #               dest='use_defaults',
        #               help='Use default branch naming conventions and prefixes.')
        #p.set_defaults(func=cls.run)
        #return p

    @staticmethod
    def run(args):
        from . import _init

        _init.run_default(args)
"""

def main():
    #print("hi mom")

    parser = argparse.ArgumentParser(prog='git flow')
    placeholder = parser.add_subparsers(title='Subcommands')

    for cls in itersubclasses(GitFlowCommand):
        cls.register_parser(placeholder)
        #print(cls)

    args = parser.parse_args()

    try:
        args.func(args)
    except KeyboardInterrupt:
        raise SystemExit('Aborted by user request.')


if __name__ == '__main__':
    try:
        main()
    except (GitflowError) as e:
        raise SystemExit('Error: %s' % e)
