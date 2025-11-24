import phonenumbers
from phonenumbers import carrier, geocoder, timezone

def lookup_number(phone_number):
    try:
        
        parsed_number = phonenumbers.parse(phone_number, None)

        
        if not phonenumbers.is_valid_number(parsed_number):
            print(f"Error: {phone_number} is not a valid number.")
            return

        
        service_provider = carrier.name_for_number(parsed_number, "en")

       
        location = geocoder.description_for_number(parsed_number, "en")

        time_zones = timezone.time_zones_for_number(parsed_number)

        print("--------------------------------------")
        print(f"Results for: {phone_number}")
        print("--------------------------------------")
        print(f"Location:    {location}")
        print(f"Carrier:     {service_provider}")
        print(f"Timezones:   {', '.join(time_zones)}")
        print("--------------------------------------")

    except phonenumbers.NumberParseException:
        print("Error: Please include the country code (e.g., +1 for US, +44 for UK).")

if __name__== "__main__":
    print("Simple Caller ID Tool")
    print("Type 'exit' to quit.")
    
    while True:
        user_input = input("\nEnter phone number (with +country code): ")
        
        if user_input.lower() == 'exit':
            break
            
        lookup_number(user_input)
        