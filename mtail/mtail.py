import time
import sys
import os
import multiprocessing

def tail(fn, sleep=0.1):
  try:
    f = open(fn)
    curino = os.fstat(f.fileno()).st_ino
    f.seek(0, os.SEEK_END)
    while True:
      line = f.readline()

      if line:
        sys.stdout.write("{}: {}".format(fn, line))
      else:
        time.sleep(sleep)
      
      try:
        if os.stat(fn).st_ino != curino:
          f2 = open(fn)
          f.close()
          f = f2
          curino = os.fstat(f.fileno()).st_ino
      except IOError:
        pass
  except KeyboardInterrupt:
    f.close()

def mtail():
  try: 
    files = os.listdir('.')
    tails = []
    for fn in files:
      if os.path.isdir('./' + fn):
        continue
      p = multiprocessing.Process(target=tail, args=(fn,))
      tails.append(p)
      p.start()
  except KeyboardInterrupt:
    for p in tails:
      p.terminate()