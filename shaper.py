 # Copyright (c) 2013 Samuel Giles

 # Permission is hereby granted, free of charge, to any person obtaining a copy
 # of this software and associated documentation files (the "Software"), to deal
 # in the Software without restriction, including without limitation the rights
 # to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 # copies of the Software, and to permit persons to whom the Software is
 # furnished to do so, subject to the following conditions:

 # The above copyright notice and this permission notice shall be included in
 # all copies or substantial portions of the Software.

 # THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 # IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 # FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 # AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 # LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 # OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
 # THE SOFTWARE.

import signal
import sys
import argparse
import os

from subprocess import call
from pprint import pprint

if os.getuid() is not 0:
    print "Must be root: use sudo shaper.py"
    sys.exit(1);


parser = argparse.ArgumentParser(prog='shaper',description='Shape Mac OS X network traffic.')
parser.add_argument('-d', dest='delay', type=int, help='The propagation delay', required=True)
parser.add_argument('-bw', dest='bandwidth', type=int, help='The up and down bandwidth in KBit/s', required=True)
parser.add_argument('-pl', dest='packet_loss', type=int, help='The percentage of packets lost', required=True)

args = parser.parse_args()


def signal_handler(signal, frame):
        print 'Restoring network'
        call(["ipfw", "delete", "1"])
        sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

call(["ipfw", "pipe", "1", "config", "bw", str(args.bandwidth) + "Kbit/s", "delay", str(args.delay), "plr", str(args.packet_loss / 100)])
call(["ipfw", "add", "1", "pipe", "1", "ip", "from", "any", "to", "any"])

print 'Press Ctrl+C to restore'
signal.pause()
