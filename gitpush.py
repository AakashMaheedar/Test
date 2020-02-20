import os
cmd1 = 'git init'
os.system(cmd1)
cmd1_1 = 'cd /Users/aaakasha/Workstore/Feb/sampleApp'
cmd2 = 'git add  .'
os.system(cmd1_1)
cmd2_2 ='git status'
os.system(cmd2)
os.system(cmd2_2)
cmd3 = 'git commit -m "My first File"'
os.system(cmd3)
cmd4 = 'git remote add origin https://github.com/AakashMaheedar/Test'
os.system(cmd4)
os.system(cmd2_2)
cmd5 = 'git pull origin master'
os.system(cmd5)
cmd6 = 'git push -u origin master'
os.system(cmd6)
