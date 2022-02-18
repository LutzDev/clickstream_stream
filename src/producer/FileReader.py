import os
import pandas as pd
import csv

from datetime import date
from src.consumer.Neo4j import Neo4j
from MessageProducer import MessageProducer

# Reset Neo4j Database and create indexes
# Neo4j.init()

file = os.path.join(os.path.dirname(__file__), '../../ressource/data/clickstream-dewiki-2021-03.tsv')

count = 0;

df = pd.read_csv(file, sep='\t', names=["coming_from", "article", "referrer_type", "n"],
                 dtype={"referrer_type": "category"},
                 on_bad_lines="skip",
                 quoting=csv.QUOTE_NONE
                 )

df = df.reset_index()

for index, row in df.iterrows():
    count += 1
    if count % 100000 == 0:
        print(count)

    MessageProducer.sendMessage([row['coming_from'], row['article'], row['referrer_type'], row["n"], date(year=2020, month=1, day=1)])

