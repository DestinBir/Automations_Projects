import pandas as pd

# Data to write
data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "City": ["New York", "London", "Paris"]
}
df = pd.DataFrame(data)

# Write to Excel and apply formatting
with pd.ExcelWriter("designed_table.xlsx", engine="xlsxwriter") as writer:
    df.to_excel(writer, index=False, sheet_name="People")
    worksheet = writer.sheets["People"]

    # Apply formatting
    workbook = writer.book
    header_format = workbook.add_format({
        "bold": True,
        "text_wrap": True,
        "valign": "top",
        "fg_color": "#D7E4BC",
        "border": 1
    })

    # Apply header format
    for col_num, value in enumerate(df.columns.values):
        worksheet.write(0, col_num, value, header_format)

    # Set column widths
    worksheet.set_column("A:A", 20)
    worksheet.set_column("B:B", 10)
    worksheet.set_column("C:C", 15)
