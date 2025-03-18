#!/usr/bin/python3
# Copyright (c) 2016,2022 SUSE LLC
# Copyright (c) 2024,2025 Siemens AG
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import argparse
import logging
import os
import re
import sys

from pprint import pprint

def do_cat(args):
    print("cat")
    for f in args.file:
        pprint(f)

def do_list(args):
    logging.info("list")

def main(args):

    # do some work here
    logger = logging.getLogger("boilerplate")
    logger.info("main")

    globals()["do_{}".format(args.command.replace('-', '_'))](args)

    return 0


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
                    description="boilerplate python commmand line program")
    parser.add_argument("--dry", action="store_true", help="dry run")
    parser.add_argument("--debug", action="store_true", help="debug output")
    parser.add_argument("--verbose", "-v", action="store_true", help="verbose")

    subparsers = parser.add_subparsers(dest="command", title="Commands")

    parser_list = subparsers.add_parser("list", help="list stuff")

    parser_cat = subparsers.add_parser("cat", help="cat stuff")
    parser_cat.add_argument("file", nargs='*', help="some file name")

    args = parser.parse_args()

    if not getattr(args, 'command', None):
        parser.print_help()
        sys.exit(1)

    if args.debug:
        level = logging.DEBUG
    elif args.verbose:
        level = logging.INFO
    else:
        level = None

    logging.basicConfig(level=level)

    sys.exit(main(args))

# vim: sw=4 et
