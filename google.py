from google_images_download import google_images_download
import cv2
import glob
from selenium import webdriver
import sys
import os
import numpy as np
import random

def collab_setup():

	'''
	Set up chrome to work in google colab
	  https://stackoverflow.com/questions/53532060/webdriverexception-message-service-content-chromedriver-unexpectedly-exited
	Chrome driver is required if we want to download over 100 google images  
	'''

		# install all relevant packages if chrome driver is not installed
	if not os.path.isfile('/usr/lib/chromium-browser/chromedriver'):
	    
		# !<> is invalid in raw python
		#!apt install chromium-chromedriver
		#!cp /usr/lib/chromium-browser/chromedriver /usr/bin
		os.system('apt install chromium-chromedriver')
		os.system('cp /usr/lib/chromium-browser/chromedriver /usr/bin')
		sys.path.insert(0,'/usr/lib/chromium-browser/chromedriver')  

		chrome_options = webdriver.ChromeOptions()
		chrome_options.add_argument('--headless')
		chrome_options.add_argument('--no-sandbox')
		chrome_options.add_argument('--disable-dev-shm-usage')
		wd = webdriver.Chrome('chromedriver',chrome_options=chrome_options)

def download_imgs_from_google(keyword,num):

	'''
		Downloads cv2 compatible images to /downloads/keyword
		Returns dictionary with keyword and total number of images
	'''

	collab_setup()

	# download images from google images to /downloads/keyword
	response = google_images_download.googleimagesdownload()
	arguments = {"keywords":keyword,"limit":num,"extract_metadata":True,"chromedriver":'/usr/lib/chromium-browser/chromedriver'} 
	paths = response.download(arguments)   
	img_dir =  f'downloads/{keyword}/'

	# get paths to all downloaded images
	img_paths = glob.glob(f'{img_dir}*')

	# delete images that are not compatible with cv2
	for img_path in img_paths:
	  img = cv2.imread(img_path)
	  if img is None:
	      os.remove(img_path)
	      
	img_count = len(glob.glob(f'{img_dir}*'))
	return {
	    'keyword':keyword
	    ,'img_count':img_count
	    ,'img_dir':img_dir
	}

def create_imagenet_style_dirs():

	'''
		Create image net style directories for all images in downloads/.
		- data/train/<class> for each class
		- data/valid/<class> for each class
		- data/test
		All possible classs are defined by downloads/<class> 
		Images per each class are split 60/20/20 to train/valid/test
	'''
	os.system(f'mkdir data/train')
	os.system(f'mkdir data/valid')
	os.system(f'mkdir data/test')

	classes = [os.path.basename(x) for x in glob.glob('downloads/*')];
	for c in classes:
		# get image paths for a class and split 60/20/20 into train/valid/test
		c_paths = [path for path in glob.glob(f'downloads/{c}/*')];
		random.shuffle(c_paths)
		train,valid,test = np.split(c_paths, [int(.6*len(c_paths)), int(.8*len(c_paths))])

		# create class subfolders and move images over
		os.system(f'mkdir data/train/"{c}"')
		os.system(f'mkdir data/valid/"{c}"')

		_ = [os.system(f'mv "{path}" data/train/"{c}"') for path in train]
		_ = [os.system(f'mv "{path}" data/valid/"{c}"') for path in valid]
		_ = [os.system(f'mv "{path}" data/test/') for path in test]
