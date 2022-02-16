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
  Remove reduntant code/change some of the console verbage from pre-scheduled task version.
  Add functionality to alert user beyond the console. Pop-up, Email, SMS, etc.(Though this might be better suited for a completely new script)
  
USAGE:
Current usage leverages event scheduler (or cron) to run this script periodically. 
Output is text files containing logged changes.
