#!/usr/bin/env python

from builtins import input
import os
import sys
import subprocess

THISDIR = os.path.dirname(os.path.abspath(__file__))

args = [sys.executable, "setup.py", "sdist", "bdist_wheel", "upload"]
returncode = subprocess.call(args, cwd = THISDIR)
if returncode != 0:
    input("Press ENTER to continue...")
