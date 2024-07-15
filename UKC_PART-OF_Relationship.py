"""
PART-OF UKC 
This script generates an PART-OF hierarchical tree visualization of a UKC example.
"""

# Importing the random module
import random

# Importing the Graphviz library
import graphviz


def generate_random_digit_string():
    """Generates a random 5-digit string.

    Returns:
      A string containing the 5 random digits.
    """
    random_digits = []
    for _ in range(5):
        random_digit = random.randint(0, 9)
        random_digits.append(str(random_digit))
    random_digit_string = "".join(random_digits)
    return random_digit_string


def create_node(graph, node, parent=None, relationship="PART-OF", language=None):
    """
    Creates a node in the graph and links it to the parent node if specified.

    Args:
        graph (graphviz.Digraph): The Graphviz Digraph object.
        node (dict): The current node represented as a dictionary with 'name' and 'id' keys.
        parent (str, optional): The ID of the parent node. Default is None.
        is_translated (bool, optional): Whether the node name is translated. Default is False.
        language (str, optional): The language for translation. Default is None.
    """

    prefix = ""
    node_label = ""

    if language == "italian":
        prefix = "it"
        node_name = translate_to_italian(node["name"])
        node_id = f"it{node['id']}"
        node_id_label = generate_random_digit_string()
        node_label = f"{node_name}\n{prefix}{node_id_label}"
    elif language == "ukc":
        node_name = generate_random_digit_string()
        node_id = f"ukc_{node['id']}"
        node_label = f"{node_name}"
    else:
        prefix = "en"
        node_id = f"{node['id']}"
        node_name = node["name"]
        node_label = f"{node_name}\n{prefix}{node_id}"

    graph.node(node_id, node_label, shape="box", style="rounded")

    if parent:
        if relationship == "PART-OF":
            graph.edge(parent, node_id, label="PART-OF", style="dashed", dir="back")

    if "children" in node:
        for child in node["children"]:
            create_node(graph, child, node_id, relationship, language)


def create_tree_visualization(trees):
    """
    Creates a tree visualization from the given trees.

    Args:
        trees (list): A list of trees, each represented as a list of dictionaries.

    Returns:
        graphviz.Digraph: The resulting Graphviz Digraph object.
    """
    dot = graphviz.Digraph(comment="UKC Tree PART-OF")
    dot.attr(rankdir="BT")  # Bottom to Top direction

    with dot.subgraph(name="cluster_0") as c:
        c.attr(label="English")
        root_id = "01740"
        c.node(root_id, "entity\nen47321", shape="box", style="rounded")

        for tree in trees:
            create_node(c, tree[0], root_id, relationship="PART-OF")

    with dot.subgraph(name="cluster_1") as c:
        c.attr(label="UKC")
        root_id = "ukc_01740"
        c.node(root_id, generate_random_digit_string(), shape="box", style="rounded")

        for tree in trees:
            create_node(c, tree[0], root_id, relationship="PART-OF", language="ukc")

    with dot.subgraph(name="cluster_2") as c:
        c.attr(label="Italiano")
        root_id = "it01740"
        c.node(root_id, "entità\nit70650", shape="box", style="rounded")

        for tree in trees:
            create_node(c, tree[0], root_id, relationship="PART-OF", language="italian")

    dot.edge(
        "01740", "ukc_01740", label="", style="dotted", color="#70727B", dir="back"
    )
    dot.edge(
        "it01740", "ukc_01740", label="", style="dotted", color="#70727B", dir="back"
    )

    dot.edge(
        "00100", "ukc_00100", label="", style="dotted", color="#70727B", dir="back"
    )
    dot.edge(
        "it00100", "ukc_00100", label="", style="dotted", color="#70727B", dir="back"
    )

    dot.edge(
        "20001", "ukc_20001", label="", style="dotted", color="#70727B", dir="back"
    )
    dot.edge(
        "it20001", "ukc_20001", label="", style="dotted", color="#70727B", dir="back"
    )

    dot.edge(
        "00500", "ukc_00500", label="", style="dotted", color="#70727B", dir="back"
    )
    dot.edge(
        "it00500", "ukc_00500", label="", style="dotted", color="#70727B", dir="back"
    )

    dot.edge(
        "00600", "ukc_00600", label="", style="dotted", color="#70727B", dir="back"
    )
    dot.edge(
        "it00600", "ukc_00600", label="", style="dotted", color="#70727B", dir="back"
    )

    dot.edge(
        "00200", "ukc_00200", label="", style="dotted", color="#70727B", dir="back"
    )
    dot.edge(
        "it00200", "ukc_00200", label="", style="dotted", color="#70727B", dir="back"
    )

    return dot


# Definition of the PART-OF trees
part_of_tree_education = [
    {
        "id": "00100",
        "name": "education",
    }
]

part_of_tree_urban = [
    {
        "id": "00200",
        "name": "urban",
    }
]

part_of_tree_location = [
    {
        "id": "20001",
        "name": "locations",
    }
]

part_of_tree_events = [
    {
        "id": "00500",
        "name": "events",
    }
]

part_of_tree_people = [
    {
        "id": "00600",
        "name": "people",
    },
]

# Define only PART-OF trees to visualize
part_of_trees = [
    part_of_tree_education,
    part_of_tree_people,
    part_of_tree_events,
    part_of_tree_location,
    part_of_tree_urban,
]

# Create the visualization for PART-OF trees only
part_of_tree_viz = create_tree_visualization(part_of_trees)

# Save the visualization as a PDF file
part_of_tree_viz.render("UKC_PARTOF", format="pdf", cleanup=True)
print("PART-OF tree visualization saved as 'UKC_PARTOF.pdf'")
