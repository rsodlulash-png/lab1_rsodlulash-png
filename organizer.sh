#!/bin/bash

if [ ! -d "archive" ]; then
    mkdir archive
    echo "Archive directory created."
fi

timestamp=$(date +"%Y%m%d-%H%M%S")

echo $timestamp
