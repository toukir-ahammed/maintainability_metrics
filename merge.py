

data1 = pd.read_csv('/home/toukir/maintainabilty_metrics/test/activemq-5.16.1_ClassMetrics.csv')
print(data1.shape)
data1 = data1.drop_duplicates(subset=['Class'])
print(data1.shape)

data2 = pd.read_csv('/home/toukir/maintainabilty_metrics/test/activemq-5.16.1_ClassOOMetrics.csv')
print(data2.shape)
data2 = data2.drop_duplicates(subset=['Class'])
print(data2.shape)

merged = pd.merge(data1, data2, how='inner', on=['Project', 'Revision', 'Class'])
print(merged.shape)

data3 = pd.read_csv('/home/toukir/maintainabilty_metrics/test/activemq-5.16.1_metrics.csv')
print(data3.shape)
data3 = data3.drop_duplicates(subset=['Name'])
print(data3.shape)

allmerged = pd.merge(merged,data3, how='inner', left_on='Class', right_on='Name')
print(allmerged.shape)

allmerged = allmerged.rename(
    columns={
        'Lines': 'NL',
        'Lines Code': 'LOC',
        'Lines Comment': 'CLOC',
        'Ratio Comment to Code': 'RCC',
        'CountDeclMethod': 'NOM'
        }
    )

totalMethods = allmerged['CountDeclMethodPublic'] + allmerged['CountDeclMethodPrivate'] + allmerged['CountDeclMethodProtected']
allmerged['RPM'] = round(allmerged['CountDeclMethodPublic']/totalMethods, 2)
allmerged['RSM'] = round(allmerged['CountDeclClassMethod']/totalMethods,2)

allmerged['RPM'] = allmerged['RPM'].fillna(0)
allmerged['RSM'] = allmerged['RSM'].fillna(0)

allmerged = allmerged[['Project','Revision','Class','File','NL','LOC','CLOC','RCC','LCOM','DIT','IFANIN','CBO','NOC','RFC','NIM','NIV','WMC','NOM','RPM','RSM']]
# print(allmerged.head())
allmerged.to_csv('/home/toukir/maintainabilty_metrics/test/activemq-5.16.1_AllMergedClassMetrics.csv', index = False)