"""
WORDNET ISA + PART-OF (EVENT)
This script generates hierarchical tree visualizations of a WordNet example for both ISA and PART-OF relationships.
Here we focus on the EVENT branch.
"""

import graphviz


def create_node(graph, node, parent=None, relationship="ISA"):
    """
    Creates a node in the graph and links it to the parent node if specified.

    Args:
        graph (graphviz.Digraph): The Graphviz Digraph object.
        node (dict): The current node represented as a dictionary with 'name' and 'id' keys.
        parent (str, optional): The ID of the parent node. Default is None.
        relationship (str): The type of relationship for the edge ("ISA" or "PART-OF").
    """
    node_id = f"{node['name']}_{node['id']}"
    # Adding the node to the graph with a specific shape and style
    graph.node(node_id, f"{node['name']}\n{node['id']}", shape="rect", style="rounded")
    if parent:
        # Creating an edge based on the relationship type
        if relationship == "ISA":
            graph.edge(node_id, parent, label="IS-A")
        elif relationship == "PART-OF":
            graph.edge(parent, node_id, label="PART-OF", style="dashed", dir="back")
    # Recursively creating child nodes if present
    for child in node.get("children", []):
        create_node(graph, child, node_id, relationship)


def create_tree_visualization(isa_trees, part_of_trees):
    """
    Creates a combined ISA and PART-OF tree visualization from the given trees.

    Args:
        isa_trees (list): A list of ISA trees, each represented as a list of dictionaries.
        part_of_trees (list): A list of PART-OF trees, each represented as a list of dictionaries.

    Returns:
        graphviz.Digraph: The resulting Graphviz Digraph object.
    """
    dot = graphviz.Digraph(comment="WordNet Hierarchical Trees")
    dot.attr(rankdir="BT")  # Bottom to Top direction

    # Create nodes for ISA trees
    root_id = "entityisa_01740"
    # dot.node(root_id, "contextual entity\n47321", shape='rect', style='rounded')
    dot.node(root_id, "entity\n47321", shape="rect", style="rounded")
    for tree in isa_trees:
        for subtree in tree:
            create_node(dot, subtree, root_id, "ISA")

    # Create nodes for PART-OF tree
    part_of_root_id = "entitypartof_01740"
    dot.node(part_of_root_id, "entity\n01740", shape="rect", style="rounded")
    for tree in part_of_trees:
        for subtree in tree:
            create_node(dot, subtree, part_of_root_id, "PART-OF")

    # dot.node("contentity_01740", "entity\n01740", shape='box', style='rounded')
    # dot.edge("entityisa_01740", "contentity_01740", "IS-A")

    return dot


# Definizione dell'albero PART-OF
part_of_tree_education = [
    {
        "id": "00100",
        "name": "education",
        "children": [
            {"id": "48472", "name": "lecture"},
        ],
    }
]

part_of_tree_events = [
    {
        "id": "00500",
        "name": "events",
        "children": [
            {"id": "48450", "name": "graduation"},
            {"id": "47358", "name": "conference"},
            {"id": "47375", "name": "seminar"},
        ],
    }
]

# Definizione degli alberi IS-A
tree_event = [
    {
        "id": "46884",
        "name": "event",
        "children": [
            {
                "id": "46988",
                "name": "social event",
                "children": [
                    {
                        "id": "48370",
                        "name": "university event",
                        "children": [
                            {"id": "48450", "name": "graduation"},
                            {"id": "48472", "name": "lecture"},
                        ],
                    },
                ],
            },
            {
                "id": "47309",
                "name": "professional event",
                "children": [
                    {"id": "47358", "name": "conference"},
                    {"id": "47375", "name": "seminar"},
                ],
            },
        ],
    }
]

# Combine all trees
isa_trees = [tree_event]
part_of_trees = [part_of_tree_events, part_of_tree_education]

# Create the visualization
tree_viz = create_tree_visualization(isa_trees, part_of_trees)

# Save the visualization as a PDF file
tree_viz.render("wordnet_ISA&PARTOF_EVENT", format="pdf", cleanup=True)
print("Tree visualization saved as 'wordnet_ISA&PARTOF_EVENT.pdf'")
