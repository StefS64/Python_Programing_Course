# Big python project.
# Author: Stefan Świerczewski
# Indeks: ss459678
import networkx as nx
import matplotlib.pyplot as plt
import P1_create_data as create

# _________problem 2 functions___________
def plot_synonym_graph(drugbank_id, synonym_df):

    # Get row containing the id.
    row = synonym_df[synonym_df['drugbank-id'].apply(lambda x: drugbank_id in x)]
    
    if not row.empty:
        synonyms = row['synonyms'].values[0][0]['synonym']
        name = row['name'].values[0][0]

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
def plot_synonyms(file_path, drug_id):
    df_1 = create.read_and_get_columns(
        file_path,
        ['drugbank-id', 'synonyms', 'name']
    )
    print(df_1)
    plot_synonym_graph(drug_id, df_1)
 
if __name__ == "__main__":
    print("_________PROBLEM 2 BEGIN__________")
    file_path = './drugbank_partial.xml'
    plot_synonyms(file_path, 'DB00006')
    
    print("_________PROBLEM 2 END____________\n\n")