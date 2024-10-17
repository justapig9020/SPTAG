#!/bin/bash

ini_file="./buildconfig.ini"
bin_file="../../Debug/ssdserving"
for ((i=2; i<=512; i*=2));
do
  line=55
  replace_text="NumberOfThreads=${i}"
  sed -i "${line}s/.*/${replace_text}/" $ini_file
  ${bin_file} ${ini_file} | tee  "saturate-${i}.log"
done
