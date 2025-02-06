# Big python project.
# Author: Stefan Świerczewski
# Indeks: ss459678
import P1_create_data as create
import pandas as pd

def extract_protein_interactions(df):
    protein_data = []
    for _, row in df.iterrows():
        drug_id = row['drugbank-id']
        targets = row['targets']
        for target in targets:
            if target is None:
                continue
            rel_target = target['target'][0]
            target_id = rel_target.get('id', [''])[0]
            polypeptides = rel_target.get('polypeptide', [])
            for polypeptide in polypeptides:
                external_identifiers = polypeptide.get('external-identifiers', [{}])[0].get('external-identifier', [])
                polypeptide_attr = polypeptide.get('attributes', {})
                genatlas_id = next(
                    (item['identifier'][0] for item in external_identifiers if 'GenAtlas' in item['resource']),
                    ''
                )
                data = {
                    'Drugbank ID': drug_id,
                    'Local ID': target_id,
                    'Source':  polypeptide_attr.get('source', ''),
                    'External ID': polypeptide_attr.get('id', ''), 
                    'Polypeptide Name': polypeptide.get('name', [''])[0],
                    'Gene Name': polypeptide.get('gene-name', [''])[0],
                    'GenAtlas ID': genatlas_id,
                    'Chromosome Location': polypeptide.get('chromosome-location', [''])[0],
                    'Cellular Location': polypeptide.get('cellular-location', [''])[0]
                }
                protein_data.append(data)
    return pd.DataFrame(protein_data)

def create_prot_df(file_path):
    df = create.read_and_get_columns( 
        file_path,
        ['drugbank-id', 'targets', 'name'],
        ['polypeptide']
    )
    return extract_protein_interactions(df)

if __name__ == "__main__":
    file_path = './drugbank_partial.xml'
    protein_df = create_prot_df(file_path)
    protein_df.to_csv('./temp/protein_df.csv', index=False)
    print(protein_df)