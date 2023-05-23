import requests
import global_vars

def verify_valid_moldens():
  return request.post(global_vars.API_URL + '/moldens/verify-valid-moldens',
    json=global_vars.moldens_to_verify,
    headers=global_vars.headers).json
  

  
  