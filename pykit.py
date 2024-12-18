#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
 (c) 2023 - Copyright CTyunOS Inc

 Authors:
   youyifeng <youyf2@chinatelecom.cn>

"""

import logging
import os
import sys
from logging.handlers import RotatingFileHandler
import argparse

import cve_ease as ease
from cve_ease import to_list

from cve_ease.commands import *


def check_python_version():
    current_python = sys.version_info[0]
    if current_python == 3:
        return
    else:
        raise ease.GenericError('Invalid python version requested: %d' % current_python)



def load_commands(subparsers):
    commands = {}
    for sub_class in BaseCommand.__subclasses__():
        commands[sub_class.__doc__] = sub_class
        sub_class.register(subparsers)
    return commands

def main():
    # check run in correct python version
    check_python_version()
    # parse config from cmdline and configfile

    # make sure workdir exists
    main = ease.gconfig['main']
    ease.ensuredir(main['workdir'])
    # log configuration
    logger = logging.getLogger("cve-ease")
    console_handler = logging.StreamHandler(sys.stderr)
    console_handler.setFormatter(logging.Formatter('%(asctime)s [%(levelname)s] %(name)s: %(message)s'))
    logger.addHandler(console_handler)

    if main['log_file']:
        logfile = os.path.join(main['workdir'], main['log_file'])
        file_handler = RotatingFileHandler(
            filename=logfile,
            encoding='UTF-8',
            maxBytes=int(main['log_maxbytes']),
            backupCount=int(main['log_backup_num'])
        )
        file_handler.setFormatter(logging.Formatter('%(asctime)s [%(levelname)s] %(name)s: %(message)s'))
        logger.addHandler(file_handler)
    log_level = main['log_level']
    if 'debug' == log_level:
        logger.setLevel(logging.DEBUG)
    elif 'warn' ==log_level:
        logger.setLevel(logging.WARN)
    elif 'error' == log_level:
        logger.setLevel(logging.ERROR)
    else:
        logger.setLevel(logging.INFO)


    parser = argparse.ArgumentParser(description="CVE漏洞扫描工具")
    subparsers = parser.add_subparsers(dest="command")

    commands = load_commands(subparsers)

    args = parser.parse_args()
    command = args.command

    if command in commands:
        command_class = commands[command]()
        command_class.handle(args)
    else:
        parser.print_help()


    # 加载子命令


if __name__ == "__main__":
    main()