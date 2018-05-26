#!/bin/bash
inotifywait -m /usr/src/app/src -e close |
    while read path action file; do
        echo "The file '$file' appeared in directory '$path' via '$action'"
        #upload to server
    done
