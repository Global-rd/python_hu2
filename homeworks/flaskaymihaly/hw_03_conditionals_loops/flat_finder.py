
location=input("where is the appartement? ").lower()


if location=="washington":
    print(f"Because Sarah hates", location.title() , ", she would not want to move into that appartement")

elif location=="chicago":
    print(f"Because Sarah loves", location.title() , ", she would want to move into that appartement")

elif location in ["new york", "san francisco"]:
    fee=int(input("what is the monthly rental fee? "))
    dev_intention="would" if fee<=4000 else "would not"
    print(f"With the given rental fee of", fee, "dollars/month, Sarah ", dev_intention," move into the appartement in" ,location.title() ,"")

else:
    fee=int(input("what is the rental fee? "))
    dev_intention="would" if fee<=3000 else "would not"
    print(f"With the given rental fee of", fee, "dollars/month, Sarah ", dev_intention," move into the appartement in" ,location.title() ,"")
    
    
    


    