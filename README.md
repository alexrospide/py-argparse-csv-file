# py-argparse-csv-file

Script developed to create a CSV file with random data throught cli comands with argparse paramiters

# :hammer: Project features

- `Optional Arguments`: The script is prepared to receive two optional arguments as, --path to print the file path before finish the script, and --encoding to inform a diferent encoding then default utf-8
- `Positional Arguments`: These are required arguments to run the script, first is file name, then delimiter and row numbers 
- `Function`: After receive correct paramiters the script will create a csv file with a defined header as "owner_name", "email", "month_quota", "start_date" then all data are created with Faker witch is a Python package that generates fake data. The csv file can be used to do stress tests, registrations or graphics for an example. 

# :heavy_check_mark: Technologies and Dependencies
* Python 3.12
* argparse
* csv
* os

# :mechanical_arm: How to
* Python 3.12 installed required
* Download repository files
* Open terminal and acess project folder
* python .\py-argparse.py --path --encoding "<file_name>" "<delimiter>" <row_number>
  * and for help run the script with -h or --help to see more information
  * python .\py-argparse.py --help  

![Badge em Desenvolvimento](http://img.shields.io/static/v1?label=dEV&message=PYTHON&color=GREEN&style=for-the-badge)