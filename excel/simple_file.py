from openpyxl import Workbook

# Create a new workbook
wb = Workbook()
sheet = wb.active
sheet.title = "Page 1"

# Write data to the sheet
sheet["A1"] = "Name"
sheet["B1"] = "Age"
sheet["A2"] = "John"
sheet["B2"] = 30
sheet["A3"] = "Destin"
sheet["B3"] = 25
sheet["A4"] = "Delphin"
sheet["B4"] = 23

# Save the workbook
wb.save("example.xlsx")
