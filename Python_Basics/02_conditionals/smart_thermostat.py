device_status = input("Enter the device status (on/off): ").strip().lower()

if device_status == "on" :
    
    temperature = float(input("Enter the current temperature in Celsius: "))

    if temperature > 35:  
        print("High Temperature Alert! The device is on and the temperature is above 35°C. Please take necessary precautions.")
    else:
        print("Temperature is normal")
else:
    print("The device is off. No temperature monitoring is needed.")