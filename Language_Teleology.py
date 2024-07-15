"""
LANGUAGE TELEOLOGY
This script generates a graph visualization of a Language Teleology example.
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
    relationship = f"{node['relationship']}"

    # Define labels for each type of node
    if nodeName == "entity":
        label = f"{{ {nodeName} | 01740 }}"
    elif nodeName == "person":
        label = f"{{ {nodeName} | {nodeId} | name : string | age : int }}"
    elif nodeName == "professor":
        label = f"{{ {nodeName} | {nodeId} | name : string | age : int | supervises : research project | holds : lecture | belongs to : department }}"
    elif nodeName == "student":
        label = f"{{ {nodeName} | {nodeId} | name : string | age : int | attends : lecture | enrolls in : course }}"
    elif nodeName == "administrative staff":
        label = f"{{ {nodeName} | {nodeId} | name : string | age : int | manages : department }}"
    elif nodeName == "education event":
        label = f"{{ {nodeName} | {nodeId} | name : string}}"
    elif nodeName == "research project":
        label = f"{{ {nodeName} | {nodeId} | title : string | duration : int | funded by : university }}"
    elif nodeName == "course":
        label = f"{{ {nodeName} | {nodeId} | title : string | credits : int | offered by : department }}"
    elif nodeName == "lecture":
        label = f"{{ {nodeName} | {nodeId} | title : string | duration : int | part of : course | held in : classroom }}"
    elif nodeName == "location":
        label = f"{{ {nodeName} | {nodeId} | name : string}}"
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
        if relationship == "IS-A":
            graph.edge(node_id, parent, label=relationship, dir="back")
        else:
            graph.edge(node_id, parent, label=relationship)

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
    label = f"{{ university | 01740 | name : string | head : professor | part of : university }}"
    dot.node(root_id, label, shape="record", style="rounded")
    label = f"{{ entity | 01740 }}"
    dot.node("spacentity_01740", label, shape="record", style="rounded")
    dot.edge("entity_01740", "spacentity_01740", "PART-OF")

    # Creating nodes for each tree and linking to the root
    for tree in trees:
        create_node(dot, tree, root_id)

    return dot


# Definition of IS-A trees
tree_teleology = [
    {
        "id": "10502",
        "name": "professor",
        "relationship": "PART-OF",
        "children": [
            {
                "id": "25323",
                "name": "person",
                "relationship": "IS-A",
                "children": [
                    {"id": "01741", "name": "entity", "relationship": "IS-A"},
                ],
            },
        ],
    },
    {
        "id": "20111",
        "name": "lecture",
        "relationship": "PART-OF",
        "children": [
            {
                "id": "30113",
                "name": "education event",
                "relationship": "IS-A",
                "children": [
                    {"id": "01741", "name": "entity", "relationship": "IS-A"},
                ],
            },
        ],
    },
    {
        "id": "40111",
        "name": "department",
        "relationship": "PART-OF",
        "children": [
            {
                "id": "50111",
                "name": "classroom",
                "relationship": "PART-OF",
                "children": [
                    {"id": "50112", "name": "location", "relationship": "IS-A"},
                ],
            },
            {
                "id": "50112",
                "name": "location",
                "relationship": "IS-A",
                "children": [
                    {"id": "01741", "name": "entity", "relationship": "IS-A"},
                ],
            },
        ],
    },
]

# Create the visualization
tree_viz = create_tree_visualization(tree_teleology)

# Save the visualization as a PDF file
tree_viz.render("Language_Teleology", format="pdf", cleanup=True)
print("Tree visualization saved as 'Language_Teleology.pdf'")
