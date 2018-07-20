Simple features is a standard interface for access and manipulation of spatial vector data (points, lines, polygons). Predating the simple features package, spatial vector data in package `sp` is difficult to work with by its S4 nature, where objects store spatial geometries separately from associated attribute data, matching by order. The `sp` implementation is hard to maintain because it contains incremental changes from a baseline that predated the industry-standard (simple features). 

Tidy data is defined as 
1. Each variable forms a column
2. Each observation forms a row
3. Each type of observational unit forms a table
Tidy rule for simple feature means each feature forms a row.  asingle column contains the geometry for each observation, thereby representing the spatial feature in a classic tidy dataframe. 

What do we want to do:
1. Learn what is available
   * https://github.com/edzer/UseR2017/blob/master/tutorial.Rmd
   * `methods("sf")`
      * reading in and basic shaping (st_as_sf, as(x, "Spatial"))
      * logical binary geometry predicates - st_intersects, st_disjoint, etc
      * geometry generating logical operators - st_intersection etc
      * higher level - summarise, interpolate, st_join
      * manipulating geometries
   * simple features vignette
   * simple features Github issues
2. Take point data from csv and turn into spatial features
   * crs
      * http://spatialreference.org/ref/epsg/4326/
   * `st_as_sf`
3. Shaping the data using classic R dplyr methods
4. Load in polygons
   * aggregate polygons up a level
   * intersect points with polygons
     * st_intersect vs st_intersection
     * st_transform
5. Summary statistics
6. Plotting


http://www.maths.lancs.ac.uk/~rowlings/Teaching/UseR2012/crime.html crime
http://www.rspatial.org/cases/rst/3-speciesdistribution.html wild potatoes

Steps:
1. Install `sf`
2. Things that we 