PostGIS
=========

Installation
-------------

For windows, use Stack Builder which is installed together with PostGreSQL.
Under Category > Spatial Extensions > select the PostGIS version for installation.

For Ubuntu, it is easier to use Docker for installation.


Upload Shapefiles
------------------

It is easiest to use postgisgui for uploading shapefiles. 
Go to ``C:\Program Files\PostgreSQL\9.6\bin\postgisgui`` or whichever directory PostGres was installed in. Double click the application.

.. figure:: img/postgis1.PNG
    :width: 300px
    :align: center
    :figclass: align-center

Open the connection button and connect to the database.
    
.. figure:: img/postgis2.PNG
    :width: 400px
    :align: center
    :figclass: align-center
    
Remember to add the SRID. 3414 is the coordinate system for Singapore's SVY21.

Spatial indexing is automatically done using this tool when uploading the shapefiles to PostGIS.


Editing
----------

**ArcGIS** by default does not allow editing. However, 3rd party paid extensions like gisquirrel allows this.

**QGIS** bby default allows for editing/deleting.


Map Service
------------

GeoServer can be connected to PostGIS & published the layers. In GeoServer, create a new store with connection to PostGIS,
and select the relevant tables to publish as a WMS.

.. figure:: img/postgis3.png
    :width: 400px
    :align: center
    :figclass: align-center

Queries
----------

.. code::
  
  # PostGIS version
  SELECT PostGIS_full_version();
  
  # Data directory path
  show data_directory;

