def ip():
    import requests
    import os


    def clear(): os.system('clear')


    verde = "\033[1;32m"

    print('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓')

    print(""" 
    ⠄⠄⠄⢰⣧⣼⣯⠄⣸⣠⣶⣶⣦⣾⠄⠄⠄⠄⡀⠄⢀⣿⣿⠄⠄⠄⢸⡇⠄⠄
    ⠄⠄⠄⣾⣿⠿⠿⠶⠿⢿⣿⣿⣿⣿⣦⣤⣄⢀⡅⢠⣾⣛⡉⠄⠄⠄⠸⢀⣿⠄
    ⠄⠄⢀⡋⣡⣴⣶⣶⡀⠄⠄⠙⢿⣿⣿⣿⣿⣿⣴⣿⣿⣿⢃⣤⣄⣀⣥⣿⣿⠄
    ⠄⠄⢸⣇⠻⣿⣿⣿⣧⣀⢀⣠⡌⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⠿⣿⣿⣿⠄
    ⠄⢀⢸⣿⣷⣤⣤⣤⣬⣙⣛⢿⣿⣿⣿⣿⣿⣿⡿⣿⣿⡍⠄⠄⢀⣤⣄⠉⠋⣰
    ⠄⣼⣖⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⣿⣿⣿⣿⣿⢇⣿⣿⡷⠶⠶⢿⣿⣿⠇⢀⣤
    ⠘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣽⣿⣿⣿⡇⣿⣿⣿⣿⣿⣿⣷⣶⣥⣴⣿⡗
    ⢀⠈⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠄
    ⢸⣿⣦⣌⣛⣻⣿⣿⣧⠙⠛⠛⡭⠅⠒⠦⠭⣭⡻⣿⣿⣿⣿⣿⣿⣿⣿⡿⠃⠄
    ⠘⣿⣿⣿⣿⣿⣿⣿⣿⡆⠄⠄⠄⠄⠄⠄⠄⠄⠹⠈⢋⣽⣿⣿⣿⣿⣵⣾⠃⠄
    ⠄⠘⣿⣿⣿⣿⣿⣿⣿⣿⠄⣴⣿⣶⣄⠄⣴⣶⠄⢀⣾⣿⣿⣿⣿⣿⣿⠃⠄⠄
    ⠄⠄⠈⠻⣿⣿⣿⣿⣿⣿⡄⢻⣿⣿⣿⠄⣿⣿⡀⣾⣿⣿⣿⣿⣛⠛⠁⠄⠄⠄
    ⠄⠄⠄⠄⠈⠛⢿⣿⣿⣿⠁⠞⢿⣿⣿⡄⢿⣿⡇⣸⣿⣿⠿⠛⠁⠄⠄⠄⠄⠄
    ⠄⠄⠄⠄⠄⠄⠄⠉⠻⣿⣿⣾⣦⡙⠻⣷⣾⣿⠃⠿⠋⠁⠄⠄⠄⠄⠄⢀⣠⣴
    ⣿⣿⣿⣶⣶⣮⣥⣒⠲⢮⣝⡿⣿⣿⡆⣿⡿⠃⠄⠄⠄⠄⠄⠄⠄⣠⣴⣿⣿⣿
    """)
    print('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛')

    print('Eu não sou responsável por seus atos maliciosos')
    print('Extrai dados de ip e domínio')
    print('Contém localizador')
    print('Feedback ou erros: GitHub BunnyGhost')
    print('~~~~~~~~~~~~~')
    print(' ')
    x = input('IP ou domínio: ')

    ip = requests.get(
        f'http://ip-api.com/json/{x}?fields=status,message,continent,continentCode,country,countryCode,region,regionName,city,district,zip,lat,lon,timezone,offset,currency,isp,org,as,asname,reverse,mobile,proxy,hosting,query').json()

    if 'message' not in ip:
        clear()
        print(f""" {verde}                                                                     
     @@@@@@ @@@@@@@@  @@@@@@  @@@@@@@   @@@@@@@ @@@  @@@    @@@ @@@@@@@  
    !@@     @@!      @@!  @@@ @@!  @@@ !@@      @@!  @@@    @@! @@!  @@@ 
     !@@!!  @!!!:!   @!@!@!@! @!@!!@!  !@!      @!@!@!@!    !!@ @!@@!@!  
        !:! !!:      !!:  !!! !!: :!!  :!!      !!:  !!!    !!: !!:      
    ::.: :  : :: ::   :   : :  :   : :  :: :: :  :   : :    :    :       
                                                                         """)
        print('━━━━━━━━━━━━━━━━━━━━━━━━━┓')
        print('Status: {}'.format(ip['status']))
        print('')
        print(' ')
        print('@País: {}'.format(ip['continent']))
        print('@Código do país: {}'.format(ip['continentCode']))
        print('@Região: {}'.format(ip['country']))
        print('@Código do continente: {}'.format(ip['countryCode']))
        print('@Região: {}'.format(ip['region']))
        print('@Nome da região: {}'.format(ip['regionName']))
        print('@Cidade: {}'.format(ip['city']))
        print('@Distrito: {}'.format(ip['district']))
        print('@Zip: {}'.format(ip['zip']))
        print('@Latitude: {}'.format(ip['lat']))
        print('@Longitude: {}'.format(ip['lon']))
        print('@Fuso horário: {}'.format(ip['timezone']))
        print('@Offset: {}'.format(ip['offset']))
        print('@Moeda: {}'.format(ip['currency']))
        print('@Isp: {}'.format(ip['isp']))
        print('@Org: {}'.format(ip['org']))
        print('@As: {}'.format(ip['as']))
        print('@Asname: {}'.format(ip['asname']))
        print('@Reverse: {}'.format(ip['reverse']))
        print('@Mobile: {}'.format(ip['mobile']))
        print('@Proxy: {}'.format(ip['proxy']))
        print('@Hospedagem: {}'.format(ip['hosting']))
        print('@Ip: {}'.format(ip['query']))
        print('━━━━━━━━━━━━━━━━━━━━━━━━━┛')

    else:
        print(f"erro in {x}")
