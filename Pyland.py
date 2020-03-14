#!/usr/bin/python3
"""
pyland.

Usage:
    pyland run <f_or_s> [--output=<output_filename>]
    pyland about <frame_name>
    pyland show (--frame_dirs|--frames)
    pyland -h | --help
    pyland --version
    pyland --license
    pyland --author

Options:
    -h --help                       Show help options
    --version                       Show version and license information
    --author                        Show author's information
    --output=<output_filename>      Output file name when executing a frame command
                                    for storing the generated text in that file
    --frame_name                    Show information about the frame
    

"""

# License
# Copyright (C) 2020  Shakerin Ahmed
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.



from docopt import docopt
import json
from pathlib import Path
from ucg.PylandMaster import PylandMaster
from ucg.global_vars import *


PYLANDLICENSE = \
"""
  License
  Copyright (C) 2020  Shakerin Ahmed
 
  This program is free software: you can redistribute it and/or modify
  it under the terms of the GNU General Public License as published by
  the Free Software Foundation, either version 3 of the License, or
  (at your option) any later version.
 
  This program is distributed in the hope that it will be useful,
  but WITHOUT ANY WARRANTY; without even the implied warranty of
  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
  GNU General Public License for more details.
 
  You should have received a copy of the GNU General Public License
  along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

                
AUTHOR = (
            "Author: Shakerin Ahmed\n"
            "Email: shakerin.ahmed@gmail.com"
        )




default_config_file = '~/pyland.json'

execpath_config_file = 'pyland.json'

def getFrameDirs():

    default_cfg = Path(default_config_file)
    execpath_cfg = Path(execpath_config_file)

    if execpath_cfg.is_file():

        config_file = execpath_config_file


    elif default_cfg.is_file():

        config_file = default_config_file


    else:

        config_file = ""
        print("config file not present in '~' or './' directory,\n",
              "Please created ~/pyland.json or ./pyland.json file \n",
              "with frame_dirs information")


    frame_dirs = []

    if config_file != "":

        with open(config_file) as f:

            data = json.load(f)
            frame_dirs = data["frame_dirs"]


    return frame_dirs








def run(framecmd_or_structurefile, output_filename=""):

    frame_dirs = getFrameDirs()

    if len(frame_dirs) > 0:

        pmstr = PylandMaster(frame_dirs, framecmd_or_structurefile, output_filename)






def about(framename):

    frame_dirs = getFrameDirs()

    if len(frame_dirs) > 0:

        pmstr = PylandMaster(frame_dirs, framename, cmd="ABOUT")






def showFrames():

    framename = "NOTHING"
    frame_dirs = getFrameDirs()

    if len(frame_dirs) > 0:

        pmstr = PylandMaster(frame_dirs, framename, cmd="NOTHING")


    print("Total Frame Number: ", len(pmstr.TL1.frame_names))

    print("-------------------------")

    for each_frame in pmstr.TL1.frame_names:

        print(each_frame)

    print("-------------------------")


    return









def showFrameDirs():

    frame_dirs = getFrameDirs()
    print(frame_dirs)

    return











if __name__ == '__main__':

    args = docopt(__doc__, version='Pyland 1.0')


    if args['run']:

        if args['<f_or_s>']:

            if args['--output']:

                run(args['<f_or_s>'], args['--output'])

            else:
                run(args['<f_or_s>'])



    elif args['about']:

        about(args['<frame_name>'])



    elif args['show']:

        if args["--frame_dirs"]:

            showFrameDirs()


        elif args["--frames"]:

            showFrames()


        else:

            pass



    elif args['--license']:

        print(PYLANDLICENSE)



    elif args['--author']:

        print(AUTHOR)



    else:
        pass
    
