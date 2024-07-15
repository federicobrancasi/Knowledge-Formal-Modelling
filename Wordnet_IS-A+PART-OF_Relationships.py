"""
WORDNET ISA + PART-OF (EVENT + LOCATION + PERSON)
This script generates hierarchical tree visualizations of a WordNet example for both ISA and PART-OF relationships.
Here we have all three branches: EVENT + LOCATION + PERSON
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

    return dot


# Definition of PART-OF trees
part_of_tree_education = [
    {
        "id": "00100",
        "name": "education",
        "children": [
            {"id": "28560", "name": "academic"},
            {"id": "08660", "name": "Ph.D."},
        ],
    }
]

part_of_tree_events = [
    {
        "id": "00500",
        "name": "events",
        "children": [
            {"id": "48450", "name": "graduation"},
            {"id": "48472", "name": "lecture"},
            {"id": "47358", "name": "conference"},
            {"id": "47375", "name": "seminar"},
        ],
    }
]

part_of_tree_urban = [
    {
        "id": "00200",
        "name": "urban",
        "children": [
            {"id": "30582", "name": "downtown"},
        ],
    }
]

part_of_tree_location = [
    {
        "id": "20001",
        "name": "locations",
        "children": [
            {"id": "12912", "name": "facility"},
            {"id": "30145", "name": "business district"},
            {"id": "61098", "name": "classroom"},
            {"id": "24960", "name": "dormitory"},
            {"id": "58821", "name": "library"},
        ],
    }
]

part_of_tree_people = [
    {
        "id": "00600",
        "name": "people",
        "children": [
            {"id": "07698", "name": "child"},
            {"id": "56237", "name": "undergraduate"},
            {"id": "65489", "name": "graduate"},
        ],
    },
]

# Definition of ISA trees
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

tree_location = [
    {
        "id": "08094",
        "name": "location",
        "children": [
            {
                "id": "09265",
                "name": "geographic area",
                "children": [
                    {
                        "id": "09526",
                        "name": "urban area",
                        "children": [
                            {
                                "id": "30127",
                                "name": "university",
                                "children": [
                                    {"id": "61098", "name": "classroom"},
                                    {"id": "24960", "name": "dormitory"},
                                    {"id": "58821", "name": "library"},
                                ],
                            },
                            {"id": "30582", "name": "downtown"},
                            {"id": "30145", "name": "business district"},
                        ],
                    },
                    {"id": "12912", "name": "facility"},
                ],
            },
        ],
    }
]

tree_person = [
    {
        "id": "10502",
        "name": "person",
        "children": [
            {
                "id": "07846",
                "name": "adult",
                "children": [
                    {
                        "id": "08659",
                        "name": "professional",
                        "children": [
                            {
                                "id": "25323",
                                "name": "professor",
                                "children": [
                                    {"id": "28560", "name": "academic"},
                                    {"id": "08660", "name": "Ph.D."},
                                ],
                            },
                        ],
                    },
                    {
                        "id": "45356",
                        "name": "student",
                        "children": [
                            {"id": "56237", "name": "undergraduate"},
                            {"id": "65489", "name": "graduate"},
                        ],
                    },
                ],
            },
            {
                "id": "07698",
                "name": "child",
            },
        ],
    }
]

# Combine all trees
isa_trees = [tree_event, tree_location, tree_person]
part_of_trees = [
    part_of_tree_events,
    part_of_tree_location,
    part_of_tree_urban,
    part_of_tree_education,
    part_of_tree_people,
]

# Create the visualization
tree_viz = create_tree_visualization(isa_trees, part_of_trees)

# Save the visualization as a PDF file
tree_viz.render("wordnet_ISA&PARTOF", format="pdf", cleanup=True)
print("Tree visualization saved as 'wordnet_ISA&PARTOF.pdf'")
