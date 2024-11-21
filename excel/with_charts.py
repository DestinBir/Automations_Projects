from openpyxl.chart import BarChart, Reference
from openpyxl import Workbook

# Create a new workbook
wb = Workbook()
sheet = wb.active
sheet.title = "Page 1"

# Data for the chart
sheet["A4"] = "Category"
sheet["B4"] = "Values"
sheet["A5"] = "A"
sheet["B5"] = 10
sheet["A6"] = "B"
sheet["B6"] = 40
sheet["A7"] = "C"
sheet["B7"] = 30

# Create a bar chart
chart = BarChart()
data = Reference(sheet, min_col=2, min_row=4, max_row=7)
categories = Reference(sheet, min_col=1, min_row=5, max_row=7)
chart.add_data(data, titles_from_data=True)
chart.set_categories(categories)
chart.title = "Sample Chart"

# Add the chart to the sheet
sheet.add_chart(chart, "D4")

wb.save("chart_example.xlsx")
