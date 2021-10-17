#!/bin/bash

filename=$1
project=$2
revision=$3
# delete all blank lines
content=`sed '/^$/d' $filename`

# delete first 3 lines
content=`echo "$content" | sed '1,3d'`

header="Project,Revision,Class,LCOM,DIT,IFANIN,CBO,NOC,RFC,NIM,NIV,WMC\n"

content=`echo "$content" | sed "1s/^/$header/"`

# Remove Metric names and keep values only
content=`echo "$content" | sed 's/\s\+\(.*\)\s\+\([0-9]\+\)/\2/g'`

# Mark class name lines
content=`echo "$content" | sed 's/\(.*\):$/,\1/g'`

# Make single line sperated with comma
content=`echo "$content" | paste -s -d ,` 

# Make lines for each class
content=`echo "$content" | sed 's/,,/\n/g'`

# Remove Anonymus Class
# e.g., org.apache.activemq.ActiveMQConnection.ActiveMQConnection.(Anon_1)
content=`echo "$content" | sed '/(Anon_[0-9]\+)/d'`

# sed '/^$/d' $1 | sed 's/\(.*\)\s\+\([0-9]\+\)/\2/g' | sed '\:$/ s/^/,/g'

echo "$content" | sed "2,\$s/^/$project,$revision,/g" > "$(dirname "$filename")"/$project_$revision'_ClassOOMetrics.csv'
