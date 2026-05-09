#!/usr/bin/bash

 res=$(curl -s https://api.github.com/repos/Tipix-dev/OLS/releases | jq '[.[].assets[].download_count] | add')

 echo "download_count: $res"
