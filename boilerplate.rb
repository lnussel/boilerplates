#!/usr/bin/ruby
# Copyright (c) 2015 SUSE Linux GmbH
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

require 'optparse'
require 'singleton'
require 'logger'

class GlobalLogger

  include Singleton

  attr_accessor :log

  def initialize
    @log = Logger.new($stderr)
    @log.level = ::Logger::ERROR
    @log.formatter = proc do |severity, datetime, progname, msg|
      "#{severity}: #{msg}\n"
    end

  end

end

module DefaultLogger

  def log
    GlobalLogger.instance.log
  end

  def self.included(base)
    base.extend self
  end
end

class CommandLineInterface
  attr_reader :options

  include DefaultLogger

  def initialize(argv)
    @options = {}

    parser = OptionParser.new

    parser.banner += ' XXX'

    parser.separator ''
    parser.separator 'Options:'

    parser.on('--debug', 'debug output') do
      @options[:debug] = true
      log.level = ::Logger::DEBUG
    end
    parser.on('--verbose', 'verbose output') do
      @options[:verbose] = true
      log.level = ::Logger::INFO
    end
    parser.on("-h","--help","help") do
      puts parser
      exit(0)
    end

    begin
      parser.parse(argv)
    rescue OptionParser::InvalidOption => e
      log.error e.message
      puts parser
      exit(1)
    end
    if argv.empty?
      puts parser
      exit(1)
    end
  end
end

cli = CommandLineInterface.new(ARGV)

# vim:sw=2 et
