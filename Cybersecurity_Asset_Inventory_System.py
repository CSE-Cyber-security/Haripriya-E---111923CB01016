# ==========================================
# CYBERSECURITY ASSET INVENTORY SYSTEM
# Week - 1 Mini Project
# ==========================================

assets = []


# ------------------------------------------
# VALID VALUES
# ------------------------------------------

ASSET_TYPES = [
    "Workstation",
    "Server",
    "Router",
    "Switch",
    "Application"
]

RISK_LEVELS = [
    "Low",
    "Medium",
    "High",
    "Critical"
]

SECURITY_STATUSES = [
    "Secure",
    "Warning",
    "Vulnerable"
]


# ------------------------------------------
# ADD ASSET
# ------------------------------------------

def add_asset():
    print("\n========== ADD ASSET ==========")

    asset_id = input("Asset ID: ").strip()

    # Check duplicate Asset ID
    for asset in assets:
        if asset["id"] == asset_id:
            print("Error: Asset ID already exists.")
            return

    asset_name = input("Asset Name: ").strip()

    # Asset Type
    print("\nAsset Types:")
    for i, asset_type in enumerate(ASSET_TYPES, 1):
        print(f"{i}. {asset_type}")

    while True:
        try:
            choice = int(input("Select Asset Type: "))
            if 1 <= choice <= len(ASSET_TYPES):
                asset_type = ASSET_TYPES[choice - 1]
                break
            else:
                print("Invalid choice.")
        except ValueError:
            print("Please enter a number.")

    ip_address = input("IP Address: ").strip()
    operating_system = input("Operating System: ").strip()
    department = input("Owner/Department: ").strip()

    # Risk Level
    print("\nRisk Levels:")
    for i, risk in enumerate(RISK_LEVELS, 1):
        print(f"{i}. {risk}")

    while True:
        try:
            choice = int(input("Select Risk Level: "))
            if 1 <= choice <= len(RISK_LEVELS):
                risk_level = RISK_LEVELS[choice - 1]
                break
            else:
                print("Invalid choice.")
        except ValueError:
            print("Please enter a number.")

    # Security Status
    print("\nSecurity Status:")
    for i, status in enumerate(SECURITY_STATUSES, 1):
        print(f"{i}. {status}")

    while True:
        try:
            choice = int(input("Select Security Status: "))
            if 1 <= choice <= len(SECURITY_STATUSES):
                security_status = SECURITY_STATUSES[choice - 1]
                break
            else:
                print("Invalid choice.")
        except ValueError:
            print("Please enter a number.")

    asset = {
        "id": asset_id,
        "name": asset_name,
        "type": asset_type,
        "ip": ip_address,
        "os": operating_system,
        "department": department,
        "risk": risk_level,
        "status": security_status
    }

    assets.append(asset)

    print("\nAsset added successfully!")


# ------------------------------------------
# DISPLAY ASSETS
# ------------------------------------------

def display_assets():
    print("\n=========================================")
    print("       CYBERSECURITY ASSET INVENTORY")
    print("=========================================")

    if len(assets) == 0:
        print("No assets available.")
        return

    for asset in assets:
        print(f"\nAsset ID       : {asset['id']}")
        print(f"Asset Name     : {asset['name']}")
        print(f"Asset Type     : {asset['type']}")
        print(f"IP Address     : {asset['ip']}")
        print(f"Operating Sys. : {asset['os']}")
        print(f"Department     : {asset['department']}")
        print(f"Risk Level     : {asset['risk']}")
        print(f"Security Status: {asset['status']}")
        print("-----------------------------------------")


# ------------------------------------------
# SEARCH ASSET
# ------------------------------------------

def search_asset():
    print("\n========== SEARCH ASSET ==========")

    asset_id = input("Enter Asset ID to search: ").strip()

    for asset in assets:
        if asset["id"] == asset_id:
            print("\nAsset Found!")
            print(f"Asset ID       : {asset['id']}")
            print(f"Asset Name     : {asset['name']}")
            print(f"Asset Type     : {asset['type']}")
            print(f"IP Address     : {asset['ip']}")
            print(f"Operating Sys. : {asset['os']}")
            print(f"Department     : {asset['department']}")
            print(f"Risk Level     : {asset['risk']}")
            print(f"Security Status: {asset['status']}")
            return

    print("Asset not found.")


# ------------------------------------------
# UPDATE ASSET
# ------------------------------------------

def update_asset():
    print("\n========== UPDATE ASSET ==========")

    asset_id = input("Enter Asset ID to update: ").strip()

    for asset in assets:
        if asset["id"] == asset_id:

            print("\nLeave input empty to keep the existing value.")

            new_name = input(
                f"Asset Name [{asset['name']}]: "
            ).strip()

            new_ip = input(
                f"IP Address [{asset['ip']}]: "
            ).strip()

            new_os = input(
                f"Operating System [{asset['os']}]: "
            ).strip()

            new_department = input(
                f"Department [{asset['department']}]: "
            ).strip()

            if new_name:
                asset["name"] = new_name

            if new_ip:
                asset["ip"] = new_ip

            if new_os:
                asset["os"] = new_os

            if new_department:
                asset["department"] = new_department

            print("\nAsset updated successfully!")
            return

    print("Asset not found.")


# ------------------------------------------
# DELETE ASSET
# ------------------------------------------

def delete_asset():
    print("\n========== DELETE ASSET ==========")

    asset_id = input("Enter Asset ID to delete: ").strip()

    for asset in assets:
        if asset["id"] == asset_id:

            assets.remove(asset)

            print("Asset deleted successfully!")
            return

    print("Asset not found.")


# ------------------------------------------
# SUMMARY
# ------------------------------------------

def show_summary():
    print("\n=========================================")
    print("             ASSET SUMMARY")
    print("=========================================")

    total_assets = len(assets)

    critical_assets = 0
    high_risk_assets = 0
    medium_risk_assets = 0
    vulnerable_assets = 0

    for asset in assets:

        if asset["risk"] == "Critical":
            critical_assets += 1

        if asset["risk"] == "High":
            high_risk_assets += 1

        if asset["risk"] == "Medium":
            medium_risk_assets += 1

        if asset["status"] == "Vulnerable":
            vulnerable_assets += 1

    print(f"Total Assets      : {total_assets}")
    print(f"Critical Assets   : {critical_assets}")
    print(f"High Risk Assets  : {high_risk_assets}")
    print(f"Medium Risk Assets: {medium_risk_assets}")
    print(f"Vulnerable Assets : {vulnerable_assets}")

    print("=========================================")


# ------------------------------------------
# MAIN MENU
# ------------------------------------------

def main():

    while True:

        print("\n")
        print("=========================================")
        print(" CYBERSECURITY ASSET INVENTORY SYSTEM")
        print("=========================================")

        print("1. Add Asset")
        print("2. Search Asset")
        print("3. Update Asset")
        print("4. Delete Asset")
        print("5. Display All Assets")
        print("6. Show Summary")
        print("7. Exit")

        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            add_asset()

        elif choice == "2":
            search_asset()

        elif choice == "3":
            update_asset()

        elif choice == "4":
            delete_asset()

        elif choice == "5":
            display_assets()

        elif choice == "6":
            show_summary()

        elif choice == "7":
            print("\nThank you for using the system!")
            break

        else:
            print("\nInvalid choice. Please try again.")


# ------------------------------------------
# PROGRAM START
# ------------------------------------------

if __name__ == "__main__":
    main()
