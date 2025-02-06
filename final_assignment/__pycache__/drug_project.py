# Big python project.
# Author: Stefan Świerczewski
# Indeks: ss459678
import pandas as pd
import xml.etree.ElementTree as ET
import networkx as nx
import matplotlib.pyplot as plt
#___________Input functions_____________
def strip_namespace(tag):
    return tag.split('}', 1)[1] if '}' in tag else tag

def parse_element(element, namespace):
    data = {}
    for child in element:
        tag = strip_namespace(child.tag)
        if len(child):
            if tag not in data:
                data[tag] = []
            data[tag].append(parse_element(child, namespace))
        else:
            if tag not in data:
                data[tag] = []
            data[tag].append(child.text)
    return data


def read_and_get_columns(file_path, selected_columns=None):
    tree = ET.parse(file_path)
    root = tree.getroot()
    namespace = {'db': 'http://www.drugbank.ca'}

    data = []
    print("start")
    for drug in root.findall('db:drug', namespace):
        drug_data = {}

        for attr in drug.attrib:
            drug_data[attr] = drug.attrib[attr]

        drug_data.update(parse_element(drug, namespace))
        data.append(drug_data)

    raw_df = pd.DataFrame(data)
    if selected_columns:
        return raw_df[selected_columns]
    return raw_df
#_________Input functions end_____________ 
# helper prints to get to know the dataset
file_path = './drugbank_partial.xml'
df = read_and_get_columns(file_path)
print(df)
print(df.columns)



# _________problem 2 functions___________
def plot_synonym_graph(drugbank_id, synonym_df):

    # Get row containing the id.
    row = synonym_df[synonym_df['drugbank-id'].apply(lambda x: drugbank_id in x)]
    
    if not row.empty:
        synonyms = row['synonyms'].values[0][0]['synonym']
        name = row['name'].values[0][0]

        # Create the graph
        G = nx.Graph()
        G.add_node(name, label=name)
        for synonym in synonyms:
            if synonym != name:
                G.add_node(synonym, label=synonym)
                G.add_edge(synonym, name)

        fig = plt.figure()
        fig.canvas.manager.set_window_title(f"Synonyms of {name}")
    
        pos = nx.spring_layout(G)
        labels = nx.get_node_attributes(G, 'label')
        nx.draw(G, pos, with_labels=True, labels=labels, node_size=10000, node_color='skyblue', font_size=10, font_weight='bold')
        
        
        plt.show()

    else:
        print(f"DrugBank ID {drugbank_id} not found")
#_______functions problem 2 end____________

file_path = './drugbank_partial.xml'

print("_________PROBLEM 1 BEGIN__________")
df_1 = read_and_get_columns(
    file_path, 
    ['name', 'type', 'description', 'state', 'indication', 
    'mechanism-of-action', 'food-interactions']
)
print(df_1)
print("_________PROBLEM 1 END____________\n\n")

print("_________PROBLEM 2 BEGIN__________")
df_2 = read_and_get_columns(
    file_path,
    ['drugbank-id', 'synonyms', 'name']
)
# Example print of function:
plot_synonym_graph('DB00006', df_2)
print("_________PROBLEM 2 END_____________\n\n")

# problem 3.

print("_________PROBLEM 3 BEGIN___________")
drug_id = 'DB00006'
df_products = read_and_get_columns(
    file_path,
    ['drugbank-id', 'products']
)
row = df_products[df_products['drugbank-id'].apply(lambda x: drug_id in x)]

products = row['products'].values[0]
drug_ids = row['drugbank-id']

product_data = []
for product in products:
    # print(product)
    # TODO to zmienić żeby było ładniejsze.
    product_info = {
                'drugbank-id': drug_ids,
                'product-name': product.get('name', ''),
                'manufacturer': product.get('manufacturer', ''),
                'ndc': product.get('ndc', ''),
                'form': product.get('form', ''),
                'route': product.get('route', ''),
                'dosage': product.get('dosage', ''),
                'country': product.get('country', ''),
                'agency': product.get('agency', '')
            }
    product_data.append(product_info)
