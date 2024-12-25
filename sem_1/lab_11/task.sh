#!/bin/bash
echo hello
if [[ $# != 2 ]]; then
	exit 100
fi
if [[ ! ($2 =~ ^.$) ]]; then
	exit 200
fi
IFS="; "
for word in $1; do
	echo $word
done
exit 0
