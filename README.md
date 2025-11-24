# Caller-Id-Lookup
A simple Python-based program that provides information about the phone numbers including carrier, location, and timezone data.

## Features

- **Location Detection**: Identifies the geographic location associated with a phone number
- **Carrier Identification**: Determines the service provider for the number
- **Timezone Information**: Shows all timezones associated with the number's region
- **Number Validation**: Verifies if a phone number is valid before lookup
- **Interactive CLI**: Simple command-line interface for easy usage

## Requirements

- Python 3.6 or higher
- phonenumbers library

## Installation

1. Clone this repository:

git clone 
cd caller-id-lookup


2. Install the required dependency:

pip install phonenumbers


## Usage

Run the script:

python caller_id_lookup.py


Enter a phone number with the country code (e.g., +1 555-123-4567 for US numbers, +44 20 1234 5678 for UK numbers).

### Example


Simple Caller ID Tool
Type 'exit' to quit.

Enter phone number (with +country code): +1 650-253-0000
--------------------------------------
Results for: +1 650-253-0000
--------------------------------------
Location:    United States
Carrier:     
Timezones:   America/Los_Angeles
--------------------------------------


Type exit to quit the program.

## How It Works

The tool uses the phonenumbers library to:
1. Parse the input phone number
2. Validitate the input
3. shows the carrier information
4. Determine geographic location
5. Shows the timezones

## Error Handling

- **Invalid Format**: The tool will ask you to include the country code if it's missing
- **Invalid Number**: Shows you if the number format is incorrect or doesn't exist

## Limitations

- Carrier information may not be available for all numbers
- Location data shows the region/country, not exact addresses
- Mobile number portability may affect carrier accuracy

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source.

## Acknowledgments

Built using the phonenumbers library
