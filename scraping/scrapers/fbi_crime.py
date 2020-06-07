import requests
import os
import time

year = 2016
data_folder = "./data/{}".format(year)
if not os.path.exists(data_folder):
    os.makedirs(data_folder)

"""Download Offenses and Clearance tables"""

#offenses_table_nums = range(1, 25) + ['1A']
#clearances_table_nums = range(25, 29)
offenses_and_clearances_table_names = ["table-{}".format(i) for i in list(range(1, 29)) + ["1A"]]


for i, table_i in enumerate(offenses_and_clearances_table_names):
	offenses_and_clearances_url = "https://ucr.fbi.gov/crime-in-the-u.s/{0}/crime-in-the-u.s.-{0}/tables/{1}/{1}.xls/output.xls".format(year, table_i)
	response = requests.get(offenses_and_clearances_url)

	if i < 25:
		filename = "{}_offenses_{}.xls".format(year, table_i)
	else:
		filename = "{}_clearances_{}.xls".format(year, table_i)

	with open(os.path.join(data_folder, filename), 'wb') as f:
		f.write(response.content)
	
	print('Downloading {}...'.format(filename))
	time.sleep(1)

"""Download Robbery and Homicide tables """

robbery_and_assault_table_names = ["robbery-table-{}".format(i) for i in [1, 2, 3]] + ['aggravated-assault']
expanded_homicide_table_names = ['expanded-homicide-data-table-{}'.format(i) for i in range(1, 15)]

other_tables = robbery_and_assault_table_names + expanded_homicide_table_names
for i, table_i in enumerate(other_tables):
	offenses_and_clearances_url = "https://ucr.fbi.gov/crime-in-the-u.s/{0}/crime-in-the-u.s.-{0}/tables/{1}.xls/output.xls".format(year, table_i)
	response = requests.get(offenses_and_clearances_url)

	filename = "{0}_{1}.xls".format(year, table_i)

	with open(os.path.join(data_folder, filename), 'wb') as f:
		f.write(response.content)
	
	print('Downloading {}...'.format(filename))
	time.sleep(1)