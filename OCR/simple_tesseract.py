import pytesseract
from PIL import Image

image=Image.open("book_page_6.png")

# custom_oem_psm_config = r'--oem 3 --psm 6'

# result = pytesseract.image_to_string(image, lang="snum", config=custom_oem_psm_config) # number
# result = pytesseract.image_to_string(image, lang="eng", config=custom_oem_psm_config) # english
result = pytesseract.image_to_string(image, lang="chi_sim", config=custom_oem_psm_config) # chinese simplified
print(result)
