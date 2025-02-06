# Big python project.
# Author: Stefan Świerczewski
# Indeks: ss459678
import pandas as pd;
import P1_create_data as create

def get_pathway_data_frame(file_path):
    kolumns = ['pathways']
    pathway_df = create.read_and_get_columns(file_path, kolumns)
    path_data = []
    for _, row in pathway_df.iterrows():
        pathways = row['pathways']
        for path in pathways:
            if path and path not in path_data:
                path_data.append(path['pathway'][0])
    return pd.DataFrame(path_data)


if __name__ == "__main__":
    file_path = './drugbank_partial.xml'
    df_pathways = get_pathway_data_frame(file_path)
    print(df_pathways)