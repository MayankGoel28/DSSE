#!/usr/bin/env bash
if [ $# -lt 1 ] 
then 
    echo -e "USAGE: ./merge.sh <category name or common prefix>"
    exit 1
fi 

cat "$1"-* > "$1".json
sed -i 's/\]\[/,/g' "$1".json
