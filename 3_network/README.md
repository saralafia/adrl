# Enabling the Discovery of Related Research with Spatialized Library Interfaces - Introduction to Network Analysis with Python 

### Instructors

- [Sara Lafia](http://www.geog.ucsb.edu/~lafia/) - [Center for Spatial Studies, University of California, Santa Barbara]
- [Christina Last](https://www.linkedin.com/in/christina-last/) - [School of Geographical Sciences, University of Bristol]

This tutorial is an introduction to network analysis in Python, with a focus on producing networks from tabular data. It first focuses on introducing the basics of networkx, a well-developed network analysis library in Python. This includes importing visualizing, combining and tidying data for analysis, and uses libraries such as `pandas`, `numpy`, `matplotlib` or `plotly`. The second part will build upon this and focus on more more on spatializing research resources available through a public library repository (https://alexandria.ucsb.edu/collections/f3348hkz). No previous experience with networkx or the other python libraries is needed, but basic familiarity with network data structures and concepts (nodes vs edges) and pandas will be helpful.

## Installation notes

Following this tutorial will require recent installations of:

- Python >= 3.7 (it will probably work on python 2.7 as well, but I didn't test it specifically)
- pandas
- matplotlib
- plotly
- numpy
- networkx

- [Jupyter Notebook](http://jupyter.org)

If you do not yet have these packages installed, we recommend to use the [conda](http://conda.pydata.org/docs/intro.html) package manager to install all the requirements 
(you can install [miniconda](http://conda.pydata.org/miniconda.html) or install the (larger) Anaconda
distribution, found at https://www.anaconda.com/download/).

Once this is installed, the following command will install all required packages in your Python environment:

```
conda env create -f environment.yml
```

But of course, using another distribution (e.g. Enthought Canopy) or ``pip`` is fine as well (a requirements file is provided as well), as long as you have the above packages installed.


## Downloading the tutorial materials

**NOTE:** *We may update the materials up until the workshop. So, please make sure that, if you download the materials, you refresh the downloaded material close to the workshop.*

If you have git installed, you can get the tutorial materials by cloning this repo:

    git clone https://github.com/saralafia/adrl.git

Otherwise, you can download the repository as a .zip file by heading over
to the GitHub repository (https://github.com/saralafia/adrl.git) in
your browser and click the green "Download" button in the upper right:

![](https://drive.google.com/file/d/1kjHYWVVEVTZegJa_sKOifMJiVup8kxzl/view?usp=sharing)

## Test the tutorial environment

To make sure everything was installed correctly, open a terminal, and change its directory (`cd`) so that your working directory is the tutorial materials you downloaded in the step above. Then enter the following:

```sh
python check_environment.py
```

Make sure that this scripts prints "All good. Enjoy the tutorial!"
