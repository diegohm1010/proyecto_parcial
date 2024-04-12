
import os

location = "C:/Users/Diego Hernandez/OneDrive - GFI/Documents/diego/CERTUS/proyecto_parcial/python/dataset"

###Validar que la carpeta exista###
if not os.path.exists(location):
    ##En caso mi carpeta no exista, voy a crear una nueva##
    os.mkdir(location) ##mkdir -> make directory
else:
    ##Si la carpeta ya existe, entonces borramos el contenido##
    for root, dirs, files in os.walk(location, topdown=False):
        for name in files:
            os.remove(os.path.join(root,name)) ##elimino todos los archivos
        for name in dirs:
            os.rmdir(os.path.join(root,name)) ##rmdir -> remove directory / elimino todas mis carpetas


from kaggle.api.kaggle_api_extended import KaggleApi
###Iniciamos sesion con nuestra cuenta de kaggle####
api=KaggleApi()
api.authenticate()

##print(api.dataset_list(search='henryshan'))###
##print(api.dataset_list())

api.dataset_download_file('jatinthakur706/most-watched-netflix-original-shows-tv-time','imdb.csv',path='dataset',quiet=False)
api.dataset_download_file('henryshan/starbucks','starbucks.csv',path='dataset',quiet=False)
print("se descargo archivo")