product_df = pd.DataFrame(product_data)

print(product_df)
# print(drug_ids)
# print(products)

print("_________PROBLEM 3 END___________")

print("_________PROBLEM 4 BEGIN_________")
def get_pathway_data_frame(file_path):
    kolumns = ['pathways']
    pathway_df = read_and_get_columns(file_path, kolumns)
    path_data = []
    for _, row in pathway_df.iterrows():
        pathways = row['pathways']
        for path in pathways:
            if path and path not in path_data:
                path_data.append(path['pathway'][0])
    return pd.DataFrame(path_data)
df_pathways = get_pathway_data_frame(file_path)
print(df_pathways)
print("_________PROBLEM 4 END___________")


print("_________PROBLEM 5 BEGIN_________")

def get_bipartite_pathway_graph(pathways_graph_df):


    pathway_names = sum(pathways_graph_df['name'].tolist(), [])
    pathway_ids = sum(pathways_graph_df['smpdb-id'].tolist(), [])
    # print(pathway_names)
    B = nx.Graph()
    for i in range(len(pathway_names)):
        B.add_node(pathway_ids[i], bipartite=0, label=pathway_names[i])

    for _, row in pathways_graph_df.iterrows():
        name = row['name'][0]
        path_id = row['smpdb-id'][0]
        # print(row['drugs'])
        for drug in row['drugs'][0]['drug']:
            if drug:
                drug_name = drug['name'][0]
                drug_id = drug['drugbank-id'][0]
                B.add_node(drug_id, bipartite=1, label=drug_name)
                B.add_edge(path_id, drug_id)
    return B
def plot_graph_bipartite_pathway(file_path):
    pathways_graph_df = get_pathway_data_frame(file_path)
    graph = get_bipartite_pathway_graph(pathways_graph_df)

    top_nodes = [n for n, d in graph.nodes(data=True) if d["bipartite"] == 1]
    pos = nx.bipartite_layout(graph, top_nodes, aspect_ratio=30, scale=0.5, align='horizontal')
    fig = plt.figure()
    fig.canvas.manager.set_window_title("Bipartite graph drug-pathway")
    labels = nx.get_node_attributes(graph, 'label')
    nx.draw(graph, pos, with_labels=True, labels=labels, node_size=1000, node_color='skyblue', font_size=7)
    plt.show()

plot_graph_bipartite_pathway(file_path)
print("_________PROBLEM 5 END___________")

print("_________PROBLEM 6 BEGIN_________")
def create_number_of_interacting_paths(file_path):
    drug_df = read_and_get_columns(file_path, ['drugbank-id','name'])
    # Get the graph from last problem tha number of pathways is naturally calculated.
    pathway_graph = get_bipartite_pathway_graph(get_pathway_data_frame(file_path))

    drug_nodes = [n for n, d in pathway_graph.nodes(data=True) if d["bipartite"] == 1]
    # print(pathway_graph.degree())
    # print(drug_nodes)

    drug_df['pathway_count'] = drug_df['drugbank-id'].apply(
        lambda x:  pathway_graph.degree(x[0]) if x[0] in drug_nodes else 0
    )
    return drug_df
def plot_number_of_interacting_pathways(file_path):
    drug_df = create_number_of_interacting_paths(file_path)
    # print(drug_df)
    drug_df.set_index('name', inplace=True)
    # drug_pathway_counts
    plt.figure()
    drug_df['pathway_count'].plot(kind='bar')
    plt.xlabel('Drug Name')
    plt.ylabel('Number of Pathways')
    plt.title('Number of Pathways Each Drug Interacts With')
    plt.show()
plot_number_of_interacting_pathways(file_path)

print("_________PROBLEM 6 END___________")


print("_________PROBLEM 7 BEGIN_________")


print("_________PROBLEM 7 END___________")