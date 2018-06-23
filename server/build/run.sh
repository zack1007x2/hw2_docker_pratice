#!/bin/bash
python receiver_ser.py &
inotifywait -m /usr/src/app/src -e create |
    while read path action file; do
          echo "The file '$file' appeared in directory '$path' via '$action'"
        #upload to server
        ext="${file##*.}"
        filename="${file%.*}"
        case "${ext}" in
          c)
           gcc ./src/$file -o ./src/${filename}".out"
           rm ./src/$file
           ;;
          cpp)
           g++ ./src/$file -o ./src/${filename}".out"
           rm ./src/$file
           ;;
          java)
           javac ./src/$file
           rm ./src/$file
           ;;
          class)
           python sent.py $file
           ;;
          out)
           python sent.py $file
           ;;
        esac
done