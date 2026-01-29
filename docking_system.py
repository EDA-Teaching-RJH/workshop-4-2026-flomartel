def main():
 print("--- ORBITAL DOCKING SYSTEM ---")

 # PART 1: String Manipulation
 ship_name = input("Enter Ship Name: ")
 new_name = ship_name.replace(" ", "_").upper()
 print(f"new_name:{new_name}")


 # TODO: Convert ship_name to uppercase and replace spaces with underscores

cargo_input = input("Enter Cargo Value (e.g., ¢100.00): ")
 # TODO: Remove the first character and convert to float

 # PART 2: Bay Assignment
reg_id = int(input("Enter Ship ID (Integer): "))
 # TODO: Call assign_bay(reg_id) and print the result

 # PART 3: Clearance Level
shields = int(input("Shield Integrity %: "))
 # TODO: Write if/elif/else logic to check shield ranges

 # PART 4: Crew Routing
div_code = input("Enter Division Code (CMD, NAV, ENG, SCI, MED): ")
 # TODO: Write a match/case statement for the division code
def assign_bay(n):
 # TODO: Use modulo (%) to return "Starboard Bay" for even or "Port Bay" for odd
 return ""

 
main()





