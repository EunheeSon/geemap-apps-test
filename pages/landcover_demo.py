#!/usr/bin/env python
# coding: utf-8

# <a href="https://githubtocolab.com/gee-community/geemap/blob/master/examples/notebooks/116_land_cover_timeseries.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open in Colab"/></a>

# In[ ]:


# !pip install geemap


# In[ ]:

try:
    import ee
    import geemap


    # In[ ]:


    Map = geemap.Map()
    Map.add_basemap('HYBRID')
    Map


    # In[ ]:


    # Set the region of interest by simply drawing a polygon on the map
    region = Map.user_roi
    if region is None:
        region = ee.Geometry.BBox(-89.7088, 42.9006, -89.0647, 43.2167)

    Map.centerObject(region)


    # In[ ]:


    # Set the date range
    start_date = '2011-01-01'
    end_date = '2020-12-31'


    # The `return_type` can be `hillshade`, `visualize`, `class`, or `probability`. If you want to use the resulting images for further analysis, you should use `class`.

    # In[ ]:


    images = geemap.dynamic_world_timeseries(
        region, start_date, end_date, return_type="class"
    )


    # In[ ]:


    vis_params = {
        "min": 0,
        "max": 8,
        "palette": [
            "#419BDF",
            "#397D49",
            "#88B053",
            "#7A87C6",
            "#E49635",
            "#DFC35A",
            "#C4281B",
            "#A59B8F",
            "#B39FE1",
        ],
    }
    Map.addLayer(images.first(), vis_params, 'First image')
    Map.add_legend(title="Dynamic World Land Cover", builtin_legend='Dynamic_World')
    Map


    # In[ ]:


    Map.ts_inspector(images, left_vis=vis_params, date_format='YYYY')


    # In[ ]:


    Map = geemap.Map()
    Map.add_basemap('HYBRID')
    Map.centerObject(region)

    images = geemap.dynamic_world_timeseries(
        region, start_date, end_date, return_type="hillshade"
    )
    Map.ts_inspector(images, date_format='YYYY')
    Map.add_legend(title="Dynamic World Land Cover", builtin_legend='Dynamic_World')

    Map


    # ![](https://i.imgur.com/5DGOuTC.png)
    
except Exception as e:
    import streamlit as st
    st.error(f"An error occurred: {e}")
    raise e
