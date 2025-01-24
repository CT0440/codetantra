# A weather system needs to convert temperature from Celsius to 
# Fahrenheit. Use the appropriate arithmetic operator to implement the 
#  conversion and check if the result exceeds a certain threshold.



# | **Property**           | **Celsius (°C)** | **Fahrenheit (°F)** |
# |-------------------------|------------------|---------------------|
# | **Freezing Point**      | 0°C              | 32°F                |
# | **Boiling Point**       | 100°C            | 212°F               |


def celsius_to_fahrenheit(celsius_temp, threshold):
    fahrenheit = 32 + (9 / 5 * celsius_temp)
    exceeds_threshold = fahrenheit > threshold
    return fahrenheit, exceeds_threshold

# Input from the user
celsius_temp = float(input("Enter the temperature in Celsius: "))
threshold = float(input("Enter the threshold value in Fahrenheit: "))

# Call the function
fahrenheit_temp, exceeds = celsius_to_fahrenheit(celsius_temp, threshold)

# Display results
print(f"The converted Fahrenheit temperature is: {fahrenheit_temp:.2f}°F")
if exceeds:
    print(f"The temperature exceeds the threshold of {threshold}°F.")
else:
    print(f"The temperature does not exceed the threshold of {threshold}°F.")
