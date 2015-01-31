#!/usr/bin/env python

# This small project aims to build a branded Atom-shell
# directly from the atom-shell sources. It assumes that
# you have all necessary tools available in your computer.
#
# If the build is not successful, refer to the Atom-shell
# documentation at https://github.com/atom/atom-shell/.
# Follow the suggestions to build from the source and try
# to find which tools are missing!

import shutil
import os
import subprocess
import sys



# == Parameters (edit these) == #

configuration = 'Release'  # Release / Debug
project_name = 'myapp'
product_name = 'MyApp'



# == Build sequence (do not edit) == #

# Get the code from git
subprocess.call('git clone https://github.com/atom/atom-shell.git', shell=True)

# Bootstrap code
command = 'cd atom-shell;'
command += 'python script%sbootstrap.py -v;' % (os.sep)
os.environ['GYP_DEFINES'] = 'project_name=%s product_name=%s' % (project_name, product_name)
subprocess.call(command, shell=True)

# Replace resources folder
src = 'resources'
dst = os.sep.join(['atom-shell', 'atom', 'browser', 'resources'])
shutil.rmtree(dst, ignore_errors=True)
shutil.copytree(src, dst)

# Do a micro-clean (useful when replacing resources after a build)
dst = os.sep.join(['atom-shell', 'out', configuration, product_name])
for ext in ['', '.exe', '.app']:
    try:
        if (ext == '.app'):
            shutil.rmtree(dst + ext, ignore_errors=True)
        else:
            os.remove(dst + ext)
    except OSError:
        pass

# Build
command = 'cd atom-shell;'
command += 'python script%sbuild.py -c %s -t %s;' % (os.sep, configuration, project_name)
subprocess.call(command, shell=True)

# Show 'build' directory
dst = os.sep.join(['atom-shell', 'out', configuration, ''])
print 'Build folder is %s' % (dst)

