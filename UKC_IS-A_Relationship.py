"""
IS-A UKC
This script generates an IS-A hierarchical tree visualization of a UKC example.
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


def translate_to_italian(name):
    """Translates the English name to Italian.

    Args:
      name (str): The English name to be translated.

    Returns:
        str: The translated Italian name.
    """
    translations = {
        "entity": "entità",
        "event": "evento",
        "social event": "evento sociale",
        "private event": "evento privato",
        "university event": "evento universitario",
        "graduation": "laurea",
        "university lecture": "lezione universitaria",
        "professional event": "evento professionale",
        "conference": "conferenza",
        "seminar": "seminario",
        "workshop": "workshop",
        "location": "luogo",
        "geographic area": "area geografica",
        "urban area": "area urbana",
        "university": "università",
        "classroom": "aula",
        "dormitory": "dormitorio",
        "library": "biblioteca",
        "downtown": "centro città",
        "business district": "quartiere degli affari",
        "facility": "struttura",
        "person": "persona",
        "adult": "adulto",
        "professional": "professionista",
        "lawyer": "avvocato",
        "professor": "professore",
        "academic": "accademico",
        "Ph.D.": "dottore di ricerca",
        "student": "studente",
        "undergraduate student": "studente universitario",
        "graduate student": "studente laureato",
        "child": "bambino",
    }
    return translations.get(name, name)


def create_node(graph, node, parent=None, is_translated=False, language=None):
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
    if is_translated:
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
            node_id = f"{prefix}{node['id']}"
            node_label = f"{node_name}\n{node_id}"
    else:
        prefix = "en"
        node_id = f"{node['id']}"
        node_name = node["name"]
        node_label = f"{node_name}\n{prefix}{node_id}"

    if language != "ukc":
        graph.node(node_id, node_label, shape="box", style="rounded")
    else:
        graph.node(node_id, node_label, shape="box", style="rounded")

    if parent:
        graph.edge(node_id, parent, label="IS-A")

    if "children" in node:
        for child in node["children"]:
            create_node(graph, child, node_id, is_translated, language)


def create_tree_visualization(trees):
    """
    Creates a tree visualization from the given trees.

    Args:
        trees (list): A list of trees, each represented as a list of dictionaries.

    Returns:
        graphviz.Digraph: The resulting Graphviz Digraph object.
    """
    dot = graphviz.Digraph(comment="UKC Tree")
    dot.attr(rankdir="BT")  # Bottom to Top direction

    with dot.subgraph(name="cluster_0") as c:
        c.attr(label="English")
        root_id = "01740"
        c.node(root_id, "entity\nen47321", shape="box", style="rounded")

        for tree in trees:
            create_node(c, tree[0], root_id)

    with dot.subgraph(name="cluster_1") as c:
        c.attr(label="UKC")
        root_id = "ukc_01740"
        c.node(root_id, generate_random_digit_string(), shape="box", style="rounded")

        for tree in trees:
            create_node(c, tree[0], root_id, is_translated=True, language="ukc")

    with dot.subgraph(name="cluster_2") as c:
        c.attr(label="Italiano")
        root_id = "it01740"
        c.node(root_id, "entità\nit70650", shape="box", style="rounded")

        for tree in trees:
            create_node(c, tree[0], root_id, is_translated=True, language="italian")

    dot.edge(
        "01740", "ukc_01740", label="", style="dotted", color="#70727B", dir="back"
    )
    dot.edge(
        "it01740", "ukc_01740", label="", style="dotted", color="#70727B", dir="back"
    )

    dot.edge(
        "46884", "ukc_46884", label="", style="dotted", color="#70727B", dir="back"
    )
    dot.edge(
        "it46884", "ukc_46884", label="", style="dotted", color="#70727B", dir="back"
    )

    dot.edge(
        "46988", "ukc_46988", label="", style="dotted", color="#70727B", dir="back"
    )
    dot.edge(
        "it46988", "ukc_46988", label="", style="dotted", color="#70727B", dir="back"
    )

    dot.edge(
        "48370", "ukc_48370", label="", style="dotted", color="#70727B", dir="back"
    )
    dot.edge(
        "it48370", "ukc_48370", label="", style="dotted", color="#70727B", dir="back"
    )

    dot.edge(
        "48450", "ukc_48450", label="", style="dotted", color="#70727B", dir="back"
    )
    dot.edge(
        "it48450", "ukc_48450", label="", style="dotted", color="#70727B", dir="back"
    )

    dot.edge(
        "48472", "ukc_48472", label="", style="dotted", color="#70727B", dir="back"
    )
    dot.edge(
        "it48472", "ukc_48472", label="", style="dotted", color="#70727B", dir="back"
    )

    dot.edge(
        "47309", "ukc_47309", label="", style="dotted", color="#70727B", dir="back"
    )
    dot.edge(
        "it47309", "ukc_47309", label="", style="dotted", color="#70727B", dir="back"
    )

    dot.edge(
        "47358", "ukc_47358", label="", style="dotted", color="#70727B", dir="back"
    )
    dot.edge(
        "it47358", "ukc_47358", label="", style="dotted", color="#70727B", dir="back"
    )

    dot.edge(
        "47375", "ukc_47375", label="", style="dotted", color="#70727B", dir="back"
    )
    dot.edge(
        "it47375", "ukc_47375", label="", style="dotted", color="#70727B", dir="back"
    )

    dot.edge(
        "08094", "ukc_08094", label="", style="dotted", color="#70727B", dir="back"
    )
    dot.edge(
        "it08094", "ukc_08094", label="", style="dotted", color="#70727B", dir="back"
    )

    dot.edge(
        "09265", "ukc_09265", label="", style="dotted", color="#70727B", dir="back"
    )
    dot.edge(
        "it09265", "ukc_09265", label="", style="dotted", color="#70727B", dir="back"
    )

    dot.edge(
        "09526", "ukc_09526", label="", style="dotted", color="#70727B", dir="back"
    )
    dot.edge(
        "it09526", "ukc_09526", label="", style="dotted", color="#70727B", dir="back"
    )

    dot.edge(
        "30127", "ukc_30127", label="", style="dotted", color="#70727B", dir="back"
    )
    dot.edge(
        "it30127", "ukc_30127", label="", style="dotted", color="#70727B", dir="back"
    )

    dot.edge(
        "61098", "ukc_61098", label="", style="dotted", color="#70727B", dir="back"
    )
    dot.edge(
        "it61098", "ukc_61098", label="", style="dotted", color="#70727B", dir="back"
    )

    dot.edge(
        "24960", "ukc_24960", label="", style="dotted", color="#70727B", dir="back"
    )
    dot.edge(
        "it24960", "ukc_24960", label="", style="dotted", color="#70727B", dir="back"
    )

    dot.edge(
        "58821", "ukc_58821", label="", style="dotted", color="#70727B", dir="back"
    )
    dot.edge(
        "it58821", "ukc_58821", label="", style="dotted", color="#70727B", dir="back"
    )

    dot.edge(
        "30582", "ukc_30582", label="", style="dotted", color="#70727B", dir="back"
    )
    dot.edge(
        "it30582", "ukc_30582", label="", style="dotted", color="#70727B", dir="back"
    )

    dot.edge(
        "30145", "ukc_30145", label="", style="dotted", color="#70727B", dir="back"
    )
    dot.edge(
        "it30145", "ukc_30145", label="", style="dotted", color="#70727B", dir="back"
    )

    dot.edge(
        "12912", "ukc_12912", label="", style="dotted", color="#70727B", dir="back"
    )
    dot.edge(
        "it12912", "ukc_12912", label="", style="dotted", color="#70727B", dir="back"
    )

    dot.edge(
        "07846", "ukc_07846", label="", style="dotted", color="#70727B", dir="back"
    )
    dot.edge(
        "it07846", "ukc_07846", label="", style="dotted", color="#70727B", dir="back"
    )

    dot.edge(
        "08659", "ukc_08659", label="", style="dotted", color="#70727B", dir="back"
    )
    dot.edge(
        "it08659", "ukc_08659", label="", style="dotted", color="#70727B", dir="back"
    )

    dot.edge(
        "25323", "ukc_25323", label="", style="dotted", color="#70727B", dir="back"
    )
    dot.edge(
        "it25323", "ukc_25323", label="", style="dotted", color="#70727B", dir="back"
    )

    dot.edge(
        "28560", "ukc_28560", label="", style="dotted", color="#70727B", dir="back"
    )
    dot.edge(
        "it28560", "ukc_28560", label="", style="dotted", color="#70727B", dir="back"
    )

    dot.edge(
        "45356", "ukc_45356", label="", style="dotted", color="#70727B", dir="back"
    )
    dot.edge(
        "it45356", "ukc_45356", label="", style="dotted", color="#70727B", dir="back"
    )

    dot.edge(
        "56237", "ukc_56237", label="", style="dotted", color="#70727B", dir="back"
    )
    dot.edge(
        "it56237", "ukc_56237", label="", style="dotted", color="#70727B", dir="back"
    )

    dot.edge(
        "65489", "ukc_65489", label="", style="dotted", color="#70727B", dir="back"
    )
    dot.edge(
        "it65489", "ukc_65489", label="", style="dotted", color="#70727B", dir="back"
    )

    dot.edge(
        "07698", "ukc_07698", label="", style="dotted", color="#70727B", dir="back"
    )
    dot.edge(
        "it07698", "ukc_07698", label="", style="dotted", color="#70727B", dir="back"
    )

    return dot


# Definition of the IS-A trees
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
tree_viz.render("UKC_ISA", format="pdf", cleanup=True)
print("Tree visualization saved as 'UKC_ISA.pdf'")
