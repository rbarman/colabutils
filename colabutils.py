from google_images_download import google_images_download
import cv2
import glob
from selenium import webdriver
import sys
import os

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
		os.system('/usr/lib/chromium-browser/chromedriver /usr/bin')
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
	      os.remove(path)
	      
	img_count = len(glob.glob(f'{img_dir}*'))
	return {
	    'keyword':keyword
	    ,'img_count':img_count
	}

# download_imgs_from_google('boats',200)    