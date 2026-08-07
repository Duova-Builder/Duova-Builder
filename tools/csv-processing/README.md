# CSV Inventory Processing

A simple Python utility for processing inventory CSV files.

## Features

- Remove rows where the **Location** contains:
  - fixing
  - reserved
- Calculate the total available inventory for each SKU.
- Keep only SKUs whose total inventory is 50 or greater**.
- Output one record per SKU.

## Input

Input file:

```
input.csv
```

Required columns:

| Column | Description |
|---------|-------------|
| SKU | Product SKU |
| Location | Warehouse location |
| Available | Available inventory |

## Output

Output file:

```
largerThan50.csv
```

Each SKU appears only once, with a total available inventory of at least 50.

## Requirements

- Python 3.10+
- pandas

Install:

```bash
pip install pandas
```

Run:

```bash
python process_inventory.py
```

## Example Workflow

```
input.csv
      ↓
Remove fixing/reserved locations
      ↓
Sum inventory from difference warehouses by SKU
      ↓
Keep TotalStock ≥ 50
      ↓
Remove duplicate SKUs
      ↓
largerThan50.csv
```