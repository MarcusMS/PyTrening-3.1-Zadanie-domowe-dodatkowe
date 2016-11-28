def pobierz_tekst():
    zdanie = input("Wpisz zdanie: ").split()
    return zdanie
    
def check_f(i):
    for key in zakazane_slowa:
        if key in i.lower():
            print (zakazane_slowa[key])
            return True
        else:
            continue

                   

def wyswietl_tekst(zdanie, zakazane_slowa):
    for i in zdanie:
        if check_f(i) == True:
            pass
        else:
            print (i.capitalize())
   
zakazane_slowa = {"voldemort":"Sam-wiesz-kto", "lord":"Taki tam pamperek", "czarnoksiężnik":"Magik"}
wyswietl_tekst(pobierz_tekst(), zakazane_slowa)


