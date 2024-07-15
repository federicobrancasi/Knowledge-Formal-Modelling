"""
UKC ISA + PART-OF (REDUCED)
This script generates hierarchical tree visualizations of a reduced UKC example for both ISA and PART-OF relationships.
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


def create_node(
    graph, node, parent=None, relationship="IS-A", is_translated=False, language=None
):
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

    graph.node(node_id, node_label, shape="box", style="rounded")

    if parent:
        if relationship == "IS-A":
            graph.edge(node_id, parent, label="IS-A")
        elif relationship == "PART-OF":
            graph.edge(parent, node_id, label="PART-OF", style="dashed", dir="back")

    if "children" in node:
        for child in node["children"]:
            create_node(graph, child, node_id, relationship, is_translated, language)


def create_tree_visualization(isa_trees, part_of_trees):
    """
    Creates a tree visualization from the given trees.

    Args:
        trees (list): A list of trees, each represented as a list of dictionaries.

    Returns:
        graphviz.Digraph: The resulting Graphviz Digraph object.
    """
    dot = graphviz.Digraph(comment="UKC Tree ISA and PART-OF")
    dot.attr(rankdir="BT")  # Bottom to Top direction

    # English Cluster
    with dot.subgraph(name="cluster_0") as c:
        c.attr(label="English")
        root_id = "01740"
        c.node(root_id, "entity\nen47321", shape="box", style="rounded")

        for tree in isa_trees:
            create_node(c, tree[0], root_id, relationship="IS-A")

        rootpartof_id = "45679"
        c.node(rootpartof_id, "entity\nen47321", shape="box", style="rounded")

        for tree in part_of_trees:
            create_node(c, tree[0], rootpartof_id, relationship="PART-OF")

    # UKC Cluster
    with dot.subgraph(name="cluster_1") as c:
        c.attr(label="UKC")
        root_id = "ukc_01740"
        c.node(root_id, generate_random_digit_string(), shape="box", style="rounded")

        for tree in isa_trees:
            create_node(
                c,
                tree[0],
                root_id,
                relationship="IS-A",
                is_translated=True,
                language="ukc",
            )

        rootpartof_id = "55649"
        c.node(rootpartof_id, "55649", shape="box", style="rounded")

        for tree in part_of_trees:
            create_node(
                c,
                tree[0],
                rootpartof_id,
                relationship="PART-OF",
                is_translated=True,
                language="ukc",
            )

    # Italian Cluster
    with dot.subgraph(name="cluster_2") as c:
        c.attr(label="Italiano")
        root_id = "it01740"
        c.node(root_id, "contestuale\nit70650", shape="box", style="rounded")

        for tree in isa_trees:
            create_node(
                c,
                tree[0],
                root_id,
                relationship="IS-A",
                is_translated=True,
                language="italian",
            )

        rootpartof_id = "19268"
        c.node(rootpartof_id, "entità\nen19268", shape="box", style="rounded")

        for tree in part_of_trees:
            create_node(
                c,
                tree[0],
                rootpartof_id,
                relationship="PART-OF",
                is_translated=True,
                language="italian",
            )

    # Edges between clusters
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
        "08094", "ukc_08094", label="", style="dotted", color="#70727B", dir="back"
    )
    dot.edge(
        "it08094", "ukc_08094", label="", style="dotted", color="#70727B", dir="back"
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
        "07846", "ukc_07846", label="", style="dotted", color="#70727B", dir="back"
    )
    dot.edge(
        "it07846", "ukc_07846", label="", style="dotted", color="#70727B", dir="back"
    )

    dot.edge(
        "25323", "ukc_25323", label="", style="dotted", color="#70727B", dir="back"
    )
    dot.edge(
        "it25323", "ukc_25323", label="", style="dotted", color="#70727B", dir="back"
    )

    dot.edge(
        "45356", "ukc_45356", label="", style="dotted", color="#70727B", dir="back"
    )
    dot.edge(
        "it45356", "ukc_45356", label="", style="dotted", color="#70727B", dir="back"
    )

    dot.edge("45679", "55649", label="", style="dotted", color="#70727B", dir="back")
    dot.edge("19268", "55649", label="", style="dotted", color="#70727B", dir="back")

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

    return dot


# Definition of the PART-OF trees
part_of_tree_education = [
    {
        "id": "00100",
        "name": "education",
        "children": [
            {"id": "48472", "name": "lecture"},
            {"id": "25323", "name": "professor"},
            {"id": "45356", "name": "student"},
        ],
    }
]

part_of_tree_events = [
    {
        "id": "00500",
        "name": "events",
        "children": [
            {"id": "48450", "name": "graduation"},
        ],
    }
]

part_of_tree_location = [
    {
        "id": "20001",
        "name": "locations",
        "children": [
            {"id": "30127", "name": "university"},
        ],
    }
]


# Definition of the ISA trees
tree_event = [
    {
        "id": "46884",
        "name": "event",
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
    }
]

tree_location = [
    {
        "id": "08094",
        "name": "location",
        "children": [
            {
                "id": "09526",
                "name": "urban area",
                "children": [
                    {"id": "30127", "name": "university"},
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
                        "id": "25323",
                        "name": "professor",
                    },
                    {
                        "id": "45356",
                        "name": "student",
                    },
                ],
            },
        ],
    }
]

isa_trees = [tree_location, tree_event, tree_person]
part_of_trees = [part_of_tree_education, part_of_tree_events, part_of_tree_location]

tree_viz = create_tree_visualization(isa_trees, part_of_trees)

tree_viz.render("UKC_ISA_PARTOF_REDUCED", format="pdf", cleanup=True)
print("ISA and PART-OF tree visualization saved as 'UKC_ISA_PARTOF_REDUCED.pdf'")
