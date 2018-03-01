#!/bin/bash

cwd=$(pwd)

if [ ! -L /usr/bin/decoder ];
then
	sudo ln -s $cwd/decoder.py /usr/bin/decoder
else
	echo "El programa decoder ya está instalado, elimínalo de /usr/bin"
fi
