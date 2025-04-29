import random
import csv

# Step 1: Generate a list of 400 workers dynamically
num_workers = 400
workers = []

for i in range(num_workers):
    worker = {
        "id": i + 1,
        "name": f"Worker_{i+1}",
        "gender": random.choice(["Male", "Female"]),
        "salary": random.randint(5000, 35000)
    }
    workers.append(worker)

# Step 2: Generate payment slips and apply conditional statements
payment_slips = []

for worker in workers:
    try:
        employee_level = "B2"  # Default level
        
        if 10000 < worker["salary"] < 20000:
            employee_level = "A1"
        elif 7500 < worker["salary"] < 30000 and worker["gender"] == "Female":
            employee_level = "A5-F"
        
        # Create payment slip
        slip = {
            "ID": worker["id"],
            "Name": worker["name"],
            "Gender": worker["gender"],
            "Salary": worker["salary"],
            "Employee Level": employee_level
        }
        payment_slips.append(slip)
    except Exception as e:
        print(f"Error processing worker {worker['id']}: {e}")

# Step 3: Save payment slips to a CSV file
with open("payment_slips.csv", "w", newline="") as file:
    fieldnames = ["ID", "Name", "Gender", "Salary", "Employee Level"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(payment_slips)

print("Payment slips generated successfully!")

