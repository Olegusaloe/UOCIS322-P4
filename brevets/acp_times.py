"""
Open and close time calculations
for ACP-sanctioned brevets
following rules described at https://rusa.org/octime_alg.html
and https://rusa.org/pages/rulesForRiders
"""
import arrow


#  You MUST provide the following two functions
#  with these signatures. You must keep
#  these signatures even if you don't use all the
#  same arguments.
#

# ------------------------------------------------------------

def val(arg):
    
    v = 200 / 34 
    if arg == 200:
       return v
    
    v += (100/32)
    if arg == 300:
       return v

    v += (100/32)
    if arg == 400:
       return v

    v += (200/30)
    if arg == 600:
       return v

    v += (400/28)
    if arg == 1000:
       return v


def open_time(control_dist_km, brevet_dist_km, brevet_start_time):
    """
    Args:
       control_dist_km:  number, control distance in kilometers
       brevet_dist_km: number, nominal distance of the brevet
           in kilometers, which must be one of 200, 300, 400, 600,
           or 1000 (the only official ACP brevet distances)
       brevet_start_time:  A date object (arrow)
    Returns:
       A date object indicating the control open time.
       This will be in the same time zone as the brevet start time.
    """
    
    # Cheking for basic errors
    if (control_dist_km < 0):   
      raise ValueError  

    if control_dist_km > (brevet_dist_km * 1.2):
      raise ValueError

    # Determine the number of hours to shift
    h = 0

    if control_dist_km >= brevet_dist_km:
       
       if brevet_dist_km == 200:
          h = val(200)
       elif brevet_dist_km == 300:
          h = val(300)
       elif brevet_dist_km == 400:
          h = val(400)
       elif brevet_dist_km == 600:
          h = val(600)
       elif brevet_dist_km == 1000:
          h = val(1000)
 
    else:  
      
      if control_dist_km < 200:
         h = control_dist_km / 34
      
      elif control_dist_km < 300 and control_dist_km >= 200:
         h = ((control_dist_km - 200) / 32) + val(200)
      
      elif control_dist_km < 400 and control_dist_km >= 300:
         h = ((control_dist_km - 300) / 32) + val(300)       
      
      elif control_dist_km < 600 and control_dist_km >= 400:
         h = ((control_dist_km - 400) / 30) + val(400) 
      
      else:
         h = ((control_dist_km - 600) / 28) + val(600) 
    

    
    return brevet_start_time.shift(minutes=round(h * 60))

# ---------------------------------------------------------------

def vall(arg):

    v = 200 / 15 
    if arg == 200:
       return v
    
    v += (100/15)
    if arg == 300:
       return v

    v += (100/15)
    if arg == 400:
       return v

    v += (200/15)
    if arg == 600:
       return v

    v += (400/11.428)
    if arg == 1000:
       return v


def close_time(control_dist_km, brevet_dist_km, brevet_start_time):
    """
    Args:
       control_dist_km:  number, control distance in kilometers
          brevet_dist_km: number, nominal distance of the brevet
          in kilometers, which must be one of 200, 300, 400, 600, or 1000
          (the only official ACP brevet distances)
       brevet_start_time:  A date object (arrow)
    Returns:
       A date object indicating the control close time.
       This will be in the same time zone as the brevet start time.
    """

    # Cheking for basic errors
    if (control_dist_km < 0):   
      raise ValueError  

    if control_dist_km > (brevet_dist_km * 1.2):
      raise ValueError

    # Determine the number of hours to shift
    h = 0

    if control_dist_km >= brevet_dist_km:
       
       if brevet_dist_km == 200:
          h = 13.5
       elif brevet_dist_km == 300:
          h = 20
       elif brevet_dist_km == 400:
          h = 27
       elif brevet_dist_km == 600:
          h = 40
       elif brevet_dist_km == 1000:
          h = 75

    else:  
      
      if control_dist_km < 200:
         h = control_dist_km / 15
         
         if control_dist_km < 60:
            h += (60 - control_dist_km)/60
      
      elif control_dist_km < 300 and control_dist_km >= 200:
         h = ((control_dist_km - 200) / 15) + vall(200)
      
      elif control_dist_km < 400 and control_dist_km >= 300:
         h = ((control_dist_km - 300) / 15) + vall(300)       
      
      elif control_dist_km < 600 and control_dist_km >= 400:
         h = ((control_dist_km - 400) / 15) + vall(400) 
      
      else:
         h = ((control_dist_km - 600) / 28) + vall(600) 



    # Shifting
    return brevet_start_time.shift(minutes=round(h * 60))



