#!/usr/bin/env bash

if ! cat ~/.bashrc | grep "export PATH=$PATH:~/bin" > /dev/null 2>&1; then
  cp -r bin ~/
  echo "export PATH=$PATH:~/bin" >> ~/.bashrc
fi

if ! cat ~/.bashrc | grep "export zipnator=$(find ~/ -type d -name 'zipnator')" > /dev/null 2>&1; then
  echo "export zipnator=$(find ~/ -type d -name 'zipnator')" >> ~/.bashrc
fi

# Reloading terminal
source ~/.bashrc
