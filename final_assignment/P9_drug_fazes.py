# Big python project.
# Author: Stefan Świerczewski
# Indeks: ss459678
import P1_create_data as create
import matplotlib.pyplot as plt
def create_circle_diagram(df):
    group_counts = {}
    for _, row in df.iterrows():
        groups_list = row['groups']
        if isinstance(groups_list, list) and len(groups_list) > 0:
            for g in groups_list[0].get('group', []):
                group_counts[g] = group_counts.get(g, 0) + 1

    fig, ax = plt.subplots(figsize=(6,6))

    labels = [f"{group} ({count})" for group, count in group_counts.items()]

    wedges, texts, autotexts = ax.pie(
        group_counts.values(),
        labels=None,
        autopct='%1.1f%%',
        startangle=140
    )
    ax.set_title('Drug Groups')
    ax.axis('equal')

    ax.legend(wedges, labels, title="Groups", loc="best")

    plt.show()
def P9(file_path):
    df = create.read_and_get_columns(file_path, ['groups'])
    create_circle_diagram(df)

if __name__ == "__main__":
    file_path = './drugbank_partial.xml'
    P9(file_path)