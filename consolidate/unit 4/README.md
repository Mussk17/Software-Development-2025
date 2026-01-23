# Unit 4: Inventory Management System

A Python program for variable exploration that demonstrates different data types and file handling for data persistence.

## What It Does

- Stores product names (strings), quantities (integers), and prices (floats) in a dictionary
- Updates and displays inventory information
- Saves data to CSV and text files for persistence
- Loads data from files when the program starts

## Requirements

- Python 3.11.9

## How to Run

```bash
python inventory_manager.py
```

## Data Types Used

- **Strings**: Product names (e.g., `"Laptop"`)
- **Integers**: Quantities (e.g., `15`)
- **Floats**: Prices (e.g., `899.99`)
- **Dictionary**: Organizes all product data together

## Key Functions

- `display_inventory()` - Shows all products with quantities, prices, and total inventory value
- `add_product(name, quantity, price)` - Adds a new product or updates quantity if product exists
- `update_qty(name, new_qty)` - Changes the quantity of an existing product
- `update_price(name, new_price)` - Changes the price of an existing product
- `remove_product(name)` - Removes a product from inventory
- `save_to_file()` - Saves inventory to CSV file (`inventory.csv`)
- `load_from_file()` - Loads inventory from CSV file (returns True/False)
- `save_to_text()` - Saves inventory to human-readable text file (`inventory.txt`)
- `main()` - Main program function that runs the inventory management workflow

## Files Created

- `inventory.csv` - CSV format (can open in Excel)
- `inventory.txt` - Human-readable text format
