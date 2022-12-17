

# ================ Neutron Monitor Database (NMDB) ================ #

import urllib,os
from bs4 import BeautifulSoup
import pandas as pd

# Polar NMs....
station_list =  sorted(["SNAE","OULU","NAIN", "MCMU","THUL","APTY"])
# Note ! Kiel, DRBS, MOSC -->> unstable NMs

Begin_datetime, End_datetime = "1957-01-01", "2022-12-31" 
start_year,start_month,start_day = str(Begin_datetime).split("-")
end_year,end_month,end_day = str(End_datetime).split("-")
os.system("mkdir -p "+str(start_year)+"-"+str(end_year)+"/Measured_data")
for NM_Station_ in station_list:
  print ("\n Downloading data for ---> ",NM_Station_)
  try:
    url_ = "http://nest.nmdb.eu/draw_graph.php?formchk=1&stations[]={NM_Station_}&tabchoice=1h&dtype=corr_for_efficiency&tresolution=60&force=1&yunits=0&date_choice=bydate&start_day={start_day}&start_month={start_month}&start_year={start_year}&start_hour=0&start_min=0&end_day={end_day}&end_month={end_month}&end_year={end_year}&end_hour=23&end_min=59&output=ascii&display_null=1"
    URL = url_.format(NM_Station_=NM_Station_, start_day=start_day, start_month=start_month, start_year=start_year, end_day=end_day, end_month=end_month, end_year=end_year)
    WebR = urllib.request.urlopen(URL)
    parserHTML = WebR.read()
    Bsoup = BeautifulSoup(parserHTML, features="html.parser")
    Tx = Bsoup.find_all('pre')[0].text    
    #Tx = Tx[Tx.find('start_date_time'):]
    Tx = Tx.replace("start_date_time   1HCOR_E","# Datetime, Counts/s")
    File_ = open(str(start_year)+"-"+str(end_year)+"/Measured_data/" +str(NM_Station_)+".txt", "w")
    File_.write(Tx)
    File_.close()
  except:
    print (NM_Station_," ! Could not download and process data...")
print (' \n\n Done saving datasets !!!!!!.......\n\n')

  
 
