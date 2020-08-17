#!/usr/bin/env python3

import datetime
import os

from run import catalog_data
from reports import generate_report
from emails import generate_email, send_email


def pdf_body(input_for,desc_dir):
    """Generating a summary with two lists, which gives the output name and weight"""
    nam,wt = [],[]
    for item in os.listdir(desc_dir):
      filename=os.path.join(desc_dir,item)
      with open(filename) as file:
        line=file.readlines()
        name=line[0].strip('\n')
        weight=line[1].strip('\n')
        # print(name,weight)
        nam.append('name: ' +name)
        wt.append('weight: ' +weight)
        # print(nam)
        # print(wt)
    new_obj = ""  # initializing the object
    # Calling values from two lists one by one.
    for i in range(len(nam)):
        if nam[i] and input_for == 'pdf':
            new_obj += nam[i] + '<br />' + wt[i] + '<br />' + '<br />'
    return new_obj

if __name__ == "__main__":
    user = os.getenv('USER')
    desc_dir = '/home/'+user+'/supplier-data/descriptions/'  # The directory which contains all the files with data in it.
    today = datetime.date.today().strftime("%B %d, %Y")  # Creating data in format "May 5, 2020"
    title = 'Processed Update on ' + str(today)  # Title for the PDF file with the created date
    generate_report('/tmp/processed.pdf', title, pdf_body('pdf',desc_dir))  # calling the report function from custom module
    subject = 'Upload Completed - Online Fruit Store'  # subject line give in assignment for email
    body = 'All fruits are uploaded to our website successfully. A detailed list is attached to this email.'  # body line give in assignment for email
    msg = generate_email("automation@example.com", user+"@example.com",
                         subject, body, "/tmp/processed.pdf")  # structuring email and attaching the file. Then sending the email, using the cus$
    send_email(msg)
