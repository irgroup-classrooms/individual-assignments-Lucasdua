import re
from collections import Counter

def analyze_orders():
    # Open and read the data from the CSV file containing order details
    with open('./csv/orders.csv', 'r') as file:
        data = file.read()

    # Extract all order identifiers using a regular expression
    order_ids = re.findall(r'Order #(\d+)', data)
    print(f"List of Order IDs: {order_ids}")

    # Extract product names listed in the orders
    item_names = re.findall(r'Product: (\w+)', data)
    print(f"Extracted Product Names: {item_names}")

    # Extract the prices for each product
    item_prices = re.findall(r'Price: \$(\d+\.\d{2})', data)
    print(f"Product Prices: {item_prices}")

    # Retrieve all the dates associated with orders
    order_dates = re.findall(r'Date: (\d{4}-\d{2}-\d{2})', data)
    print(f"Original Order Dates: {order_dates}")

    # Filter products costing more than $500
    high_value_items = [item for item, price in zip(item_names, item_prices) if float(price) > 500]
    print(f"High-Value Products (above $500): {high_value_items}")

    # Reformat the dates from YYYY-MM-DD to DD/MM/YYYY
    reformatted_dates = [re.sub(r'(\d{4})-(\d{2})-(\d{2})', r'\3/\2/\1', date) for date in order_dates]
    print(f"Reformatted Dates (DD/MM/YYYY): {reformatted_dates}")

    # Identify product names with more than six characters
    lengthy_product_names = [name for name in item_names if len(name) > 6]
    print(f"Products with Names Longer than 6 Characters: {lengthy_product_names}")

    # Count how often each product appears in the dataset
    product_frequencies = Counter(item_names)
    print(f"Frequency of Each Product: {product_frequencies}")

    # Identify products priced ending in .99
    discounted_items = [item for item, price in zip(item_names, item_prices) if price.endswith('.99')]
    print(f"Products Priced Ending in .99: {discounted_items}")

    # Determine the product with the lowest price
    lowest_price = min(item_prices, key=lambda x: float(x))
    least_expensive_item = item_names[item_prices.index(lowest_price)]
    print(f"Cheapest Product: {least_expensive_item} at ${lowest_price}")

if __name__ == '__main__':
    analyze_orders()
