### Struktur
```
└─┬ root
  |
  ├─┬ ressource
  | |
  | ├─┬ config
  | | └ config.ini
  | |
  | └─┬ data
  |   └ ... // Wikipedia Clickstream-datasets
  |
  ├─┬ src
  | |
  | ├─┬ consumer
  | | ├─ MessageConsumer.py
  | | ├─ MongoDB.py
  | | ├─ Neo4j.py
  | | └ QueryHandler.py
  | |
  | └─┬ producer
  |   ├─ MessageProducer.py
  |   └─ FileReader.py
  |
  └─ .gitignore
```

### Wikipedia-Datasets
https://dumps.wikimedia.org/other/clickstream/
