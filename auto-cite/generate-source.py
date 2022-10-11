import pandas as pd

ref = pd.read_excel('auto-cite/references.xlsx')
ref.dropna(subset=['DOI'], inplace=True)

with open('_data/sources.yaml', 'w+') as file:
    for idx, row in ref.iterrows():
        print(f'- id: {row["DOI"]}')
        file.write(f'- id: {row["DOI"].strip()} \n')
        tags = row["Keywords"].split(",")
        if len(tags):
            file.write('  tags:\n')
        for tag in tags:
            file.write(f'    - {tag.strip()}\n')
        
        
    