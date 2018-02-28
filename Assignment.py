import os
import subprocess

#using smbclient to fetch the files from shared folder
#class shared_access:
   # def shared(self):
       # pass
      #  self.s1 = subprocess.call("smbclient //ltogateway9/share_folder -U Sanidhya")
     #   self.s2 = subprocess.call("get input.mp4")
    #    self.s3 = subprocess.call("quit")

    #lowraise calling through subprocess
   # def access(self):
  #      self.a1 = subprocess.call("ffmpeg -i input.mp4 -s 180x120 -c:a copy output.mp4")
 #       self.a2 = subprocess.call("mplayer -vo caca output.mp4")

#obj = shared_access()

#obj.shared()
#obj.access()
#src  = r'C:\path\to\source'
#dest = r'\\server-name\path-to-shared-directory'

# p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
# for file in os.listdir("smb://servername/sharedfolder")
#     print file

class RunCmd(object):
    def cmd_run(self, cmd):
        self.cmd = cmd
        subprocess.call(self.cmd, shell=True)
 #Sample usage

a = RunCmd()
a.cmd_run('get input.mp4')

