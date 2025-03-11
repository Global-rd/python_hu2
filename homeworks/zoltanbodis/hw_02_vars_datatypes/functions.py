import datetime

def f_age_in_days(age, mode):
    """
    kiszámolja valakinek a korát napokban az életkorból, feltételezve, hogy ma van a születésnapja
    """    
    # mai dátum
    today = datetime.date.today()
    
    if mode == 1:
        # születési év: a mai dátumból véve az év mínusz az életkor  
        # mivel feltételezzük, hogy ma van a szülinapja, ezért a hónapot és a napot is vehetjük a mai dátumból      
        birth_date = datetime.date(today.year - age, today.month, today.month)
        
        #vesszük a két dátum különbségét napokban
        age_in_days = (today - birth_date).days
    elif mode == 2:
        # kerekítős módszer: az életkorát beszorozzuk egy átlagos évnyi napszámmal
        # minden negyedik év szökőév, vagyis egy átlagos évben 365.25 nap van
        avg_days =  365.25
        age_in_days = int(age * avg_days)
    
    return age_in_days
