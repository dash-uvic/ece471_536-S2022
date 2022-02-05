#!/bin/bash

# Occasionally, when running all the levels Pygame would freeze if quiet=False. 
# Do avoid this (or to run a specific set of levels) you can 
# use a script to run each level in a loop

duration=60
for x in `seq 1 819`; do 
    #Run level $x
    python duck_hunt_main.py -l $x -d $duration; 
    #Get error code
    rc=$?; 
    if [ $rc -ne 0 ]; then
        echo "Return with an error for level $x, exit"
        break
    fi
done
