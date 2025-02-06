import os
import pandas as pd
import P1_create_data as create
import P3_products as products
import P4_pathways as pathways
import P6_number_of_paths as number_of_paths
import P7_protein_interactions as proteins
import P10_drug_interactions as drug_interactions
import P12_drug_representation as protein_gene_organisms

file_path = './drugbank_partial.xml'

def compare_csv_files(file1, file2):
    with open(file1, 'r') as f1, open(file2, 'r') as f2:
        content1 = f1.read()
        content2 = f2.read()
        assert content1 == content2, f"Files {file1} and {file2} do not match."

def test_P1_output():
    create.set_flag(5)
    df_generated = create.P1(file_path)
    generated_file = './test_files/P1_generated.csv'
    df_generated.to_csv(generated_file, index=False)
    compare_csv_files(generated_file, './test_files/P1_proper.csv')
    os.remove(generated_file)

def test_P2_output():
    df_generated = create.read_and_get_columns(file_path, ['drugbank-id', 'synonyms', 'name'])
    generated_file = './test_files/P2_generated.csv'
    df_generated.to_csv(generated_file, index=False)
    compare_csv_files(generated_file, './test_files/P2_proper.csv')
    os.remove(generated_file)

def test_P3_output():
    drug_id = 'DB00006'
    df_generated = products.extract_drug_products(file_path, drug_id)
    generated_file = './test_files/P3_generated.csv'
    df_generated.to_csv(generated_file, index=False)
    compare_csv_files(generated_file, './test_files/P3_proper.csv')
    os.remove(generated_file)

def test_P4_output():
    df_generated = pathways.get_pathway_data_frame(file_path)
    generated_file = './test_files/P4_generated.csv'
    df_generated.to_csv(generated_file, index=False)
    compare_csv_files(generated_file, './test_files/P4_proper.csv')
    os.remove(generated_file)

def test_P6_output():
    df_generated = number_of_paths.create_number_of_interacting_paths(file_path)
    generated_file = './test_files/P6_generated.csv'
    df_generated.to_csv(generated_file, index=False)
    compare_csv_files(generated_file, './test_files/P6_proper.csv')
    os.remove(generated_file)

def test_P7_output():
    df_generated = proteins.create_prot_df(file_path)
    generated_file = './test_files/P7_generated.csv'
    df_generated.to_csv(generated_file, index=False)
    compare_csv_files(generated_file, './test_files/P7_proper.csv')
    os.remove(generated_file)

def test_P10_output():
    df_generated = drug_interactions.P10(file_path)
    generated_file = './test_files/P10_generated.csv'
    df_generated.to_csv(generated_file, index=False)
    compare_csv_files(generated_file, './test_files/P10_proper.csv')
    os.remove(generated_file)

def test_P12_output():
    df_generated = protein_gene_organisms.task_12(file_path)
    generated_file = './test_files/P12_generated.csv'
    df_generated.to_csv(generated_file, index=False)
    compare_csv_files(generated_file, './test_files/P12_proper.csv')
    os.remove(generated_file)

if __name__ == "__main__":
    import pytest
    pytest.main()