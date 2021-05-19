# import numpy as np

# cnp=list(input('CNP:  '))
# print(cnp)

# KEY=list('279146358279')
# print(KEY)

# key_list=[]
# for i in range(0,12):
#     key_list.append(float(int(cnp[i])*int(KEY[i])))
# print(key_list)

# total=0
# for i in range (0,len(key_list)):
#     total=float(total+key_list[i])

# total_final=round(total%11)
# print(total_final)

# if total_final== 10:

# total_final=np.round(total_final,1)
# total_final=round(total_final%11)
# print(total_final)


# sex=cnp[0]
# print(sex)

# AA=cnp[1:3]
# print(AA)

# LL=cnp[3:5]
# print(LL)


# ZZ=cnp[5:7]
# print(ZZ)

# JJ=cnp[7:9]
# print(JJ)

# NNN=cnp[9:12]
# print(NNN)

# C=cnp[12]
# print(C)


# import pandas as pd
# judete=pd.read_csv('judete.csv',encoding="latin1")
# print(df)


import datetime
valoare_cnp = input('Introdu cnp-ul: ')
judete={
    
    '01':'Alba',
    '02':'Arad',
    '03':'Arges',
    '04':'Bacau',
    '05':'Bihor',

}

dictionar_judete = {'01': 'Alba',                    '02': 'Arad',                    '03': 'Arges',                    '04': 'Bacau',                    '05': 'Bihor',                    '06': 'Bistrita Nasaud',                    '07': 'Botosani',                    '08': 'Brasov',                    '09': 'Braila',                    '10': 'Buzau',                    '11': 'Caras Severin',                    '12': 'Cluj',                    '13': 'Constanta',                    '14': 'Covasna',                    '15': 'Dambovita',                    '16': 'Dolj',                    '17': 'Galati',                    '18': 'Gorj',                    '19': 'Hargita',                    '20': 'Hunedoara',                    '21': 'Ialomnia',                    '22': 'Iasi',                    '23': 'Ilfov',                    '24': 'Maramures',                    '25': 'Mehedinti',                    '26': 'Mures',                    '27': 'Neamt',                    '28': 'Olt',                    '29': 'Prahova',                    '30': 'Satu Mare',                    '31': 'Salaj',                    '32': 'Sibiu',                    '33': 'Suceava',                    '34': 'Teleorman',                    '35': 'Timis',                    '36': 'Tulcea',                    '37': 'Vaslui',                    '38': 'Valcea',                    '39': 'Vrancea',                    '40': 'Bucuresti',                    '41': 'Bucuresti - Sector 1',                    '42': 'Bucuresti - Sector 2',                    '43': 'Bucuresti - Sector 3',                    '44': 'Bucuresti - Sector 4',                    '45': 'Bucuresti - Sector 5',                    '46': 'Bucuresti - Sector 6',                    '51': 'Calarasi',                    '52': 'Giurgiu',                    }

cnp_jj=valoare_cnp[7:9]



# print(valoare_cnp[0])

if len(valoare_cnp) == 13:
    an = valoare_cnp[1:3]
    luna = int(valoare_cnp[3:5])
    zi = int(valoare_cnp[5:7])
    sex = int(valoare_cnp[0])
    if sex == 9:
        print('Persoana straina')
    else:
        try:
            data_de_comparat = datetime.datetime(int(f"19{an}"), luna, zi)
            data_18 = datetime.datetime(int(f"18{an}"), luna, zi)
            data_20 = datetime.datetime(int(f"20{an}"), luna, zi)

            # print(data_de_comparat)
            # print(type(data_de_comparat))

            if sex == 1 and datetime.datetime(1900, 1, 1) < data_de_comparat < datetime.datetime(1999, 12, 31):
                print("Sex barbatesc nascut in intervalul 1900 - 1999")

            elif sex == 2 and datetime.datetime(1900, 1, 1) < data_de_comparat < datetime.datetime(1999, 12, 31):
                print("Sex femeiesc nascut in intervalul 1900 - 1999")

            elif sex == 3 and datetime.datetime(1800, 1, 1) < data_18 < datetime.datetime(1899, 12, 31):
                print("Sex barbatesc nascut in intervalul 1800 - 1899") 
            
            elif sex == 4 and datetime.datetime(1800, 1, 1) < data_18 < datetime.datetime(1899, 12, 31):
                print("Sex femeiesc nascut in intervalul 1800 - 1899") 

            elif sex == 5 and datetime.datetime(2000, 1, 1) < data_20 < datetime.datetime(2099, 12, 31):
                print("Sex barbatesc nascut in intervalul 2000 - 2099") 
            
            elif sex == 6 and datetime.datetime(2000, 1, 1) < data_20 < datetime.datetime(2099, 12, 31):
                print("Sex femeiesc nascut in intervalul 2000 - 2099")     

            elif sex == 7:
                print("Persoane de sex barbatesc, rezidente in Romania")
            
            elif sex == 8:
                print("Persoane de sex femeiesc, rezidente in Romania")
            
            else:
                print("Sex Invalid")
                




            # if sex in [1, 3, 5, 7]:
                # print("Sex barbatesc")
            # else:
            #     print("Sex femeiesc")
        except ValueError:
            print("Data nu este valida")

        # J J 
        if cnp_jj in dictionar_judete.keys():
            print(dictionar_judete.get(cnp_jj))
        else:
            print('Judet invalid')

        # N N N
        NNN=valoare_cnp[9:12]
        # print(NNN)

        if NNN == '000':
            print('Interval invalid')
        
        KEY=list('279146358279')
        # print(KEY)

        key_list=[]
        for i in range(0,12):
            key_list.append(float(int(valoare_cnp[i])*int(KEY[i])))
        # print(key_list)

        total=0
        for i in range (0,len(key_list)):
            total=float(total+key_list[i])

        total_final=round(total%11)
        # print(type(total_final))
        # print(type(valoare_cnp[-1]))

        if total_final != int(valoare_cnp[-1]):
            print('invalid')


   
else:   
    print("CNP incomplet")



