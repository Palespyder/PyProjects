import pandas as pd
from openpyxl import Workbook
from openpyxl.chart import BarChart, Reference
from openpyxl.utils.dataframe import dataframe_to_rows

def get_sales_by_column(dataframe, col_name, per_unit_price_col, quantity_col, average=False, by_day=False):
    total_by_column = {}
    if col_name == 'Purchase_Date' and not by_day:
        dataframe[col_name] = pd.to_datetime(dataframe[col_name])
        dataframe['Month_Name'] = dataframe[col_name].dt.strftime('%B')
        unique_data = dataframe['Month_Name'].unique()
    elif col_name == 'Purchase_Date' and by_day:
        dataframe[col_name] = pd.to_datetime(dataframe[col_name])
        dataframe['Day_Name'] = dataframe[col_name].dt.day_name()
        unique_data = dataframe['Day_Name'].unique()
    else:
        unique_data = dataframe[col_name].unique()

    for data in unique_data:
        if col_name == 'Purchase_Date' and not by_day:
            filtered_df = dataframe[dataframe['Month_Name'] == data]
        elif col_name == 'Purchase_Date' and by_day:
            filtered_df = dataframe[dataframe['Day_Name'] == data]
        else:
            filtered_df = dataframe[dataframe[col_name] == data]
        
        if filtered_df.shape[0] == 0:
            total_by_column[data] = 0
            continue

        # Calculate total sales
        total_sales = (filtered_df[per_unit_price_col] * filtered_df[quantity_col]).sum()
        
         # Store total or average sales based on the flag
        if not average:
            total_by_column[data] = round(total_sales, 2)  # Total sales
        else:
            total_by_column[data] = round(total_sales / filtered_df.shape[0], 2)  # Average sales per row

    return total_by_column

# Function to generate report using openpyxl
def generate_sales_report(dataframe, per_unit_price_col, quantity_col):
    # Initialize the workbook
    wb = Workbook()
    ws = wb.active
    ws.title = "Sales Report"

    # Textual Data: Totals and Averages by different columns
    # Total Sales by Country
    total_sales_by_country = get_sales_by_column(dataframe, 'Country', per_unit_price_col, quantity_col)
    avg_sales_by_country = get_sales_by_column(dataframe, 'Country', per_unit_price_col, quantity_col, average=True)
    
    # Total Sales by Purchase Date Month
    total_sales_by_month = get_sales_by_column(dataframe, 'Purchase_Date', per_unit_price_col, quantity_col)
    avg_sales_by_month = get_sales_by_column(dataframe, 'Purchase_Date', per_unit_price_col, quantity_col, average=True)
    
    # Total Sales by Purchase Date by Day
    total_sales_by_day = get_sales_by_column(dataframe, 'Purchase_Date', per_unit_price_col, quantity_col, by_day=True)
    avg_sales_by_day = get_sales_by_column(dataframe, 'Purchase_Date', per_unit_price_col, quantity_col, average=True, by_day=True)
    
    # Total Sales by Product
    total_sales_by_product = get_sales_by_column(dataframe, 'Product', per_unit_price_col, quantity_col)
    
    # Total Sales by Payment Method
    total_sales_by_payment = get_sales_by_column(dataframe, 'Payment_Method', per_unit_price_col, quantity_col)
    
    # Write textual data (totals and averages)
    ws.append(["Category", "Total Sales", "Average Sales"])
    ws.append(["Total Sales by Country"])
    for country, total in total_sales_by_country.items():
        ws.append([country, total, avg_sales_by_country[country]])

    ws.append(["Total Sales by Month"])
    for month, total in total_sales_by_month.items():
        ws.append([month, total, avg_sales_by_month[month]])

    ws.append(["Total Sales by Day"])
    for day, total in total_sales_by_day.items():
        ws.append([day, total, avg_sales_by_day[day]])

    ws.append(["Total Sales by Product"])
    for product, total in total_sales_by_product.items():
        ws.append([product, total])

    ws.append(["Total Sales by Payment Method"])
    for payment, total in total_sales_by_payment.items():
        ws.append([payment, total])

    # Add charts to visualize the data
    # Chart for Total Sales by Country
    add_chart(ws, "Total Sales by Country", start_row=2, category_col=1, value_col=2)
    
    # Chart for Total Sales by Month
    add_chart(ws, "Total Sales by Month", start_row=10, category_col=1, value_col=2)
    
    # Chart for Total Sales by Product
    add_chart(ws, "Total Sales by Product", start_row=18, category_col=1, value_col=2)

    # Save the workbook
    wb.save("sales_report.xlsx")
    print("Report generated and saved as sales_report.xlsx")


# Helper function to add charts
def add_chart(worksheet, title, start_row, category_col, value_col):
    chart = BarChart()
    chart.title = title
    chart.x_axis.title = "Category"
    chart.y_axis.title = "Total Sales"
    
    # Define the categories and data ranges for the chart
    categories = Reference(worksheet, min_col=category_col, min_row=start_row + 1, max_row=start_row + 5)
    data = Reference(worksheet, min_col=value_col, min_row=start_row, max_row=start_row + 5)

    # Add data and categories to the chart
    chart.add_data(data, titles_from_data=True)
    chart.set_categories(categories)

    # Place the chart below the table
    worksheet.add_chart(chart, f"E{start_row + 1}")


if __name__ == '__main__':
    df = pd.read_csv('fake_sales_data.csv')
    generate_sales_report(df, 'Price_Per_Unit', 'Quantity')
