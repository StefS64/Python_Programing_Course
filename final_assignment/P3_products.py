# Big python project.
# Author: Stefan Świerczewski
# Indeks: ss459678
import pandas as pd
import P1_create_data as create
def extract_drug_products(file_path, drug_id):
    df_products = create.read_and_get_columns(
        file_path,
        ['drugbank-id', 'products']
    )
    row = df_products[df_products['drugbank-id'].apply(lambda x: drug_id in x)].iloc[0]

    products = row['products']
    drug_ids = row['drugbank-id']
    product_data = []
    for product in products[0]['product']:
        product_info = {
            'drugbank-id': drug_ids,
            'product-name': product.get('name', [''])[0],
            'manufacturer': product.get('labeller', [''])[0],
            'ndc': product.get('ndc-product-code', [''])[0],
            'form': product.get('dosage-form', [''])[0],
            'route': product.get('route', [''])[0],
            'dosage': product.get('strength', [''])[0],
            'country': product.get('country', [''])[0],
            'agency': product.get('source', [''])[0]
        }
        product_data.append(product_info)
    return pd.DataFrame(product_data)

if __name__ == "__main__":
    file_path = './drugbank_partial.xml'
    drug_id = 'DB00006'
    product_df = extract_drug_products(file_path, drug_id)
    print(product_df)
    product_df.to_csv('./temp/product.csv', index=False)
