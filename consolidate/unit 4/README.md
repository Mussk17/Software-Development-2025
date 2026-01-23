# Unit 4: Variable Exploration and Data Persistence

# Inventory Management System

A Python program for variable exploration that demonstrates different data types, file handling for data persistence, and interactive programming with while loops and match-case statements.

## What It Does

- Stores product names (strings), quantities (integers), and prices (floats) in a dictionary
- Interactive menu system for managing inventory
- Saves data to CSV and text files for persistence
- Loads data from files when the program starts

## Requirements

- Python 3.10+ (required for match-case statements)

## How to Run

```bash
python inventory_manager.py
```

The program will display an interactive menu where you can:
1. Add or update products
2. View current inventory
3. Exit and save inventory

## Data Types Used

- **Strings**: Product names (e.g., `"Laptop"`)
- **Integers**: Quantities (e.g., `15`)
- **Floats**: Prices (e.g., `899.99`)
- **Dictionary**: Organizes all product data together

## Key Functions

- `display_inventory()` - Shows all products with quantities, prices, and total inventory value
- `add_product(name, quantity, price)` - Adds a new product or updates quantity if product exists
- `add_or_update_product()` - Interactive function to get user input and add/update products
- `save_to_file()` - Saves inventory to CSV file (`inventory.csv`)
- `load_from_file()` - Loads inventory from CSV file (returns True/False)
- `save_to_text()` - Saves inventory to human-readable text file (`inventory.txt`)
- `main()` - Main program with interactive menu using while loop and match-case

## Features Demonstrated

- Variable declaration and assignment
- Different data types (str, int, float, dict)
- While loops for menu repetition
- Match-case statements for choice handling (Python 3.10+)
- File handling for data persistence
- Error handling with try-except blocks

## Files Created

- `inventory.csv` - CSV format (can open in Excel)
- `inventory.txt` - Human-readable text format
