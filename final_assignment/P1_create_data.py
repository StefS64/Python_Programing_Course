# Big python project.
# Author: Stefan Świerczewski
# Indeks: ss459678
import pandas as pd
import xml.etree.ElementTree as ET

PY_TEST_FLAG = None
def set_flag(value):
    global PY_TEST_FLAG
    PY_TEST_FLAG = value
#___________Input functions_____________
def strip_namespace(tag):
    return tag.split('}', 1)[1] if '}' in tag else tag
# Recurrently parse nested elements  
def parse_element(element, namespace, with_attributes):
    data = {}
    for child in element:
        tag = strip_namespace(child.tag)
        if tag in with_attributes:
            attributes = dict(child.attrib)
        else:
            attributes = None
        if len(child):
            if tag not in data:
                data[tag] = []
            child_data = parse_element(child, namespace, with_attributes)
            if attributes:
                child_data['attributes'] = attributes
            data[tag].append(child_data)
        else:
            if tag not in data:
                data[tag] = []
            if attributes:
                data[tag].append({'value': child.text, 'attributes': attributes})
            else:
                data[tag].append(child.text)
    return data


def read_and_get_columns(file_path, selected_columns=None, with_attributes=[]):
    tree = ET.parse(file_path)
    root = tree.getroot()
    namespace = {'db': 'http://www.drugbank.ca'}

    data = []
    for drug in root.findall('db:drug', namespace):
        drug_data = {}

        for attr in drug.attrib:
            drug_data[attr] = drug.attrib[attr]

        drug_data.update(parse_element(drug, namespace, with_attributes))
        data.append(drug_data)
        if PY_TEST_FLAG and PY_TEST_FLAG < len(data):
            break


    raw_df = pd.DataFrame(data)
    if selected_columns:
        return raw_df[selected_columns]
    return raw_df

def P1(file_path):
    df_1 = read_and_get_columns(
        file_path, 
        ['drugbank-id', 'name', 'type', 'description', 'state', 'indication', 
        'mechanism-of-action', 'food-interactions', 'targets'])
    return df_1

if __name__ == "__main__":
    print("_________PROBLEM 1 BEGIN__________")
    file_path = './drugbank_partial.xml'
    df_1 = P1(file_path)
    print(df_1)
    df_1.to_csv('./temp/df_1.csv', index=False)
    print("_________PROBLEM 1 END____________\n\n")