# Big python project.
# Author: Stefan Świerczewski
# Indeks: ss459678
import P1_create_data as create
import P7_protein_interactions as proteins
import matplotlib.pyplot as plt

def create_circle_diagram(df):
    counts = df['Cellular Location'].value_counts()
    fig, ax = plt.subplots(figsize=(6, 6))
    wedges, _, autotexts = ax.pie(
        counts.values,
        autopct='%1.1f%%',
        startangle=140
    )
    ax.set_title('Cellular Locations')
    ax.axis('equal')  # Keeps the pie chart circular
    ax.legend(wedges, counts.index, title="Locations", loc="best")
    plt.show()

def P8(file_path):
    df = proteins.create_prot_df(file_path)
    create_circle_diagram(df)

if __name__ == "__main__":
    file_path = "./drugbank_partial.xml"
    P8(file_path)