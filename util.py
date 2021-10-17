import pandas as pd
import re


def mergeMetrics(classMetricsFile, classOOMetricsFile, metricsFile, outputFile):

    classMetrics = pd.read_csv(classMetricsFile)
    classOOMetrics = pd.read_csv(classOOMetricsFile)
    metrics = pd.read_csv(metricsFile)

    # print(classMetricsFile, classOOMetricsFile, metricsFile)

    classMetrics = classMetrics.drop_duplicates(subset=['Class'])
    classOOMetrics = classOOMetrics.drop_duplicates(subset=['Class'])
    metrics = metrics.drop_duplicates(subset=['Name'])

    merged = pd.merge(classMetrics, classOOMetrics, how='inner', on=[
                      'Project', 'Revision', 'Class'])

    allmerged = pd.merge(merged, metrics, how='inner',
                         left_on='Class', right_on='Name')

    allmerged = allmerged.rename(
        columns={
            'Lines': 'NL',
            'Lines Code': 'LOC',
            'Lines Comment': 'CLOC',
            'Ratio Comment to Code': 'RCC',
            'CountDeclMethod': 'NOM'
        }
    )

    totalMethods = allmerged['CountDeclMethodPublic'] + \
        allmerged['CountDeclMethodPrivate'] + \
        allmerged['CountDeclMethodProtected']
    allmerged['RPM'] = round(
        allmerged['CountDeclMethodPublic']/totalMethods, 2)
    allmerged['RSM'] = round(allmerged['CountDeclClassMethod']/totalMethods, 2)

    allmerged['RPM'] = allmerged['RPM'].fillna(0)
    allmerged['RSM'] = allmerged['RSM'].fillna(0)

    allmerged = allmerged[['Project', 'Revision', 'Class', 'File', 'NL', 'LOC', 'CLOC', 'RCC',
                           'LCOM', 'DIT', 'IFANIN', 'CBO', 'NOC', 'RFC', 'NIM', 'NIV', 'WMC', 'NOM', 'RPM', 'RSM']]
    # print(allmerged.head())

    # allmerged.to_csv(outputFile, index=False)

    # Keep Class matching File name
    df = allmerged
    df = df[df['Class'].str.split(
        '.').str[-1] == df['File'].str.split('/').str[-1].str.split('.').str[-2]]
    
    df['File'] = df['File'].str.split('/home/toukir/maintainabilty_metrics/').str[-1].str.split('/',1).str[-1]

    df.to_csv(outputFile, index=False)

    
