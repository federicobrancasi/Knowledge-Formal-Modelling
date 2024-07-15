"""
KNOWLEDGE TELEOLOGY
This script generates a graph visualization of a Knowledge Teleology example.
"""

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
    nodeName = f"{node['name']}"
    nodeId = f"{node['id']}"

    # Define labels for each type of node
    if nodeName == "entity":
        label = f"{{ {nodeName} | {nodeId} }}"
    elif nodeName == "person":
        label = f"{{ {nodeName} | {nodeId} | name : string | age : int }}"
    elif nodeName == "professor":
        label = f"{{ {nodeName} | {nodeId} | name : string | age : int | supervises : research project | holds : lecture | belongs to : department }}"
    elif nodeName == "student":
        label = f"{{ {nodeName} | {nodeId} | name : string | age : int | attends : lecture | enrolls in : course }}"
    elif nodeName == "administrative staff":
        label = f"{{ {nodeName} | {nodeId} | name : string | age : int | manages : department }}"
    elif nodeName == "education event":
        label = f"{{ {nodeName} | {nodeId} }}"
    elif nodeName == "research project":
        label = f"{{ {nodeName} | {nodeId} | title : string | duration : int | funded by : university }}"
    elif nodeName == "course":
        label = f"{{ {nodeName} | {nodeId} | title : string | credits : int | offered by : department }}"
    elif nodeName == "lecture":
        label = f"{{ {nodeName} | {nodeId} | title : string | duration : int | part of : course | held in : classroom }}"
    elif nodeName == "location":
        label = f"{{ {nodeName} | {nodeId} }}"
    elif nodeName == "classroom":
        label = f"{{ {nodeName} | {nodeId} | number : string | capacity : int }}"
    elif nodeName == "department":
        label = f"{{ {nodeName} | {nodeId} | name : string | head : professor | part of : university }}"
    elif nodeName == "university":
        label = f"{{ {nodeName} | {nodeId} | name : string | location : string }}"
    else:
        label = f"{{ {nodeName} | {nodeId} }}"

    # Adding the node to the graph with the specified label
    graph.node(node_id, label, shape="record", style="rounded")
    if parent:
        # Creating an edge between the current node and the parent node
        graph.edge(node_id, parent, label="IS-A")
    # Recursively creating child nodes
    for child in node.get("children", []):
        create_node(graph, child, node_id)


def create_tree_visualization(trees):
    """
    Creates a tree visualization from the given trees and relationships.

    Args:
        trees (list): A list of trees, each represented as a list of dictionaries.

    Returns:
        graphviz.Digraph: The resulting Graphviz Digraph object.
    """
    dot = graphviz.Digraph(comment="Teleontology Tree")
    dot.attr(rankdir="BT")  # Bottom to Top direction

    # Creating the root node "entity"
    root_id = "entity_01740"
    label = f"{{ object | 01740 }}"
    dot.node(root_id, label, shape="record", style="rounded")

    with dot.subgraph(name="cluster_university") as c:
        c.attr(color="gray", label="University", penwidth="5")

        # Creating nodes for each tree and linking to the root
        for tree in trees:
            create_node(c, tree[0], root_id)

    return dot


# Definition of IS-A trees
tree_person = [
    {
        "id": "10502",
        "name": "person",
        "children": [
            {"id": "25323", "name": "professor"},
            {"id": "45356", "name": "student"},
            {"id": "65890", "name": "administrative staff"},
        ],
    }
]

tree_education_event = [
    {
        "id": "20111",
        "name": "education event",
        "children": [
            {"id": "30111", "name": "research project"},
            {"id": "30112", "name": "course"},
            {"id": "30113", "name": "lecture"},
        ],
    }
]

tree_location = [
    {
        "id": "40111",
        "name": "location",
        "children": [
            {"id": "50111", "name": "classroom"},
            {"id": "50112", "name": "department"},
            {"id": "50113", "name": "university"},
        ],
    }
]

# Combine all trees
all_trees = [tree_person, tree_education_event, tree_location]

# Create the visualization
tree_viz = create_tree_visualization(all_trees)

# Save the visualization as a PDF file
tree_viz.render("Knowledge_Teleology", format="pdf", cleanup=True)
print("Tree visualization saved as 'Knowledge_Teleology.pdf'")
