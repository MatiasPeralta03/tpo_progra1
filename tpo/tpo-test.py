import csv
import json
import os

class SalesDataPlatform:
    def __init__(self):
        self.sales_data = []

    def load_csv(self, filepath):
        try:
            with open(filepath, mode='r') as file:
                reader = csv.DictReader(file)
                self.sales_data.extend([row for row in reader])
        except Exception as e:
            print(f"Error loading CSV file: {e}")

    def load_json(self, filepath):
        try:
            with open(filepath, mode='r') as file:
                data = json.load(file)
                self.sales_data.extend(data if isinstance(data, list) else [data])
        except Exception as e:
            print(f"Error loading JSON file: {e}")

    def analyze_sales(self):
        # Implement your analysis using lists, dictionaries, etc.
        total_sales = sum(float(record.get('sales_amount', 0)) for record in self.sales_data)
        print(f"Total Sales: {total_sales}")
        # Add more complex analysis here

    def recursive_calculation(self, data, depth=0):
        # Example of a recursive calculation
        if depth == len(data):
            return 0
        return float(data[depth].get('sales_amount', 0)) + self.recursive_calculation(data, depth + 1)

    def generate_report(self):
        # Generate a report from the sales data
        # Example: print the total sales
        print("Sales Report")
        self.analyze_sales()

    def run(self):
        # Main execution method
        csv_files = [file for file in os.listdir() if file.endswith('.csv')]
        json_files = [file for file in os.listdir() if file.endswith('.json')]

        for csv_file in csv_files:
            self.load_csv(csv_file)

        for json_file in json_files:
            self.load_json(json_file)

        self.generate_report()

if __name__ == "__main__":
    platform = SalesDataPlatform()
    platform.run()
