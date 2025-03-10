
location=input("where is the appartement? ").lower()


if ("washington"== location):
    print(f"Because Sarah hates", location.title() , ", she would not want to move into that appartement")

elif ("chicago"== location):
    print(f"Because Sarah loves", location.title() , ", she would want to move into that appartement")

elif ("new york"== location or "san francisco"== location):
    fee=int(input("what is the monthly rental fee? "))
    dev_intention="would" if fee<=4000 else "would not"
    print(f"With the given rental fee of", fee, "dollars/month, Sarah ", dev_intention," move into the appartement in" ,location.title() ,"")

else:
    fee=int(input("what is the rental fee? "))
    dev_intention="would" if fee<=3000 else "would not"
    print(f"With the given rental fee of", fee, "dollars/month, Sarah ", dev_intention," move into the appartement in" ,location.title() ,"")
    
    
    


    