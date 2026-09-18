# Data Visualization Toolkit

A modular Python toolkit for loading CSV data and generating clean, professional
visualizations including bar charts, scatter plots, and grouped bar charts.

## Features
- CSV loader with validation
- Multiple graph types (bar, scatter, grouped bar)
- CLI interface for quick usage
- Export graphs as PNG
- Clean, modular architecture

## Usage
pip install -r requirements.txt
python src/main.py

## Example
python src/main.py --file sample_data/sales.csv --graph bar --x Month --y Revenue
