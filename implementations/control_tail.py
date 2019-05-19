#!/usr/bin/env python3
import subprocess
import select
import os

def tail(): 
  # f = open(args[1], 'r')
  # curino = os.fstat(f.fileno()).st_ino
  # f.seek(0, os.SEEK_END)
  # f.seek(f.tell() - 1, os.SEEK_SET)
  # p = select.poll()
  # p.register(f.fileno())
  # while True:
  #   try:
  #     if p.poll():
  #       line = f.readline().rstrip()
  #       if line:
  #         print(watchline)
  #     if os.stat(args[1]).st_ino != curino:
  #       f2 = open(args[1], 'r')
  #       p.unregister(f.fileno())
  #       f.close()
  #       f = f2
  #       p.register(f.fileno())
  #       curino = os.fstat(f.fileno()).st_ino
  #   except IOError:
  #     pass
  #   except KeyboardInterrupt: 
  #     f.close()
  #     return

  files = os.listdir('.')
  for fn in files:
    f = subprocess.Popen(['tail', '-F', '-n0', fn], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    p = select.poll()
    p.register(f.stdout)
    while True:
      if p.poll(1):
        print(f.stdout.readline().rstrip())



if __name__ == "__main__":
  tail()64.242.88.10 - - [07/Mar/2004:16:06:51 -0800] "GET /twiki/bin/rdiff/TWiki/NewUserTemplate?rev1=1.3&rev2=1.2 HTTP/1.1" 200 4523
