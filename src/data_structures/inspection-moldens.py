import requests
import pycomm3

from pycomm3 import LogixDriver

with LogixDriver('192.168.1.5') as plc:
  print(plc)
  
  print(plc._cip_path)
 
  