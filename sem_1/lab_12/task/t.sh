#!/bin/bash

if [[ $# != 2 ]]; then
	exit 100
fi

dir=$1
extension=$2

maxfile_name=''
maxfile_size=0

for file in $(find "$dir" -type f -iname "*.$extension" -printf "%f\n"); do
	filesize=$(du -b "$dir/$file" | cut -f1)
	if [[ $filesize -gt $maxfile_size ]]; then
		maxfile_size=$filesize
		maxfile_name=$file
	fi
done

if [[ $maxfile_name == '' ]]; then
	exit 200
fi

echo $maxfile_name
echo $maxfile_size