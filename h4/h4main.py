import os
def getFolderSize(path) :
    t = 0
    for e in os.scandir(path):
        if e.is_dir():
            t += getFolderSize(e.path)
        else:
            t += e.stat().st_size
    return t
t = getFolderSize("tools")
print ('Size= ', t)