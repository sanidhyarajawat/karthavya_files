# Import the module
# import subprocess
import logging
import subprocess
from glob import glob
import os

logging.basicConfig(filename='myprogram.log', level=logging.DEBUG)

class RunCmd1(object):
	def cmd_run1(self, cmd):
		self.cmd = cmd
		subprocess.call(self.cmd, shell=True)

try:
	logging.info('Starting remote connection>>>')
	a = RunCmd1()
	#To remove previously generated file
	# for filename in glob("output.mp4"):
	#  	os.renames(output.mp4, outputnew.mp4)
	a.cmd_run1('smbclient //ltogateway9/share_folder -U Sanidhya -c "get input.mp4"')
	logging.info('Connection created\n')
	a.cmd_run1('ffmpeg -i input.mp4 -s 180x120 -c:a copy output.mp4')
	#a.cmd_run1('mplayer -vo caca output.mp4') This and below commands are same
	a.cmd_run1('xdg-open output.mp4')
	logging.info('Output generated\n')
except:
	logging.info('Unable to connect')