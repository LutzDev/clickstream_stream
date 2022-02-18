from MongoDB import MongoDB
from Neo4j import Neo4j




# Queries
def mostRelationships():
    result = (Neo4j.graph.run("MATCH (n)<-[r]-() RETURN n.articleID, count(DISTINCT r) AS num ORDER BY num desc Limit 5"))
    MongoDB.insert("Dezember21", {"mostRelationships": result})

def mostRelationshipsTypeExternal():
    result = Neo4j.graph.run("MATCH (n)<-[r:External]-() RETURN n.articleID, count(DISTINCT r) AS num ORDER BY num desc Limit 5")
    MongoDB.insert("Dezember21", {"mostRelationshipsTypeExternal": result})

def mostRelationshipsTypeLink():
    result =  Neo4j.graph.run("MATCH (n)<-[r:Link]-() RETURN n.articleID, count(DISTINCT r) AS num ORDER BY num desc Limit 5")
    MongoDB.insert("Dezember21", {"mostRelationshipsTypeLink": result})

def mostRelationshipsTypeOther():
    result = Neo4j.graph.run("MATCH (n)<-[r:Other]-() RETURN n.articleID, count(DISTINCT r) AS num ORDER BY num desc Limit 5")
    MongoDB.insert("Dezember21", {"mostRelationshipsTypeLink": result})

def mostRelationshipsTypeOther():
    result = Neo4j.graph.run("MATCH (n)<-[r:Other]-() RETURN n.articleID, count(DISTINCT r) AS num ORDER BY num desc Limit 5")
    MongoDB.insert("Dezember21", {"mostRelationshipsTypeOther": result})

def mostPageCalls():
    result = Neo4j.graph.run("MATCH (n)<-[r]-() RETURN n.articleID, sum(toInteger(r.n)) AS num ORDER BY num desc Limit 5")
    MongoDB.insert("Dezember21", {"mostPageCalls": result})

def queryAll():
    mostPageCalls()
    mostRelationshipsTypeOther()
    mostRelationshipsTypeExternal()
    mostRelationshipsTypeLink()
    mostRelationships()
