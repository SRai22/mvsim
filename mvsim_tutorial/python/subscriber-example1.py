#!/usr/bin/env python3

# To test with a local build:
#
# export PYTHONPATH=$HOME/code/mvsim/build/lib/:$PYTHONPATH
# export PYTHONPATH=/tmp/install-mvsim/include/mvsim/:$PYTHONPATH

import pymvsim_comms
import time

if __name__ == "__main__":
    client = pymvsim_comms.mvsim.Client()
    client.setName("tutorial1")
    print("Connecting to server...")
    client.connect()
    print("Connected successfully.")
    time.sleep(2.0)
