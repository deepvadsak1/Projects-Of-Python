import cv2
import pytesseract
import pandas as pd
import os

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def extract_data_from_image(image_path, region):
    image = cv2.imread(image_path)
    x, y, w, h = region
    roi = image[y:y + h, x:x + w]
    gray_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
    extracted_text = pytesseract.image_to_string(gray_roi)
    return extracted_text

def save_to_excel(names, locations, times, reviews, output_file):
    new_data = pd.DataFrame({
        "Name": names,
        "Location": locations,
        "Time": times,
        "Review": reviews
    })

    if not os.path.exists(output_file):
        new_data.to_excel(output_file, index=False)
    else:
        existing_df = pd.read_excel(output_file)
        updated_df = pd.concat([existing_df, new_data], ignore_index=True)
        updated_df.to_excel(output_file, index=False)

output_excel_file = 'output_data.xlsx'

# Define the regions for each image
image_regions = [
    {'name': (180, 670, 2532, 70), 'location': (250, 740, 2532, 70), 'time': (280, 830, 2532, 70), 'review': (1, 910, 2532, 150)},
    {'name': (185, 700, 2532, 65), 'location': (185, 765, 2532, 70), 'time': (290, 855, 2532, 70), 'review': (1, 920, 2532, 100)},
    {'name': (190, 720, 2532, 65), 'location': (250, 770, 2532, 70), 'time': (290, 865, 2532, 70), 'review': (1, 945, 2532, 150)},
    {'name': (185, 770, 2532, 65), 'location': (250, 835, 2532, 70), 'time': (285, 925, 2532, 70), 'review': (1, 1005, 2532, 100)},
    {'name': (180, 1020, 2532, 65), 'location': (250, 1085, 2532, 70), 'time': (290, 1185, 2532, 50), 'review': (1, 1255, 2532, 100)}
    
    
]

# Process each image
for i, image_path in enumerate([r'C:\PYTHON CODES\img_data_in_excel\img\img1.png',
                                r'C:\PYTHON CODES\img_data_in_excel\img\img2.png',
                                r'C:\PYTHON CODES\img_data_in_excel\img\img3.png',
                                r'C:\PYTHON CODES\img_data_in_excel\img\img4.png',
                                r'C:\PYTHON CODES\img_data_in_excel\img\img5.png']):
    name_region = image_regions[i]['name']
    location_region = image_regions[i]['location']
    time_region = image_regions[i]['time']
    review_region = image_regions[i]['review']

    extracted_data_name = extract_data_from_image(image_path, name_region)
    extracted_data_location = extract_data_from_image(image_path, location_region)
    extracted_data_time = extract_data_from_image(image_path, time_region)
    extracted_data_review = extract_data_from_image(image_path, review_region)

    save_to_excel([extracted_data_name], [extracted_data_location], [extracted_data_time], [extracted_data_review], output_excel_file)

print(f"Data extraction completed. Results saved to {output_excel_file}.")
