import os
import util
resDir = '/home/toukir/maintainabilty_metrics/results'
projects = os.listdir(resDir)

for project in projects:
    print(project)
    for revision in os.listdir(os.path.join(resDir,project)):
        print('--' + revision)
        classMetricsFile = os.path.join(resDir,project,revision, revision + '_text', 'ClassMetrics.txt')
        classOOMetricsFile = os.path.join(resDir,project,revision, revision + '_text', 'ClassOOMetrics.txt')
        
        print('----' + os.path.abspath(classMetricsFile))
        # os.system('./parseClassMetrics.sh ' + os.path.abspath(classMetricsFile) + ' ' + project + ' ' + revision)

        print('----' + os.path.abspath(classOOMetricsFile))
        # os.system('./parseClassOOMetrics.sh ' + os.path.abspath(classOOMetricsFile) + ' ' + project + ' ' + revision)

        classMetricsFile = os.path.join(resDir,project,revision, revision + '_text', revision + '_ClassMetrics.csv')
        classOOMetricsFile = os.path.join(resDir,project,revision, revision + '_text', revision + '_ClassOOMetrics.csv')
        metricsFile = os.path.join(resDir,project,revision, revision + '_metrics.csv')
        outputFile = os.path.join(resDir,project,revision, revision + '_maintainability_metrics_unique.csv')


        util.mergeMetrics(classMetricsFile,classOOMetricsFile,metricsFile,outputFile)