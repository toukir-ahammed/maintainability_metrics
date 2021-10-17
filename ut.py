import yaml
import sys
import os
import subprocess

projects = os.listdir('conf')

print(projects)

for project in projects:
    config = yaml.load(open('conf/'+project))
    print(project,':',len(config['revisions']))

# print('Loading Configuartion file......')

# config = yaml.load(open('conf/' + projectName + '.conf'))

# for rev in config['revisions']:
#     print('Analysing Revision ' + rev)
#     os.system('git -C ' + repo + ' checkout ' + rev)
    
#     print('Checked out to the following tags:')
#     os.system('git -C ' + repo + ' describe --tags')
    
#     print("Analysing using understand.....")
    
#     os.system('./understand.sh ' + repo + ' ' + rev + ' ' + resDir)

# print("\nAnalysis done for project " + projectName)

