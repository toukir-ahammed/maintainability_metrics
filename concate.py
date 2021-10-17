import os
import util
resDir = '/home/toukir/maintainabilty_metrics/results'
projects = os.listdir(resDir)

# projects = ['amq']

for project in projects:
    print(project)

    cmd = 'sed 1q ' + 'results/' + project + '/*/*_maintainability_metrics_unique.csv' + \
        '>' + 'concated/' + project + '.csv'
    print(cmd)
    os.system(cmd)

    cmd = 'sed -s 1d ' + 'results/' + project + '/*/*_maintainability_metrics_unique.csv' + \
        '>>' + 'concated/' + project + '.csv'
    print(cmd)
    os.system(cmd)

# sed 1q *.csv > ../all.csv
# sed 1d *.csv >> ../all.csv
