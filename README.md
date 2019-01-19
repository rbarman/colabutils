# colabutils
```
!git clone https://github.com/rbarman/colabutils
!pip install -r colabutils/requirements.txt
```

```python
from colabutils import colabutils as c
c.download_imgs_from_google('boats',200)
# {'img_count': 200, 'img_dir': 'downloads/boats/', 'keyword': 'boats'}
```
