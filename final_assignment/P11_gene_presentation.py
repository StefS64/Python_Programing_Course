# Big python project.
# Author: Stefan Świerczewski
# Indeks: ss459678
import P7_protein_interactions as proteins
import P3_products as products
import P1_create_data as create
import matplotlib.pyplot as plt
import networkx as nx
import pandas as pd

def create_network_graph(gene_name, product_edges, drug_names):
    G = nx.Graph()
    
    
    G.add_node(gene_name, label=gene_name, level=0)
    
   
    for drug_id in drug_names['drugbank-id']:
        drug_name = drug_names[drug_names['drugbank-id'] == drug_id]['name'].values[0]
        G.add_node(drug_id, label=drug_name[0], level=1)
        G.add_edge(gene_name, drug_id)
    
   
    for _, row in product_edges.iterrows():
        product_name = row['Product Name']
        drug_id = row['DrugBank ID']
        G.add_node(product_name, label=product_name, level=2)
        G.add_edge(drug_id, product_name)
    
    
    pos = {}
    levels = {0: [], 1: [], 2: []}
    for node, data in G.nodes(data=True):
        levels[data['level']].append(node)
    
    for level, nodes in levels.items():
        y_spacing = 1 / (len(nodes) + 1)
        for i, node in enumerate(nodes):
            if level == 2 and i % 2 == 0:
                pos[node] = (level + 0.1, y_spacing * (i + 1))
            elif level == 2 and i % 2 != 0:
                pos[node] = (level - 0.1, y_spacing * (i + 1))
            else:
                pos[node] = (level, y_spacing * (i + 1))
    
    labels = nx.get_node_attributes(G, 'label')
    
    
    color_map = []
    for node in G:
        if G.nodes[node]['level'] == 0:
            color_map.append('red')
        elif G.nodes[node]['level'] == 1:
            color_map.append('lightgreen')
        else:
            color_map.append('lightblue')
    
    plt.figure(figsize=(12, 8))
    nx.draw(G, pos, with_labels=True, labels=labels, node_size=3000, node_color=color_map, font_size=10, font_weight='bold')
    plt.title('Gene-Drug-Product Interactions Network')
    plt.show()

def create_gene_presentation(file_path, gene_name):
    drugs_with_data = proteins.create_prot_df(file_path)
    
    filtered_drugs = drugs_with_data[drugs_with_data['Gene Name'] == gene_name]
    drug_ids = filtered_drugs['Drugbank ID'].apply(lambda x: x[0] if isinstance(x, list) else x).unique()

    product_edges = pd.DataFrame(columns=['DrugBank ID', 'Product Name'])
    for drug in drug_ids:
        df = products.extract_drug_products(file_path, drug)
        for _,row in df.iterrows():
            new_row = pd.DataFrame({'DrugBank ID': [drug], 'Product Name': [row['product-name']]})
            product_edges = pd.concat([product_edges,new_row], ignore_index=True)

    product_edges = product_edges.drop_duplicates()


    drug_names = create.read_and_get_columns(file_path, ['drugbank-id', 'name'])
    drug_names['drugbank-id'] = drug_names['drugbank-id'].apply(lambda x: x[0] if isinstance(x, list) else x)
    drug_names = drug_names[drug_names['drugbank-id'].isin(drug_ids)]
 
    create_network_graph(gene_name, product_edges, drug_names)
if __name__ == "__main__":
    file_path = './drugbank_partial.xml'
    gene_name = 'PLG'
    create_gene_presentation(file_path, gene_name)
    
    