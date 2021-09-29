#!/bin/bash

# Provide the source code repository and projectname as argument to run this script 
# e.g., ./und_analysis.sh /home/toukir/git/activemq/ activemq

SECONDS=0
und="/home/toukir/scitools/bin/linux64/und"


repo=$1
projectname=$2
resDir=$3
# echo $projectname

udb=$projectname.udb
# echo $udb

[ -d $resDir/$projectname ] || mkdir -p $resDir/$projectname
cd $resDir/$projectname

und create -db $udb -languages java

und -db $udb add $repo

# und settings -metrics all $udb
und settings -metrics "CountDeclMethod" "CountDeclMethodPublic" "CountDeclMethodPrivate" "CountDeclMethodProtected" "CountDeclClassMethod" $udb
# und settings -reports all $udb
und settings -reports "Class OO Metrics" "Class Metrics" $udb

und -quiet analyze -all $udb

und settings -MetricOutputFile $projectname\_metrics.csv $udb

# To see all settings
# und list -all settings $udb


und settings -ReportGenerateHTMLReport off $udb

echo "Time Elapsed: $SECONDS sec"

und metrics $udb
echo "Time Elapsed: $SECONDS sec"

und report $udb

echo "Time Elapsed: $SECONDS sec"
