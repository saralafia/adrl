# Interactive Visualiation 

### Author

- [Christina Last](https://www.linkedin.com/in/christina-last/) - [School of Geographical Sciences, University of Bristol]

These two demos illustrate an interactive visualisation that enables user to navigate through a network of research objects, which enables questions about connections between research objects or about centrality.

## Functionality
- Nodes are coloured by their department, labelled with the document title and scaled by their relative topic weight.
- Edges, which are weighted by the source node weight * target node weight, are coloured by the source node department, and represent a shared top topic between documents.

## Interactivity 
- Navigating the demo can be done by 'click and drag'
- Zoom in and out to a particular part of the network to reveal the nodel label (document title)
- Selecting a node will highlight the node and its label
- Selecting or hovering over a node will list the "Department of Selected Node" and a "List of the titles of all nodes connected to selected node".

![](https://github.com/saralafia/adrl/blob/master/3_network/Interactive_Visualisation/screen_record.gif)

## Installation notes

Following this tutorial will require recent installations of:

- Python >= 3.7
- pandas
- matplotlib
- chart_studio
- plotly
- networkx
- pyvis
- [Jupyter Notebook](http://jupyter.org)

If you do not yet have these packages installed, we recommend to use the [conda](http://conda.pydata.org/docs/intro.html) package manager to install all the requirements 
(you can install [miniconda](http://conda.pydata.org/miniconda.html) or install the (larger) Anaconda
distribution, found at https://www.anaconda.com/download/).
