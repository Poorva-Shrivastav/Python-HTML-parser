from bs4 import BeautifulSoup
import os
import glob
import csv

f = csv.writer(open("candidates.csv", 'w'))
f.writerow(['Name', 'Email', 'Mobile No'])

os.chdir("path to directory")  


for file in list(glob.glob("*.htm")):
	reader = open(file)
	soup = BeautifulSoup(reader, 'html.parser')

	names = soup.findAll("span", {"class" : "bkt4 name userName"})
	for name in names:
		cand_names = name.text.strip()

	emails =  soup.findAll("span", {"class":"txtGreen bkt4 email"}) 
	for email in emails:
		cand_emails = email.text.strip()
	
	mobile_no = soup.findAll("div", {"class":"bkt4 phoneNo"})
	for mobile in mobile_no:
		cand_nos = mobile.text.strip("Contact:")

        f.writerow([cand_names, cand_emails, cand_nos])



