# Big python project.
# Author: Stefan Świerczewski
# Indeks: ss459678
import P1_create_data as create
import pandas as pd

def extract_drug_interactions(df):
    interactions_data = []
    for _, row in df.iterrows():
        drug_id = row['drugbank-id']
        drug_name = row['name']
        raw_interactions = row.get('drug-interactions', [])[0]
        if raw_interactions is None:
            continue
        interactions = raw_interactions['drug-interaction']
        if interactions is None:
            interaction_data = {
                'DrugBank ID': drug_id,
                'Drug Name': drug_name,
                'Interaction DrugBank ID': None,
                'Interaction Name': None,
                'Description': None
            }
            interactions_data.append(interaction_data)
            continue

        # print("_____________________Interaction_______________________")
        # print(interactions)
        for interaction in interactions:
            # print("___________________________________________")
            # print(interaction)
            interaction_data = {
                'DrugBank ID': drug_id,
                'Drug Name': drug_name,
                'Interaction DrugBank ID': interaction.get('drugbank-id', ''),
                'Interaction Name': interaction.get('name', ''),
                'Description': interaction.get('description', '')
            }
            interactions_data.append(interaction_data)
    return pd.DataFrame(interactions_data)

def P10(file_path):
    df = create.read_and_get_columns(file_path, ['drugbank-id', 'name', 'drug-interactions'])
    return extract_drug_interactions(df)

if __name__ == "__main__":
    file_path = './drugbank_partial.xml'
    interactions_df = P10(file_path) 
    print(interactions_df)
    interactions_df.to_csv('./temp/drug_interactions.csv', index=False)