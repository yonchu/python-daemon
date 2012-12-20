#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
import sys
import time
from daemon import Daemon

PIDFILE = '/tmp/daemon-example.pid'


class MyDaemon(Daemon):
    def run(self):
        i = 0
        while True:
            i += 1
            if i > 30:
                break
            time.sleep(1)

if __name__ == "__main__":
    daemon = MyDaemon(PIDFILE, verbose=1)
    if len(sys.argv) == 2:
        if 'start' == sys.argv[1]:
            daemon.start()
        elif 'stop' == sys.argv[1]:
            daemon.stop()
        elif 'restart' == sys.argv[1]:
            daemon.restart()
        else:
            print('Unknown comcand')
            sys.exit(2)
        sys.exit(0)
    else:
        print('usage: %s start|stop|restart' % sys.argv[0])
        sys.exit(2)
