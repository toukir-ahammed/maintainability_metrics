import os
import util
import pandas as pd
dir = '/home/toukir/maintainabilty_metrics/stat_analysis'
projects = os.listdir(dir)

# projects = ['poi']

for project in projects:
    print(project)
    metrics = os.path.join(dir, project, project + '.csv')
    commsmell = os.path.join(dir, project, project + '_comm_smell.csv')

    # print(metrics, commsmell)

    df1 = pd.read_csv(metrics)
    df2 = pd.read_csv(commsmell)

    df = pd.merge(df1, df2, how = 'left', on=['Project', 'Revision', 'File'])

    df['Comm_Smell'] = df['Comm_Smell'].fillna('NonSmelly')

    print(df1.shape, df2.shape, df.shape)
    # print(df.head)

    outfileName = os.path.join(dir, project, project + '_combined.csv')


    df.to_csv(outfileName, index=False)