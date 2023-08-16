import subprocess

out = (subprocess.getstatusoutput('hostname -I')[1]).split()
out.append(subprocess.getstatusoutput('hostname -A')[1])
print(out)
