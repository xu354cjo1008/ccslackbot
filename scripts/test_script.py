#!/usr/bin/python
import subprocess
cmd_line = "mpstat 1 10"
p = subprocess.Popen(cmd_line, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
#out = p.communicate()[0]
#print(out)
with p.stdout:
    for line in iter(p.stdout.readline, b''):
        print(line),
p.wait()
