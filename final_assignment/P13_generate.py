# Big python project.
# Author: Stefan Świerczewski
# Indeks: ss459678
import xml.etree.ElementTree as ET
import random
import copy

def read_existing_data(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()
    namespace = {'db': 'http://www.drugbank.ca'}
    drugs = root.findall('db:drug', namespace)
    return drugs[:100]

def generate_drugbank_id(index):
    return f"DB{index:05d}"

def get_drugbank_id_element(drug):
    namespace = {'db': 'http://www.drugbank.ca'}
    return drug.find('db:drugbank-id', namespace)
# Generates 2000 200000 takes to long
def generate_additional_drugs(existing_drugs, total_drugs=2000):
    existing_ids = {get_drugbank_id_element(drug).text for drug in existing_drugs}
    additional_drugs = []
    id_counter = 100
    for _ in range(100, total_drugs):
        original_drug = random.choice(existing_drugs)
        new_drug = copy.deepcopy(original_drug)
        new_id = generate_drugbank_id(id_counter)
        while new_id in existing_ids:
            id_counter += 1
            new_id = generate_drugbank_id(id_counter)
        
        drugbank_id_element = get_drugbank_id_element(new_drug)
        if drugbank_id_element is not None:
            drugbank_id_element.text = new_id
        
        existing_ids.add(new_id)
        additional_drugs.append(new_drug)
        id_counter += 1
    return additional_drugs

def save_to_xml(existing_drugs, additional_drugs, output_file_path):
    root = ET.Element('drugbank')
    for drug in existing_drugs + additional_drugs:
        root.append(drug)
    tree = ET.ElementTree(root)
    tree.write(output_file_path)

if __name__ == "__main__":
    existing_file_path = './drugbank_partial.xml'
    output_file_path = './drugbank_partial_and_generated.xml'
    
    existing_drugs = read_existing_data(existing_file_path)
    additional_drugs = generate_additional_drugs(existing_drugs)
    save_to_xml(existing_drugs, additional_drugs, output_file_path)
    
    # Perform analysis on the generated data
    import P1_create_data as create
    import P2_id_plot_synonym as id_plot_synonym
    import P3_products as products
    import P4_pathways as pathways
    import P5_bipartite_pathway_graph as bipartite
    import P6_number_of_paths as number_of_paths
    import P7_protein_interactions as proteins
    import P8_circle_diagram as circle_diagram
    import P9_drug_fazes as drug_fazes
    import P10_drug_interactions as drug_interactions
    import P11_gene_presentation as gene_presentation
    import P12_drug_representation as protein_gene_organisms

    file_path = './drugbank_partial_and_generated.xml'
    
    # P1
    df = create.P1(file_path)
    print(df)
    df.to_csv('./temp/created_p1_generated.csv')

    # P2
    drugbank_id = 'DB00001'  # Example DrugBank ID
    id_plot_synonym.plot_synonyms(file_path, drugbank_id)

    # P3
    product_df = products.extract_drug_products(file_path, drugbank_id)
    print(product_df)
    product_df.to_csv('./temp/drug_products_generated.csv', index=False)

    # P4
    pathway_df = pathways.get_pathway_data_frame(file_path)
    print(pathway_df)
    pathway_df.to_csv('./temp/pathways_generated.csv', index=False)

    # P5
    bipartite.plot_graph_bipartite_pathway(file_path)

    # P6
    number_of_paths.plot_number_of_interacting_pathways(file_path)

    # P7
    protein_df = proteins.create_prot_df(file_path)
    print(protein_df)
    protein_df.to_csv('./temp/protein_interactions_generated.csv', index=False)

    # P8
    circle_diagram.P8(file_path)

    # P9
    drug_fazes.P9(file_path)

    # P10
    interactions_df = drug_interactions.P10(file_path)
    print(interactions_df)
    interactions_df.to_csv('./temp/drug_interactions_generated.csv', index=False)

    # P11
    gene_name = 'PLG' # Example gene
    gene_presentation.create_gene_presentation(file_path, gene_name)

    # P12
    gene_df = protein_gene_organisms.task_12(file_path)
    gene_df.to_csv('./temp/gene_info.csv', index=False)


