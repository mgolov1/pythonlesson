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