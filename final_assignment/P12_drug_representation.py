
import pandas as pd
import requests
import P7_protein_interactions as proteins

def fetch_uniprot_data(gene_name):
    url = f"https://rest.uniprot.org/uniprotkb/search?query=gene:{gene_name}&format=tsv&fields=gene_names,organism_name,length"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.text
        return data
    else:
        print(f"Failed to fetch data for gene: {gene_name}")
        return None

def task_12(file_path): 
    protein = proteins.create_prot_df(file_path)
    genes = protein[['Drugbank ID', 'Gene Name']]

    gene_info = {}

    for gene_name in genes['Gene Name']:
        uniprot_data = fetch_uniprot_data(gene_name)
        if uniprot_data:
            for line in uniprot_data.strip().split('\n')[1:]:  # Skip header line
                fields = line.split('\t')
                if gene_name not in gene_info:
                    gene_info[gene_name] = {'organism': [], 'length': []}
                gene_info[gene_name]['organism'].append(fields[1])

    genes['organisms'] = genes['Gene Name'].map(lambda x: ', '.join(gene_info[x]['organism']) if x in gene_info else None)
    return genes

if __name__ == "__main__":
    file_path = './drugbank_partial.xml'
    print(task_12(file_path))    