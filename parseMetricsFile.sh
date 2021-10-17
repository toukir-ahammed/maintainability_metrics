#!/bin/bash

filename=$1
project=$2
revision=$3

ClassOnly=`sed 's/Type Interface//g' "$filename" | sed 's/Class Template//g' | grep "^[^,]*\(Class\),"`
echo "$ClassOnly" | sed '/^Anonymous Class/d'