#!/bin/sh
[ "$1" != "u" -a "$1" != "s" ] && echo Please give a parameter \"s\" or \"u\" for Sense or Unicorn HAT && exit 1
which jq
[ $? -ne 0 ] && echo jq is required to parse Jenkins JSON files - Grab it via https://stedolan.github.io/jq/ && exit 0
while true; do 
  curl https://ci.adoptopenjdk.net/api/json | jq -c '.jobs[] | {job: .name, status: .color}' | cut -d\" -f 4,8 | tr \" \   | grep openjdk.*build > ao.txt
  sudo python ./loop$1.py
done
