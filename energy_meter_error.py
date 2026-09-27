# energy_meter_error.py
# Program to calculate the percentage error of an energy meter

# Input values
actual_energy = float(input("Enter actual energy consumed (kWh): "))
meter_energy = float(input("Enter energy recorded by meter (kWh): "))

# Calculate error
error = meter_energy - actual_energy

# Calculate percentage error
percentage_error = (error / actual_energy) * 100

# Calculate accuracy
accuracy = 100 - abs(percentage_error)

# Display results
print("\n--- Energy Meter Error Calculation ---")
print(f"Actual Energy       = {actual_energy:.3f} kWh")
print(f"Meter Energy        = {meter_energy:.3f} kWh")
print(f"Error               = {error:.3f} kWh")
print(f"Percentage Error    = {percentage_error:.2f}%")
print(f"Meter Accuracy      = {accuracy:.2f}%")

# Determine whether the meter is fast or slow
if error > 0:
    print("Meter Status        = Fast")
elif error < 0:
    print("Meter Status        = Slow")
else:
    print("Meter Status        = Accurate")
