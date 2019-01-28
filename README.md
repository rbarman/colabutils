# colabutils
```
!git clone https://github.com/rbarman/colabutils
!pip install -r colabutils/requirements.txt
```

1) Download opencv compatible images from google. This is a simple way to get images for a computer vision project.

```python
from colabutils import google as g
g.download_imgs_from_google('boats',200)
# {'img_count': 200, 'img_dir': 'downloads/boats/', 'keyword': 'boats'}
```

2) Download images with ImageNet style directories. 

- This is useful if you want train models with fastai. ```ImageDataBunch.from_folder()``` requires images to be in this directory structure

```python
from colabutils import google as g
from fastai.vision import *

'''
downloads/
	bicycle/
	scooter/
'''
g.download_imgs_from_google('bicycle',100)
g.download_imgs_from_google('scooter',100)

'''
data/
	train/
		bicycle/
		scooter/
	valid/
		bicycle/
		scooter/
	test
'''
g.create_imagenet_style_dirs()
data = ImageDataBunch.from_folder('data/',ds_tfms=get_transforms(), size=224, bs=64).normalize(imagenet_stats)
# etc
```