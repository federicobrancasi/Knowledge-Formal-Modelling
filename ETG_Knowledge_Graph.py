"""
ETG KNOWLEDGE GRAPH VISUALIZATION
This script generates an Entity Type Knowledge Graph visualization.
"""

import graphviz


def create_entity_node(graph, node):
    """
    Creates an entity node in the graph with a custom label.

    Args:
        graph (graphviz.Digraph): The Graphviz Digraph object.
        node (dict): The current node represented as a dictionary with 'name' and 'id' keys.
    """
    node_id = f"{node['name']}_{node['id']}"
    nodeName = node["name"]
    nodeId = node["id"]

    # Define labels for each type of node
    if nodeName == "professor":
        label = f"{{ {nodeName} | {nodeId} | name : string | age : int }}"
    elif nodeName == "student":
        label = f"{{ {nodeName} | {nodeId} | name : string | age : int }}"
    elif nodeName == "university":
        label = f"{{ {nodeName} | {nodeId} | name : string | location : string }}"
    elif nodeName == "lecture":
        label = f"{{ {nodeName} | {nodeId} | title : string | duration : int }}"
    elif nodeName == "department":
        label = f"{{ {nodeName} | {nodeId} | name : string | head : string }}"
    elif nodeName == "course":
        label = f"{{ {nodeName} | {nodeId} | title : string | credits : int }}"
    elif nodeName == "classroom":
        label = f"{{ {nodeName} | {nodeId} | number : string | capacity : int }}"
    elif nodeName == "research project":
        label = f"{{ {nodeName} | {nodeId} | title : string | duration : int }}"
    elif nodeName == "administrative staff":
        label = f"{{ {nodeName} | {nodeId} | name : string | age : int }}"
    else:
        label = f"{{ {nodeName} | {nodeId} }}"

    # Adding the node to the graph with the specified label
    graph.node(node_id, label, shape="record", style="rounded")


def create_relationship_graph(entities, relationships):
    """
    Creates a graph visualization with specified entities and relationships.

    Args:
        entities (list): A list of entity dictionaries.
        relationships (list): A list of relationship dictionaries.

    Returns:
        graphviz.Digraph: The resulting Graphviz Digraph object.
    """
    dot = graphviz.Digraph(comment="Complex University Relationship Graph")

    # Creating nodes for each entity
    for entity in entities:
        create_entity_node(dot, entity)

    # Creating edges for each relationship
    for rel in relationships:
        source_id = f"{rel['source']['name']}_{rel['source']['id']}"
        target_id = f"{rel['target']['name']}_{rel['target']['id']}"
        dot.edge(source_id, target_id, label=rel["label"])

    return dot


# Definition of entities
entities = [
    {"id": "25323", "name": "professor"},
    {"id": "45356", "name": "student"},
    {"id": "30127", "name": "university"},
    {"id": "48472", "name": "lecture"},
    {"id": "52830", "name": "department"},
    {"id": "19473", "name": "course"},
    {"id": "37549", "name": "classroom"},
    {"id": "65984", "name": "research project"},
    {"id": "84321", "name": "administrative staff"},
]

# Definition of relationships
relationships = [
    {
        "source": {"name": "student", "id": "45356"},
        "target": {"name": "lecture", "id": "48472"},
        "label": "attends",
    },
    {
        "source": {"name": "professor", "id": "25323"},
        "target": {"name": "lecture", "id": "48472"},
        "label": "holds",
    },
    {
        "source": {"name": "professor", "id": "25323"},
        "target": {"name": "department", "id": "52830"},
        "label": "belongs to",
    },
    {
        "source": {"name": "department", "id": "52830"},
        "target": {"name": "university", "id": "30127"},
        "label": "part of",
    },
    {
        "source": {"name": "course", "id": "19473"},
        "target": {"name": "department", "id": "52830"},
        "label": "offered by",
    },
    {
        "source": {"name": "student", "id": "45356"},
        "target": {"name": "course", "id": "19473"},
        "label": "enrolls in",
    },
    {
        "source": {"name": "lecture", "id": "48472"},
        "target": {"name": "course", "id": "19473"},
        "label": "part of",
    },
    {
        "source": {"name": "lecture", "id": "48472"},
        "target": {"name": "classroom", "id": "37549"},
        "label": "held in",
    },
    {
        "source": {"name": "professor", "id": "25323"},
        "target": {"name": "research project", "id": "65984"},
        "label": "supervises",
    },
    {
        "source": {"name": "research project", "id": "65984"},
        "target": {"name": "university", "id": "30127"},
        "label": "funded by",
    },
    {
        "source": {"name": "administrative staff", "id": "84321"},
        "target": {"name": "department", "id": "52830"},
        "label": "manages",
    },
]

# Create the visualization
complex_relationship_viz = create_relationship_graph(entities, relationships)

# Save the visualization as a PDF file
complex_relationship_viz.render("ETG", format="pdf", cleanup=True)
print("Complex graph visualization saved as 'ETG.pdf'")
