network_devices = ['router_01', 192.168, 'active']
print(len(network_devices))
print(network_devices[0])
print(network_devices[:-1])
additional_devices = ['switch_01', 'firewall_02']
complete_network = network_devices + additional_devices
print(complete_network)

inventory = [1001, 'Laptop', 899.99]
inventory.append('In Stock')
print(inventory)
inventory.pop(2)
print(inventory)

support_tickets = ['Ticket_B', 'Ticket_A', 'Ticket_C']
support_tickets.sort()
print(support_tickets)
support_tickets.reverse()
print(support_tickets)

laptop_inventory = ["HP-2021-001", "Dell-2022-002", "Lenovo-2023-003"]
tablet_inventory = ["iPad-2023-001", "Surface-2023-002"]
laptop_inventory.append("Macbook-2024-004")

primary_inventory = ["HP-2021-001", "Dell-2022-002", "Lenovo-2023-003"]
acquired_inventory = ["HP-2023-701", "Dell-2023-892"]
primary_inventory.extend(acquired_inventory)

laptop_inventory.insert(1, "DevServer-2025-001")
laptop_inventory.remove("HP-2021-001")
transferred_device = laptop_inventory.pop()
print(laptop_inventory)
print(transferred_device)

acquired_inventory.clear()
print(acquired_inventory)

laptop_inventory.sort()
laptop_inventory.reverse()
server_position = laptop_inventory.index("DevServer-2025-001")
hp_count = laptop_inventory.count("Dell-2022-002")
print(hp_count)

complete_inventory = laptop_inventory + tablet_inventory
branch_setups = tablet_inventory * 3
total_tablet_inventory = len(tablet_inventory + branch_setups)
print(total_tablet_inventory)

employees = [
    ["Alice", "IT", 75000],
    ["Bob", "HR", 65000],
    ["Carol", "IT", 78000]
]

it_salaries = [emp[2] for emp in employees if emp[1] == "IT"]
print(it_salaries)

average_it_salary = sum(it_salaries) / len(it_salaries)
print(f"Average IT Salary: ${average_it_salary}")

departments = set ([emp[1] for emp in employees])
print(departments)

employee_data = [
    [1001, 50000, 'HR', 'Active'],
    [1002, 60000, 'IT', 'Active'],
    [1004, 65000, 'IT', 'Active']
]

adjusted_salaries = [employee[1] + 5000 for employee in employee_data]
print(adjusted_salaries)
it_department = [employee[1] for employee in employee_data]
print(it_department)
active_employee_ids = [employee[0] for employee in employee_data if employee[3] == 'Active']
print(active_employee_ids)
department_codes = [employee[2] for employee in employee_data]
formatted_codes = [code.lower() for code in department_codes]
print(formatted_codes)
high_salary_employees = [employee for employee in employee_data if employee[1] > 55000]
print(high_salary_employees)

sales_data = [
    [100, 150, 200], # Product A daily sales
    [300, 350, 400], # Product B daily sales
    [500, 550, 600] # Product C daily sales
]

daily_totals = (sum(day) for day in sales_data)
print(f"Day 1 total sales: ${next(daily_totals)}")
print(f"Day 2 total sales: ${next(daily_totals)}")
print(f"Day 3 total sales: ${next(daily_totals)}")

product_totals = list(map(sum, sales_data))
print(product_totals)

# {sale for product in sales_data for sale in product}

unique_sales = set()
for product in sales_data:
    for sale in product:
        unique_sales.add(sale)
print("Unique sales value:", sorted (unique_sales, reverse=True))
daily_increases = [day2 - day1 for day1, day2 in zip(sales_data[0][:-1], sales_data[0][1:])]
print(daily_increases)
for increase in daily_increases:
    print(f"Increase: ${increase}")