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