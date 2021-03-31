# ThocStockScraper
This Python script scrapes Stocklists from ThocStock, detecting changes and alerting the user. 

DEPENDENCIES (Bolded are non-standard Python Libraries):
  re
  os
  time
  **requests**
  **re**

TO-DO:
  Documentation, there isn't a ton to do- but there isn't any at the moment.
  More mature start-up/running methods. At moment, this script just loops once per 10 minutes to recheck stock. Allowing the user to check stock before the time.sleep() is over would be smart.
  Maybe add functionality to alert user beyond the console. Pop-up, Email, SMS, etc.
  
USAGE:
  Starting the script will make a series of web requests to ThocStock, and compare the current stock lists to the ones held within the 8 Stock Files. The differences will be printed in console, and the files will be updated. Currently, there is a time.sleep(600) at line 64- this allows the stock check to run every 10 minutes, change this if you want the script to run more frequently.
