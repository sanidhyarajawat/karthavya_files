import subprocess

class RunCmd(object):
	def cmd_run(self, cmd):
		self.cmd = cmd
		subprocess.call(self.cmd, shell=True)
a = RunCmd()

proc = subprocess.Popen(['python', 'abc.py'],  stdin=subprocess.PIPE, stdout=subprocess.PIPE)
proc.communicate()
