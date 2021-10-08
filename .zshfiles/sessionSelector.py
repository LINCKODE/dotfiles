import os

stream = os.popen("tmux list-sessions")
output = stream.read().split("\n")
print(output[0].split(":")[0])
