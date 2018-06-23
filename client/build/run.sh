#!/bin/bash
python receiver_cli.py &
inotifywait -m /usr/src/app/src -e close_write |
    while read path action file; do
          echo "The file '$file' appeared in directory '$path' via '$action'"
        #upload to server
        ext="${file##*.}"
        filename="${file%.*}"
        case "${ext}" in
          c)
           python sent.py $file
           ;;
          cpp)
           python sent.py $file
           ;;
          java)
           python sent.py $file
           ;;
        esac
done