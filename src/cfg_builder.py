
from ast_builder import ASTNode
import networkx as nx
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt


class CFGNode:
    def __init__(self, name):
        self.name = name
        self.statements = []
        self.next = []

    def __repr__(self):
        stmts = [s.type if hasattr(s, 'type') else str(s) for s in self.statements]
        return f"{self.name}: {stmts}"


class CFGBuilder:
    def __init__(self):
        self.counter = 1

    def new_node(self):
        node = CFGNode(f"BB{self.counter}")
        self.counter += 1
        return node

    def build(self, ast: ASTNode):
        entry = self.new_node()
        exit_node = self._build_block(ast, entry)
        return entry, exit_node

    def _build_block(self, node: ASTNode, current: CFGNode):
        if node is None:
            return current

        if node.type == "block":
            last_node = current
            for stmt in node.children or []:
                last_node = self._build_block(stmt, last_node)
            return last_node


        if node.type in ("int_decl", "assign", "expr_stmt", "return"):
            new_node = self.new_node()
            new_node.statements.append(node)
            current.next.append(new_node)
            return new_node

        # if
        if node.type == "if":
            cond_node = self.new_node()
            cond_node.statements.append(node.children[0])  # شرط
            current.next.append(cond_node)


            then_entry = self.new_node()
            then_exit = self._build_block(node.children[1], then_entry)


            end_node = self.new_node()

            cond_node.next.append(then_entry)


            if len(node.children) > 2 and node.children[2]:
                else_entry = self.new_node()
                else_exit = self._build_block(node.children[2], else_entry)
                cond_node.next.append(else_entry)
                then_exit.next.append(end_node)
                else_exit.next.append(end_node)
            else:
                then_exit.next.append(end_node)
                cond_node.next.append(end_node)

            return end_node


        if node.type == "while":
            cond_node = self.new_node()
            cond_node.statements.append(node.children[0])
            current.next.append(cond_node)

            body_entry = self.new_node()
            body_exit = self._build_block(node.children[1], body_entry)
            body_exit.next.append(cond_node)  # loop back

            end_node = self.new_node()
            cond_node.next.append(body_entry)  # true branch
            cond_node.next.append(end_node)    # false branch

            return end_node


        new_node = self.new_node()
        new_node.statements.append(node)
        current.next.append(new_node)
        return new_node


def plot_cfg(entry_node: CFGNode):
    G = nx.DiGraph()
    visited = set()

    def dfs(node):
        if node in visited:
            return
        visited.add(node)
        label = f"{node.name}\n" + "\n".join([s.type for s in node.statements])
        G.add_node(node.name, label=label)
        for nxt in node.next:
            G.add_edge(node.name, nxt.name)
            dfs(nxt)

    dfs(entry_node)

    pos = nx.spring_layout(G)
    labels = nx.get_node_attributes(G, 'label')
    nx.draw(G, pos, labels=labels, node_size=2000, node_color="skyblue", font_size=10)
    plt.show()
