from openpyxl import Workbook
from openpyxl.drawing.image import Image

# Create a new workbook and select the active sheet
wb = Workbook()
sheet = wb.active
sheet.title = "Image Example"

# Add some data
sheet["A1"] = "Here is an image:"

# Load and insert the image
img = Image("logo.jpg")  # Replace with your image path

# Adjust the image size (optional)
img.width = 150  # Set desired width
img.height = 100  # Set desired height

# Add the image to the sheet
sheet.add_image(img, "B2")  # Position the image at cell B2

# Save the workbook
wb.save("image_example.xlsx")
