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

---
Recipes

1) Working with fastai

```python
from colabutils import google as g
from fastai.vision import *

# download images to downloads/bicycle/ and downloads/unicycle/ 
g.download_imgs_from_google('bicycle',100)
g.download_imgs_from_google('unicycle',100)

data = ImageDataBunch.from_folder('downloads',train=".",valid_pct = .2, ds_tfms=get_transforms(), size=224, bs=64).normalize(imagenet_stats)
# now train with data, etc
```