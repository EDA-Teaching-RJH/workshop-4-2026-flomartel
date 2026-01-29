def main():
  print("--- ORBITAL DOCKING SYSTEM ---")
ship_name = input("Enter Ship Name: ")
    new_name = ship_name.replace(" ", "_").upper()
    print(f"new_name:{new_name}")
 
    cargo_input = input("Enter Cargo Value (e.g., ¢100.00): ")
    removed = float(cargo_input[1:])
    print(f"Cargo Value:{removed}")

    reg_id = int(input("Enter Ship ID (Integer): "))
    bay = assign_bay(reg_id)
    print(f"Assigned to: {bay}")

 # PART 3: Clearance Level
    shields = int(input("Shield Integrity %: "))
 # TODO: Write if/elif/else logic to check shield ranges

 # PART 4: Crew Routing
    div_code = input("Enter Division Code (CMD, NAV, ENG, SCI, MED): ")
 # TODO: Write a match/case statement for the division code

  
    
def assign_bay(n):
    # Modulo check for even/odd
    if n % 2 == 0:
        return "Starboard Bay"
    else:
        return "Port Bay"

main()
   





