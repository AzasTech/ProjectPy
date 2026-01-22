import shutil
from datetime import datetime
import os
import string

# Function to detect all available drives (Windows only)
def get_available_drives():
    drives = []
    for letter in string.ascii_uppercase:
        path = f"{letter}:\\"
        if os.path.exists(path):
            drives.append(path)
    return drives

# Function to generate a disk usage report for a given path
def check_disk(path):
    total, used, free = shutil.disk_usage(path)
    usage_percent = (used / total) * 100

    report = []
    report.append(f"Path: {path}")
    report.append(f"Total: {total // (2**30)} GB")
    report.append(f"Used:  {used // (2**30)} GB")
    report.append(f"Free:  {free // (2**30)} GB")
    report.append(f"Usage: {usage_percent:.2f}%")

    if usage_percent > 80:
        report.append("Status: WARNING - Disk usage is high")
    else:
        report.append("Status: OK")

    return "\n".join(report)

# Function to save the report to disk_report.txt in the script's folder
def save_report(content):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, "disk_report.txt")
    with open(file_path, "a") as file:
        file.write(f"\n[{datetime.now()}]\n")
        file.write(content)
        file.write("\n" + "-" * 40 + "\n")

# Main program function
def main():
    print("💾 Disk Space Checker")
    print("====================\n")

    # Detect all drives
    drives = get_available_drives()
    if not drives:
        print("❌ No drives detected. Exiting.")
        return

    # If only one drive is found, check it automatically
    if len(drives) == 1:
        print(f"Only one drive detected: {drives[0]}")
        selected_drives = drives
    else:
        # Multiple drives found, show menu for selection
        print("Available drives:")
        for i, d in enumerate(drives, start=1):
            print(f"{i}) {d}")
        print(f"{len(drives)+1}) All drives")

        # Ask user to choose
        choice = input("\nEnter your choice: ").strip()

        # All drives selected
        if choice == str(len(drives)+1):
            selected_drives = drives
        # Single drive selected
        elif choice.isdigit() and 1 <= int(choice) <= len(drives):
            selected_drives = [drives[int(choice)-1]]
        else:
            print("❌ Invalid choice. Exiting.")
            return

    # Generate and print reports
    full_report = []
    for path in selected_drives:
        report = check_disk(path)
        print("\n" + report)
        print("-" * 40)
        full_report.append(report)

    # Save all reports to file
    save_report("\n\n".join(full_report))
    print("\n✅ Report saved to disk_report.txt")

# Run the program
if __name__ == "__main__":
    main()
