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

`data/` contains the DEM, veg, and reference snow

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

### CHM

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