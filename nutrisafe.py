import re
from difflib import SequenceMatcher
from PIL import Image
import pytesseract
import cv2
import numpy as np
import os

pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files (x86)/Tesseract-OCR/tesseract'

def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

def cleantext(text):
	text= re.sub('[*|\n|\|(|)|.]',' ',text)
	text = re.sub('[}|{|\|/|,|:]',' ',text)
	text = re.sub(' +',' ',text)
	ingredients = text.split()  
	return ingredients 

def checksafe(ingredients,wheat):
    for i in range(len(wheat)):
    		 for j in range(len(ingredients)):
        		if similar(wheat[i],ingredients[j]) >= 0.7:
            		    print ("NOT SAFE CONTAINS ALLERGIC INGREDIENTS")
            		    #print (similar(wheat[i],ingredients[j]))
            		    return 0

    return 1       	

def gettext(image):
	img = cv2.imread(image,0)
	kernel = np.ones((1,1),np.uint8)
	th = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)
	big = cv2.resize(th,(0,0),fx=2,fy=2)
	cv2.imwrite("ing.jpg",big)
	text = pytesseract.image_to_string(Image.open(os.path.abspath("ing.jpg")))
	return text


wheat = ['bulgur', 'cereal', 'couscous', 'cracker', 'einkorn', 'flour', 'gluten', 'malt', 
'semolina', 'triticale', 'triticum', 'bran', 'gem', 'wheat','dextrin', 'maltodextrin', 
'monosodium glutamate', 'oats', 'soy']

text = gettext("ingredients.jpg")
#print(text)
#.encode("utf-8")
ingredientslist = cleantext(text)
#print len(ingredientslist)
ingredientslist = [x.lower() for x in ingredientslist]
x=0
for i in range(len(wheat)):
    for j in range(len(ingredientslist)):
    	#print similar(wheat[i],ingredientslist[j])
        if similar(wheat[i],ingredientslist[j]) >= 0.7:
            x=x+1
            #print(wheat[i])
#checksafe(ingredientslist,wheat)
if x>0:
	print("NOT SAFE CONTAINS ALLERGIC INGREDIENTS")
else:
      print("IT IS SAFE DOESN'T CONTAIN ALLERGIC INGREDIENTS")
#print(x)

