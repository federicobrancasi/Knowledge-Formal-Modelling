"""
IS-A WORDNET
This script generates an IS-A hierarchical tree visualization of a WordNet example.
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
    graph.node(node_id, f"{node['name']}\n{node['id']}", shape="box", style="rounded")
    if parent:
        # Creating an edge between the current node and the parent node
        graph.edge(node_id, parent, label="IS-A")
    # Recursively creating child nodes
    for child in node.get("children", []):
        create_node(graph, child, node_id)


def create_tree_visualization(trees):
    """
    Creates a tree visualization from the given trees.

    Args:
        trees (list): A list of trees, each represented as a list of dictionaries.

    Returns:
        graphviz.Digraph: The resulting Graphviz Digraph object.
    """
    dot = graphviz.Digraph(comment="WordNet Tree")
    dot.attr(rankdir="BT")  # Bottom to Top direction

    # Creating the root node "entity" and the "contextual entity"
    root_id = "entity_01740"
    # dot.node(root_id, "contextual entity\n47321", shape='box', style='rounded')
    # dot.node("contentity_01740", "entity\n01740", shape='box', style='rounded')
    # dot.edge("entity_01740", "contentity_01740", "IS-A")
    dot.node(root_id, "entity\n47321", shape="box", style="rounded")

    # Creating nodes for each tree and linking to the root
    for tree in trees:
        create_node(dot, tree[0], root_id)

    return dot


# Definition of IS-A trees
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
all_trees = [tree_event, tree_location, tree_person]

# Create the visualization
tree_viz = create_tree_visualization(all_trees)

# Save the visualization as a PDF file
tree_viz.render("wordnet_ISA", format="pdf", cleanup=True)
print("Tree visualization saved as 'wordnet_ISA.pdf'")
