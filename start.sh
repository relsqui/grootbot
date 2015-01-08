#!/bin/sh

./main.py $* 2>>log & tail -f log
