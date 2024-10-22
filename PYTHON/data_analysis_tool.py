import pandas as pd
import mysql.connector
import matplotlib.pyplot as plt

# Step 1: Connect to the MySQL database
def connect_to_db():
    return mysql.connector.connect(
        host='localhost',  # Change if your MySQL server is on a different host
        user='root',  # Replace with your MySQL username
        password='mysql',  # Replace with your MySQL password
        database='retail_store'
    )

# Step 2: Fetch data from the 'sales_data' table
def fetch_sales_data(connection):
    query = "SELECT * FROM sales_data"
    return pd.read_sql(query, connection)

# Step 3: Analyze Sales Data
def analyze_data(df):
    # Group by product name to get total sales and quantities
    sales_summary = df.groupby('product_name').agg({
        'quantity_sold': 'sum',
        'sale_amount': 'sum'
    }).reset_index()
    return sales_summary

# Step 4: Visualize Sales Trends
def visualize_sales(sales_summary):
    # Plot total sales amount per product
    plt.figure(figsize=(10, 6))
    plt.bar(sales_summary['product_name'], sales_summary['sale_amount'], color='skyblue')
    plt.title('Total Sales Amount per Product')
    plt.xlabel('Product Name')
    plt.ylabel('Total Sale Amount')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

    # Plot total quantity sold per product
    plt.figure(figsize=(10, 6))
    plt.bar(sales_summary['product_name'], sales_summary['quantity_sold'], color='lightgreen')
    plt.title('Total Quantity Sold per Product')
    plt.xlabel('Product Name')
    plt.ylabel('Total Quantity Sold')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# Main Function
def main():
    # Connect to the database
    connection = connect_to_db()

    # Fetch sales data
    df = fetch_sales_data(connection)

    # Analyze the data
    sales_summary = analyze_data(df)

    # Visualize the results
    visualize_sales(sales_summary)

    # Close the database connection
    connection.close()

if __name__ == "__main__":
    main()
