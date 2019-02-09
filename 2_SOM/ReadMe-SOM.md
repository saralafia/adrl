## Self-Organizing Map
###Author
- [Sara Lafia](http://www.geog.ucsb.edu/~lafia/) - [Center for Spatial Studies, University of California, Santa Barbara]

### SOM Analyst
Run [**SOM Analyst**](<http://code.google.com/p/somanalyst>) with the following parameters:

* x / y dimensions: 42x42 (i.e., 1764 hexagons)
* length of training: 50,000 / 500,000
* initial neighborhood radius: 42 / 6

Output of nine steps in SOM Analyst is stored in folder, **"SOM_output"**.

### Publishing to ArcGIS Online
Subset 1,730 research resources (**"Theses_all.csv"**) to 775 (**"Theses_selected.csv"**) displaying the publications from the largest departments (i.e. over fifty publications). Publish neurons as basemap and point set as a feature layer to ArcGIS Online. Both layers are available through a public facing [application](<http://arcg.is/rmuKf>):

![SOM](https://drive.google.com/uc?export=view&id=1XG_mXX9BFRnT944srSeYzFj_A28REvxF)