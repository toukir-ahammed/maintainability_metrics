import yaml
import sys
import os
import subprocess


projectName = sys.argv[1]
repoLink = sys.argv[2]

print("Cloning repository......")
os.system('git clone ' + repoLink + ' ' + projectName + '-repo')

repo = os.path.abspath(projectName + '-repo')
resDir = os.path.abspath('results/'+ projectName)
print('Loading Configuartion file......')

config = yaml.load(open('conf/' + projectName + '.conf'))

for rev in config['revisions']:
    print('Analysing Revision ' + rev)
    os.system('git -C ' + repo + ' checkout ' + rev)
    
    print('Checked out to the following tags:')
    os.system('git -C ' + repo + ' describe --tags')
    
    print("Analysing using understand.....")
    
    os.system('./understand.sh ' + repo + ' ' + rev + ' ' + resDir)

print("\nAnalysis done for project " + projectName)

