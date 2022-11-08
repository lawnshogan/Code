
'''
Config items:
   -AGOL folder id : use your own folder (i don’t think we can share folders) 
   -AGOL group id for sharing : 34e8414eaedc4e3d93b3e861280e7a82
   -List of feature layer urls: 
      -https://services1.arcgis.com/qkYTKlfKEB2WYL01/ArcGIS/rest/services/FMPro_Final_Loaded/FeatureServer/1
      -https://services1.arcgis.com/qkYTKlfKEB2WYL01/ArcGIS/rest/services/FMPro_Final_Loaded/FeatureServer/3  

Using the ArcGIS API for Python
For each feature layer in config list
   -call the ExtractData tool to Shapefile (should create a zip file)
   -upload extracted shapefile zip to the folder 
   -overwrite existing or delete if already exists
   -share zip file with group id from config 
'''

########################################

print("importing modules...")
import arcgis
from arcgis import GIS
from getpass import getpass
print("\tmodules imported.")

########################################

# Place these into a config file?
url = 'https://arcgis.com'
username = 'martinwi'
password = getpass()

itemURLs = ['https://services5.arcgis.com/rqsYvPKZmvSrSWbw/ArcGIS/rest/services/SLB_Surface_Ownership/FeatureServer/0']

groupID = '94bd8c89cc624bcd8ceac6c515f72973'

### Thumbnail variable can be a path or URL to thumbnail image ###
thumbnail = 'https://upload.wikimedia.org/wikipedia/commons/thumb/4/46/Flag_of_Colorado.svg/255px-Flag_of_Colorado.svg.png'

########################################

gis = GIS(url=url, username=username, password=password)

features = []
updatedURLs = []

def ServiceURLtoShapefile():

    #grab specific feature servers to search for
    #update urls with lowercase 'ArcGIS' section, AGOL content urls return lowercase
    for url in itemURLs:
        split = url.split('/')
        feature = split[7]
        if feature not in features:
            features.append(feature)
        split[4] = split[4].lower()
        join = '/'.join(split)
        updatedURLs.append(join)

    #publish shapefile for each service url, share to group
    for f in features:
        content = gis.content.search(f,'Feature Layer')
        for item in content:
            print(item)
            for layer in item.layers:
                if layer.url in updatedURLs:
                    print('   '+str(layer))
                    name = layer.properties.name

                    x = []
                    x.append(name)

                    exists = gis.content.search(name,'ShapeFile')
                    for c in exists:
                        if name == c.title:
                            x.remove(name)
                            c.delete()
                            shp = arcgis.features.manage_data.extract_data([layer],data_format='ShapeFile',output_name=name)
                            shp.share(groups=groupID)
                            shp.update(thumbnail=thumbnail)
                            print('      {} REPLACED'.format(name))
                    for i in x:
                        if name == i:
                            shp = arcgis.features.manage_data.extract_data([layer],data_format='ShapeFile',output_name=name)
                            shp.share(groups=groupID)
                            shp.update(thumbnail=thumbnail)
                            print('      {} ADDED'.format(name))
                        
########################################

if __name__ == '__main__':
    ServiceURLtoShapefile()

########################################