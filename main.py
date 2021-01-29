import time

def metodoa():
    #Aqui definimos el diccionario basicamente es como un hashmap con keys y values
    pertsona={'izena': 'Oskar','abizena1': 'Casquero','abizena2': 'Oyarzabal'}



    #De aqui lo que sacamos es el value del key 'izena'
    print(pertsona['izena'])


    #Para añadir otro valor al diccionario
    pertsona['herria']='Amurrio'


    #Mediante esto recorremos el diccionario entero sacando los keys y los values
    for key in pertsona.keys():
        print(key + '='+pertsona[key])


    #Esto sirve para meter varios valores al diccionario
    beste_datuak={'jaiotze_data': '1979-01-01','NAN': '12345678-A'}
    pertsona.update(beste_datuak)


    ikasgaiak = ['Web Sistemak','KonputagailuSareenOinarriak','Datu-baseenDiseinua','Datu-baseenKudeaketa','Datu-egituraketa Algoritmoak']

    print("HEMENDIK AURRERA")

    print(ikasgaiak[0])


    #Los arrays tienen una estructura circular
    print(ikasgaiak[-2])

    #Para printear solo los primeros dos
    print(ikasgaiak[:2])

    #Para printear todos menos los primeros dos
    print(ikasgaiak[2:])

    #Te recorre el array
    for ikasgaia in ikasgaiak:
        print(ikasgaia)

    #Pones la i al principio para definirla como en la estructura clasica del for en java
    #Find lo que hace es te busca ese palabra en la cadena y si existe te devuelve el indice
    #de la primera aparicion de ese elemento y sino existe te devuelve -1

    zerrenda_berria = [i for i in ikasgaiak if i.find('Datu') != -1]
    print("hemen")
    print(zerrenda_berria)

    #Append es el add de java
    zerrenda_berria.append('Proiektuen Kudeaketa')
    print(zerrenda_berria)

    #Te devuelve el indice de un elemento que sabes que esta en la lista
    print(zerrenda_berria.index('Proiektuen Kudeaketa'))

    #Es el remove de java
    zerrenda_berria.remove('Proiektuen Kudeaketa')

    if 'Proiektuen kudeaketa' in zerrenda_berria:
        print("dago")
    else:
        print("ez dago")

    pertsona = {'id': 'cvzcaoio', 'desc': {'firstName': 'Oskar', 'lastName': ['Casquero', 'Oyarzabal']},
                'contact': {'email': 'oskar.casquero@ehu.es', 'phone': '946014459'},
                'courses': [{'code': 27699, 'desc': 'Introduction to Computer Networks'},
                            {'code': 27702, 'desc': 'Web Systems'}]}

    print(pertsona['id'])

    print(pertsona['desc']['lastName'])
    print(pertsona['contact']['email'])
    print(pertsona['courses'][0]['code'])




if __name__ == '__main__':
    metodoa()

