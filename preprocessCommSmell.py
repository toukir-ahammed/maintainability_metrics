import os
import pandas as pd

# df = pd.read_csv(os.path.join('./comm_smells','amq.csv'), sep='\t')
# print(df.head)

directory = os.path.join("./comm_smells/")
for root,dirs,files in os.walk(directory):
    for file in files:
       if file.endswith(".csv"):
        print(file)
        df = pd.read_csv(os.path.join('./comm_smells',file), sep='\t')
        df['Revision'] = df.apply(lambda x: x['cycle'].split(x['tag']+'-', 1), axis=1).str[-1]
        df['Comm_Smell'] = 'Smelly'
        df = df.rename(columns = {'name': 'Project', 'file': 'File'}, inplace = False)
        df = df[['Project', 'Revision', 'File', 'Comm_Smell']]

        df = df.drop_duplicates(subset=['File'])

        outfileName = os.path.splitext(file)[0] + '_comm_smell.csv'

        df.to_csv(os.path.join(directory,outfileName), index=False)
