# Big python project.
# Author: Stefan Świerczewski
# Indeks: ss459678
import matplotlib.pyplot as plt
import P1_create_data as create
import P4_pathways as paths
import P5_bipartite_pathway_graph as bipartite

def create_number_of_interacting_paths(file_path):
    drug_df = create.read_and_get_columns(file_path, ['drugbank-id','name'])
    # Get the graph from last problem tha number of pathways is naturally calculated.
    pathway_graph = bipartite.get_bipartite_pathway_graph(paths.get_pathway_data_frame(file_path))

    drug_nodes = [n for n, d in pathway_graph.nodes(data=True) if d["bipartite"] == 1]

    drug_df['pathway_count'] = drug_df['drugbank-id'].apply(
        lambda x:  pathway_graph.degree(x[0]) if x[0] in drug_nodes else 0
    )
    return drug_df
def plot_number_of_interacting_pathways(file_path):
    drug_df = create_number_of_interacting_paths(file_path)
    drug_df.set_index('name', inplace=True)
    # drug_pathway_counts
    plt.figure()
    drug_df['pathway_count'].plot(kind='bar')
    plt.xlabel('Drug Name')
    plt.ylabel('Number of Pathways')
    plt.title('Number of Pathways Each Drug Interacts With')
    plt.show()

if __name__ == "__main__":
    file_path = './drugbank_partial.xml'
    plot_number_of_interacting_pathways(file_path)