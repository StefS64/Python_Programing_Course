import networkx as nx
import matplotlib.pyplot as plt
import P4_pathways as paths


def get_bipartite_pathway_graph(pathways_graph_df):


    pathway_names = sum(pathways_graph_df['name'].tolist(), [])
    pathway_ids = sum(pathways_graph_df['smpdb-id'].tolist(), [])
    B = nx.Graph()
    for i in range(len(pathway_names)):
        B.add_node(pathway_ids[i], bipartite=0, label=pathway_names[i])

    for _, row in pathways_graph_df.iterrows():
        name = row['name'][0]
        path_id = row['smpdb-id'][0]
        for drug in row['drugs'][0]['drug']:
            if drug:
                drug_name = drug['name'][0]
                drug_id = drug['drugbank-id'][0]
                B.add_node(drug_id, bipartite=1, label=drug_name)
                B.add_edge(path_id, drug_id)
    return B
def plot_graph_bipartite_pathway(file_path):
    pathways_graph_df = paths.get_pathway_data_frame(file_path)
    graph = get_bipartite_pathway_graph(pathways_graph_df)

    top_nodes = [n for n, d in graph.nodes(data=True) if d["bipartite"] == 1]
    pos = nx.bipartite_layout(graph, top_nodes, aspect_ratio=30, scale=0.5, align='horizontal')
    fig = plt.figure()
    fig.canvas.manager.set_window_title("Bipartite graph drug-pathway")
    labels = nx.get_node_attributes(graph, 'label')
    
    nx.draw(graph, pos, with_labels=True, labels=labels, node_size=1000, node_color='skyblue', font_size=7)
    plt.show()
if __name__ == "__main__":
    file_path = './drugbank_partial.xml'
    plot_graph_bipartite_pathway(file_path)