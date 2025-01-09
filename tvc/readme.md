# Trail Valley Creek

Lidar and met data from Philip Marsh. Reproduced with permission

Met data:

Tutton, Rosamond; Dakin, Brampton; Essery, Richard; Griffith, Jory; Hould-Gosselin, Gabriel; Marsh, Philip; Sonnentag, Oliver; Thorne, Robin; Walker, Branden, 2024, "A hydrometeorological dataset from the taiga-tundra ecotone in the western Canadian Arctic: Trail Valley Creek, Northwest Territories (1991-2023)", https://doi.org/10.5683/SP3/BXV4DE

Lidar data:
https://tc.copernicus.org/articles/13/3045/2019/

# Spack env
Load the anon space env with 

```
$ spacktivate .
```

Upon activating it the first time, install the env:
```
$ spack concretize -f
$ spack install
```

# folders

`data/` contains the DEM, veg, and observed snow depth
`wind/` contains the code to run windmapper
`mesher/` contains the code to produce the mesh from the DEM and windmapper outputs
`chm/` contains the configuration file to run CHM
`analysis` contains the jupyter notebook to do analysis on the output with python

# Run stesp 
## 1 - Windmapper
`wind` is where windmapper is run from:

```
windmapper.py windmapper_config.py
```

The internal projection windmapper needs to do to ensure an exactly rectangular domain results in a smaller than input domain.

`wind/windmapper_config/shp/user_bbox.shp` contains this modified extent which mesher can ingest to clip to.

## 1b 
run `windmapper2mesher windmapper_config` or use the `wind/wind2mesher.sh` to generate the wind parameters that need to go into mesher
these are output to stdout as well as `config_WN.txt`

## 2 - mesher

```
$ mesher tvc.py
```

The resulting mesh is given in `meshes/tvc/*.mesh` and `meshes/tvc/*.param`

In `meshes/tvc/DEM_TVC_Lakes_2x2m_NAD83_UTM8N_TUPSR50DRIFT/DEM_TVC_Lakes_2x2m_NAD83_UTM8N_TUPSR50DRIFT.vtu` can be loaded into Paraview to view the resulting mesh. The `.shp` can be loaded into a GIS.


The hdf5 mesh loads much faster at runtime, so convert to h5
```
partition -m DEM_TVC_Lakes_2x2m_NAD83_UTM8N_TUPSR50DRIFT.mesh -p DEM_TVC_Lakes_2x2m_NAD83_UTM8N_TUPSR50DRIFT.param
```

## 3 - CHM

CHM likes paths relative to the running dir so create a symlink to the meshes

```
$ cd chm
$ ln -s ../meshes/tvc meshes
$ ln -s ../met/siksik_1hr_chm_2012-2013.txt .
```

then run chm

```
$ CHM -f tvc_config.json
```

## 4 - Analysis

Using the jupyter notebook, convert the CHM output to structured grid (tif file) for analysis