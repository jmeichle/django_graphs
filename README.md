# What dis?

A django app with a basic graph DB schema (graphs that have nodes, and edges that connect nodes). Frameworking for juypter notebook interaction. Thats about it.

# Installation/setup

Create virtualenv with python 3.6.8, then:

```
pip install -r requirements
```

Then choose a DB type. The easiest is sqlite3

### Sqlite3

The DB will automatically be created as a file `db.sqlite3` when migrations are ran. Nothing is needed.

### Mysql

Create a DB user via (`sudo mysql --user=root mysql`)

```
CREATE USER 'django'@'%' IDENTIFIED BY 'password';
GRANT ALL PRIVILEGES ON *.* TO 'django'@'%' WITH GRANT OPTION;
FLUSH PRIVILEGES;
CREATE DATABASE graphs;
```

## Run DB migrations

```
python manage.py migrate
```

# Usage

Below are usage cases

## To use the webserver (just list graphs by name):

```
python manage.py runserver 8000
```

then load http://localhost:8000/

## To use the juypter notebook:

```
bash start_notebook.sh
```

## IPython with Django models loaded:


NOTE: this just runs `graphs/management/commands/graph_shell.py` which is very simple:

```
python manage.py graph_shell
```

## Create a graph

What this is doing is creating a single graph, with two nodes, and an edge between the FirstNode and SecondNode. This is a Graph and not a Directed graph since the NodeEdge model that maps nodes to edges does not encapsulate or enforce directionality. Its a bit verbose:

- Create the graph
- Create nodes 1 and 2
- Creates the edge (which doesnt link to any nodes)
- Creates the edge<->node mapping for the edge to the first node
- Creates the edge<->node mapping for the edge to the second node

### django shell (IPython)

```
jmeichle@stacy-desktop:~/projects/graphs_graphs_graphs$ python manage.py graph_shell
DB Models Loaded. Starting IPython
Python 3.6.8 (default, Feb  3 2019, 19:24:14) 
Type 'copyright', 'credits' or 'license' for more information
IPython 7.5.0 -- An enhanced Interactive Python. Type '?' for help.

In [1]: g = Graph.objects.create(name="test")

In [2]: n1 = Node.objects.create(graph=g, value="FirstNode")

In [3]: n2 = Node.objects.create(graph=g, value="SecondNode")

In [4]: e1 = Edge.objects.create(graph=g, value='foobar')

In [5]: ne1 = NodeEdge.objects.create(node=n1, edge=e1)

In [6]: ne2 = NodeEdge.objects.create(node=n2, edge=e1)
```

### Management command / script

```
jmeichle@stacy-desktop:~/projects/django_graphs$ python manage.py create_dumb_graph
DB Models Loaded. Creating a dumb Graph of two nodes linked.
Creating graph with name=test
Creating Node with name=FirstNode
Creating Node with name=SecondNode
Creating Edge with value=foobar
Relating Edge=foobar to node=FirstNode
Relating Edge=foobar to node=SecondNode
Done.
```