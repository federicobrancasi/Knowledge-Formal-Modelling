"""
PART-OF WORDNET
This script generates a PART-OF hierarchical tree visualization of a WordNet example.
"""

# Importing the Graphviz library
import graphviz


def create_node(graph, node, parent=None):
    """
    Creates a node in the graph and links it to the parent node if specified.

    Args:
        graph (graphviz.Digraph): The Graphviz Digraph object.
        node (dict): The current node represented as a dictionary with 'name' and 'id' keys.
        parent (str, optional): The ID of the parent node. Default is None.
    """
    node_id = f"{node['name']}_{node['id']}"
    # Adding the node to the graph with a specific shape and style
    graph.node(node_id, f"{node['name']}\n{node['id']}", shape="rect", style="rounded")
    if parent:
        # Creating a dashed edge with a "PART-OF" relationship label
        graph.edge(parent, node_id, label="PART-OF", style="dashed", dir="back")
    # Recursively creating child nodes if present
    for child in node.get("children", []):
        create_node(graph, child, node_id)


def create_part_of_tree_visualization(part_of_trees):
    """
    Creates a PART-OF tree visualization from the given trees.

    Args:
        part_of_trees (list): A list of PART-OF trees, each represented as a list of dictionaries.

    Returns:
        graphviz.Digraph: The resulting Graphviz Digraph object.
    """
    dot = graphviz.Digraph(comment="WordNet PART-OF Hierarchical Tree")
    dot.attr(rankdir="BT")  # Bottom to Top direction

    # Creating the root node for PART-OF trees
    part_of_root_id = "entitypartof_01740"
    dot.node(part_of_root_id, "entity\n01740", shape="rect", style="rounded")

    # Creating nodes for each tree and linking to the root
    for tree in part_of_trees:
        for subtree in tree:
            create_node(dot, subtree, part_of_root_id)

    return dot


# Definition of PART-OF trees
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
    }
]

# Combine all PART-OF trees
part_of_trees = [
    part_of_tree_education,
    part_of_tree_people,
    part_of_tree_events,
    part_of_tree_location,
    part_of_tree_urban,
]

# Create the visualization for PART-OF trees only
part_of_tree_viz = create_part_of_tree_visualization(part_of_trees)

# Save the visualization as a PDF file
part_of_tree_viz.render("wordnet_PARTOF", format="pdf", cleanup=True)
print("PART-OF tree visualization saved as 'wordnet_PARTOF.pdf'")
