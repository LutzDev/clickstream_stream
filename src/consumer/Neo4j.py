from py2neo import *

class Neo4j:
    graph = Graph("bolt://localhost:7687", auth=("neo4j", "test"))
    matcher = NodeMatcher(graph)
    nodeLabel = "Article"

    @staticmethod
    def hanldeGraph(message):
        prev = Node(Neo4j.nodeLabel, name=message[0])
        curr = Node(Neo4j.nodeLabel, name=message[1])
        relProp = {'date': message[4], 'n': int(message[3])}
        relationship = Relationship(prev, message[2], curr, **relProp)
        Neo4j.graph.merge(relationship, Neo4j.nodeLabel, "name")

    @staticmethod
    def init():
        Neo4j.graph.delete_all()
        Neo4j.graph.run('DROP INDEX ON :Article(name)')
        Neo4j.graph.run('CREATE INDEX ON :Article(name)')
