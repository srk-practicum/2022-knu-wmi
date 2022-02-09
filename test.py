import os
from os.path import join, isfile
import errno, os, stat, shutil

def removeFolder(folderPath: str):
    filesNames = os.listdir(folderPath)
    for fileName in filesNames:
        if isfile(join(folderPath, fileName)):
            os.remove(join(folderPath, fileName))
        else:
            removeFolder(join(folderPath, fileName))
    os.rmdir(folderPath)

def handleRemoveReadonly(func, path, exc):
  excvalue = exc[1]
  if func in (os.rmdir, os.remove) and excvalue.errno == errno.EACCES:
      os.chmod(path, stat.S_IRWXU| stat.S_IRWXG| stat.S_IRWXO) # 0777
      func(path)
  else:
      raise

shutil.rmtree("dataset1")




# removeFolder("dataset1")

