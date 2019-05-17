#!/usr/bin/env python3
import os
import time
import sys
from queue import Queue
from threading import Thread

def tail(fn, sleep=0.1):
  f = open(fn)
  curino = os.fstat(f.fileno()).st_ino
  f.seek(0, os.SEEK_END)
  while True:
    line = f.readline()

    if line:
      sys.stdout.write(line)
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

def multitail(i, q):
    while True:
      fn = q.get()
      ret = tail(fn)
      q.task_done()
if __name__ == "__main__":
  queue = Queue()
  log_files = os.listdir('.')
  num_threads = len(log_files)

  for i in range(num_threads):
    thread = Thread(target=multitail, args=(i, queue))
    thread.setDaemon(True)
    thread.start()

  for fn in log_files:
    queue.put(fn)

  queue.join()