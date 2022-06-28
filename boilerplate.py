#!/usr/bin/python3
# Copyright (c) 2016,2022 SUSE LLC
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

import cmdln
import logging
import os
import re
import sys

from pprint import pprint


class BoilderPlate(cmdln.Cmdln):
    def __init__(self, *args, **kwargs):
        cmdln.Cmdln.__init__(self, args, kwargs)

    def get_optparser(self):
        parser = cmdln.CmdlnOptionParser(self)
        parser.add_option("--dry", action="store_true", help="dry run")
        parser.add_option("--debug", action="store_true", help="debug output")
        parser.add_option("--verbose", action="store_true", help="verbose")
        return parser

    def postoptparse(self):
        level = None
        if self.options.debug:
            level = logging.DEBUG
        elif self.options.verbose:
            level = logging.INFO

        logging.basicConfig(level=level, format='%(module)s:%(lineno)d %(levelname)s %(message)s')

        self.logger = logging.getLogger(self.optparser.prog)

    @cmdln.option("-f", "--force", action="store_true",
                  help="force something")
    def do_foo(self, subcmd, opts, *args):
        """${cmd_name}: foo bar

        ${cmd_usage}
        ${cmd_option_list}
        """


if __name__ == "__main__":
    app = BoilderPlate()
    sys.exit(app.main())

# vim: sw=4 et
