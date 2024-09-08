import pandas as pd
from openpyxl import Workbook
from openpyxl.chart import BarChart, Reference
from openpyxl.utils.dataframe import dataframe_to_rows

def get_sales_by_column(dataframe, col_name, per_unit_price_col, quantity_col, average=False, by_day=False):
    """
    Calculate total or average sales grouped by a specified column.
    
    Parameters:
    dataframe (pd.DataFrame): The input DataFrame containing the sales data.
    col_name (str): The column name by which to group sales data (e.g., 'Country', 'Product', 'Purchase_Date').
    per_unit_price_col (str): The column name for the price per unit.
    quantity_col (str): The column name for the quantity sold.
    average (bool): If True, return the average sales per group; if False, return total sales per group.
    by_day (bool): If True and col_name is 'Purchase_Date', group by day name; otherwise group by month.

    Returns:
    dict: A dictionary where keys are unique values from `col_name` and values are total/average sales.
    """
    total_by_column = {}
    
    # Handle special case when grouping by 'Purchase_Date'
    if col_name == 'Purchase_Date' and not by_day:
        dataframe[col_name] = pd.to_datetime(dataframe[col_name])  # Convert to datetime
        dataframe['Month_Name'] = dataframe[col_name].dt.strftime('%B')  # Extract month name
        unique_data = dataframe['Month_Name'].unique()  # Get unique months
    elif col_name == 'Purchase_Date' and by_day:
        dataframe[col_name] = pd.to_datetime(dataframe[col_name])  # Convert to datetime
        dataframe['Day_Name'] = dataframe[col_name].dt.day_name()  # Extract day name
        unique_data = dataframe['Day_Name'].unique()  # Get unique days
    else:
        unique_data = dataframe[col_name].unique()  # Get unique values from other columns

    # Iterate through unique values and calculate total/average sales
    for data in unique_data:
        if col_name == 'Purchase_Date' and not by_day:
            filtered_df = dataframe[dataframe['Month_Name'] == data]  # Filter by month
        elif col_name == 'Purchase_Date' and by_day:
            filtered_df = dataframe[dataframe['Day_Name'] == data]  # Filter by day
        else:
            filtered_df = dataframe[dataframe[col_name] == data]  # Filter by other columns
        
        # Skip empty DataFrames
        if filtered_df.shape[0] == 0:
            total_by_column[data] = 0
            continue

        # Calculate total sales for the current group
        total_sales = (filtered_df[per_unit_price_col] * filtered_df[quantity_col]).sum()
        
        # Store total or average sales based on the flag
        if not average:
            total_by_column[data] = round(total_sales, 2)  # Total sales
        else:
            total_by_column[data] = round(total_sales / filtered_df.shape[0], 2)  # Average sales per row

    return total_by_column

def generate_sales_report(dataframe, per_unit_price_col, quantity_col):
    """
    Generate an Excel sales report with totals, averages, and charts.

    Parameters:
    dataframe (pd.DataFrame): The input DataFrame containing sales data.
    per_unit_price_col (str): The column name for the price per unit.
    quantity_col (str): The column name for the quantity sold.

    Returns:
    None
    """
    # Initialize an Excel workbook and set the active worksheet
    wb = Workbook()
    ws = wb.active
    ws.title = "Sales Report"

    # Calculate totals and averages for different categories
    # Total and average sales by country
    total_sales_by_country = get_sales_by_column(dataframe, 'Country', per_unit_price_col, quantity_col)
    avg_sales_by_country = get_sales_by_column(dataframe, 'Country', per_unit_price_col, quantity_col, average=True)
    
    # Total and average sales by purchase month
    total_sales_by_month = get_sales_by_column(dataframe, 'Purchase_Date', per_unit_price_col, quantity_col)
    avg_sales_by_month = get_sales_by_column(dataframe, 'Purchase_Date', per_unit_price_col, quantity_col, average=True)
    
    # Total and average sales by day
    total_sales_by_day = get_sales_by_column(dataframe, 'Purchase_Date', per_unit_price_col, quantity_col, by_day=True)
    avg_sales_by_day = get_sales_by_column(dataframe, 'Purchase_Date', per_unit_price_col, quantity_col, average=True, by_day=True)
    
    # Total sales by product
    total_sales_by_product = get_sales_by_column(dataframe, 'Product', per_unit_price_col, quantity_col)
    
    # Total sales by payment method
    total_sales_by_payment = get_sales_by_column(dataframe, 'Payment_Method', per_unit_price_col, quantity_col)
    
    # Write totals and averages to the worksheet
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

    # Add charts to the report for visualization
    # Chart for total sales by country
    add_chart(ws, "Total Sales by Country", start_row=2, category_col=1, value_col=2)
    
    # Chart for total sales by month
    add_chart(ws, "Total Sales by Month", start_row=10, category_col=1, value_col=2)
    
    # Chart for total sales by product
    add_chart(ws, "Total Sales by Product", start_row=18, category_col=1, value_col=2)

    # Save the Excel workbook
    wb.save("sales_report.xlsx")
    print("Report generated and saved as sales_report.xlsx")

def add_chart(worksheet, title, start_row, category_col, value_col):
    """
    Add a bar chart to the worksheet to visualize total sales.

    Parameters:
    worksheet (openpyxl.Worksheet): The worksheet where the chart will be added.
    title (str): The title of the chart.
    start_row (int): The starting row of the data in the worksheet.
    category_col (int): The column number where categories (e.g., country names) are located.
    value_col (int): The column number where the values (e.g., total sales) are located.

    Returns:
    None
    """
    # Create a bar chart object
    chart = BarChart()
    chart.title = title
    chart.x_axis.title = "Category"
    chart.y_axis.title = "Total Sales"
    
    # Define the data and category ranges for the chart
    categories = Reference(worksheet, min_col=category_col, min_row=start_row + 1, max_row=start_row + 5)
    data = Reference(worksheet, min_col=value_col, min_row=start_row, max_row=start_row + 5)

    # Add the data and categories to the chart
    chart.add_data(data, titles_from_data=True)
    chart.set_categories(categories)

    # Insert the chart in the worksheet
    worksheet.add_chart(chart, f"E{start_row + 1}")

if __name__ == '__main__':
    # Load the sales data from a CSV file
    df = pd.read_csv('fake_sales_data.csv')

    # Generate the sales report
    generate_sales_report(df, 'Price_Per_Unit', 'Quantity')
