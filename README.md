# Google-spec-final-project
Final qwiklabs project

-----------------------------------------------------------------------------------
                                changeImage.py
-----------------------------------------------------------------------------------
Changes the following parameters of images.

Size: Change image resolution from 3000x2000 to 600x400 pixel
Format: Change image format from .TIFF to .JPEG

-----------------------------------------------------------------------------------
                           supplier_image_upload.py
-----------------------------------------------------------------------------------
Takes the images processed by changeImage.py script and uploads them to web server.

-----------------------------------------------------------------------------------
                                   run.py
-----------------------------------------------------------------------------------
Processes the text files (001.txt, 003.txt ...) from the 'supplier-data/descriptions'
directory. The script should turn the data into a JSON dictionary by adding all the
required fields, including the image associated with the fruit (image_name), and
uploading it to web server using the Python requests library.

-----------------------------------------------------------------------------------
                                  reports.py
-----------------------------------------------------------------------------------
Generates PDF report to be sent to supplier. The data in the pdf comes from 
report_email.py scripts which processes data.

-----------------------------------------------------------------------------------
                                report_email.py
-----------------------------------------------------------------------------------
Processes supplier description data from 'supplier-data/descriptions' directory. 

-----------------------------------------------------------------------------------
                                   email.py
-----------------------------------------------------------------------------------
Once the PDF is generated by reports.py, you need to send the email using this script.

-----------------------------------------------------------------------------------
                                health_check.py
-----------------------------------------------------------------------------------
Reports an error if CPU usage is over 80%
Reports an error if available disk space is lower than 20%
Reports an error if available memory is less than 500MB
Reports an error if the hostname "localhost" cannot be resolved to "127.0.0.1"
