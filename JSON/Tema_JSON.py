import json


description = ('Country', ['2011 ', '2012 ', '2013 ', '2014 ', '2015 ', '2016 ', '2017', '2018 ', '2019 '])
dataset = [
('AL', [': ', ': ', ': ', ': ', ': ', ': ', ': ', '84 ', ':']),
('AT', ['75 ', '79 ', '81 ', '81 ', '82 ', '85 ', '89 ', '89 ', '90 ']),
('BA', [': ', ': ', ': ', ': ', ': ', ': ', ': ', '69 ', '72 ']),
('BE', ['77 ', '78 ', '80 ', '83 ', '82 ', '85 ', '86 ', '87 ', '90 ']),
('BG', ['45 ', '51 ', '54 ', '57', '59 ', '64 ', '67 ', '72 ', '75 ']),
('CH', [': ', ': ', ': ', '91 ', ': ', ': ', '93 b', ': ', '96 ']),
('CY', ['57 ', '62 ', '65 ', '69 ', '71 ', '74 ', '79 ','86 ', '90 ']),
('CZ', ['67 ', '73 ', '73 ', '78 ', '79 ', '82 ', '83 ','86 ', '87 ']),
('DE', ['83 ', '85 ', '88 ', '89 ', '90 ', '92 ', '93 ','94 ', '95 ']),
('DK', ['90 ', '92 ', '93 ', '93 ', '92 ', '94 ', '97 ','93 ', '95 ']),
('EA', ['74 ', '76 ', '79 ', '81 ', '83 ', '85 ', '87 ','89 ', '90 ']),
('EE', ['69 ', '74 ', '79 ', '83 ', '88 ', '86 ', '88 ','90 ', '90 ']),
('EL', ['50 ', '54 ', '56 ', '66 ', '68 ', '69 ', '71 ','76 ', '79 ']),
('ES', ['63 ', '67 ', '70 ', '74 ', '79 ', '82 ', '83 ','86 ', '91 ']),
('FI', ['84 ', '87 ', '89 ', '90 ', '90 ', '92 ', '94 ','94 ', '94 ']),
('FR', ['76 ', '80 ', '82 ', '83 ', '83 ', '86 ', '86 ','89 ', '90 ']),
('HR', ['61 ', '66 ', '65 ', '68 ', '77 ', '77 ', '76 ','82 ', '81 ']),
('HU', ['63 ', '67 ', '70 ', '73 ', '76 ', '79 ', '82 ','83 ', '86 ']),
('IE', ['78 ', '81 ', '82 ', '82 ', '85 ', '87 ', '88 ','89 ', '91 ']),
('IS', ['93 ', '95 ', '96 ', '96 ', ': ', ': ', '98 ', '99', '98 ']),
('IT', ['62 ', '63 ', '69 ', '73 ', '75 ', '79 ', '81 ','84 ', '85 ']),
('LT', ['60 ', '60 ', '65 ', '66 ', '68 ', '72 ', '75 ','78 ', '82 ']),
('LU', ['91 ', '93 ', '94 ', '96 ', '97 ', '97 ', '97 ','93 b', '95 ']),
('LV', ['64 ', '69 ', '72 ', '73 ', '76 ', '77 b', '79 ','82 ', '85 ']),
('ME', [': ', '55 ', ': ', ': ', ': ', ': ', '71 ', '72 ','74 ']),
('MK', [': ', '58 ', '65 ', '68 ', '69 ', '75 ', '74 ', '79', '82 ']),
('MT', ['75 ', '77 ', '78 ', '80 ', '81 ', '81 ', '85 ','84 ', '86 ']),
('NL', ['94 ', '94 ', '95 ', '96 ', '96 ', '97 ', '98 ','98 ', '98 ']),
('NO', ['92 ', '93 ', '94 ', '93 ', '97 ', '97 ', '97 ','96 ', '98 ']),
('PL', ['67 ', '70 ', '72 ', '75 ', '76 ', '80 ', '82 ','84 ', '87 ']),
('PT', ['58 ', '61 ', '62 ', '65 ', '70 ', '74 ', '77 ','79 ', '81 ']),
('RO', ['47 ', '54 ', '58 ', '61 b', '68 ', '72 ', '76 ','81 ', '84 ']),
('RS', [': ', ': ', ': ', ': ', '64 ', ': ', '68 ', '73 ','80 ']),
('SE', ['91 ', '92 ', '93 ', '90 ', '91 ', '94 b', '95 ','93 ', '96 ']),
('SI', ['73 ','74 ', '76 ', '77 ', '78 ', '78 ', '82 ','87 ', '89 ']),
('SK', ['71 ', '75 ', '78 ', '78 ', '79 ', '81 ', '81 ','81 ', '82 ']),
('TR', [': ', '47 ', '49 ', '60 ', '70 ', '76 ', '81 ', '84', '88 ']),
('UK', ['83 ', '87 ', '88 ', '90 ', '91 ','93 ', '94 ','95 ', '96 ']),
('XK', [': ', ': ', ': ', ': ', ': ', ': ', '89 ', '93 ','93 ']),
]

 # Description Cleaner
years=description[1]
for i in range(len(years)):
    years[i]=years[i][:4]
# print(description)


# Dataset Cleaner


for line in dataset:
    values=line[1]
    for i in range(len(values)):
        values[i]=values[i].replace(" ","")
        for element in range(len(values[i])):
            # print(values[i][element])
            if values[i][element].isnumeric() is not True:
                to_remove=values[i][element]
                # print(values[i], '-> ', to_remove )
        # print(values[i], to_remove)
        values[i]=values[i].replace(to_remove,"")
    for count,value in enumerate(values):
        if value=="":
            values[count]=0
        else:
            values[count]=int(values[count])

# for line in dataset:
#     print(line)

###########################################################################################################

def get_year(dataset: list, anul: str) -> dict or str:
    try:
        index = ''
        years = description[1]
        # print(years)
        for i in range(len(years)):
            if years[i][:3] == anul[:3]:
                index = i
        lista = []
        for line in dataset:
            country=line[0]
            value=line[1]
            test=(country,value[index])
            lista.append(test)
        dictionar={}
       # print(lista)
        key = anul
        dictionar.setdefault(anul, lista)
        # print(dictionar)
        json_dict=json.dumps(dictionar,indent=3)
        return dictionar
    except UnboundLocalError:
        error = "Please check if the year argument is between 2011-2019 "
        return error



###########################################################################################################

def get_country(dataset:list,country:str)-> dict:
    years = description[1]
    reversed = []
    for i in range(len(years) - 1, -1, -1):
        reversed.append(years[i])
    # print(reversed)
    reversed_values=[]
    for line in dataset:
        # print(line)
        if line[0] == country:
            values = line[1]
            # print(values)
            for var in range(len(values) - 1, -1, -1):
                reversed_values.append(values[var])
    dictionar_value=list(zip(reversed,reversed_values))
    dictionar = {}
    # print(lista)
    key = country
    dictionar.setdefault(country, dictionar_value)
    # print(dictionar)
    json_dict = json.dumps(dictionar, indent=3)
    return dictionar
    # return dictionar_value



###########################################################################################################

def get_average(dataset, country):

    for line in dataset:
        if line[0]==country:
            values=line[1]
            sum=0
            count=0
            for item in values:
                if item != 0:
                    sum+=item
                    count+=1
            average=sum/count
            return average



###########################################################################################################

def json_test(dataset, country):
    for line in dataset:
        if country == line[0]:
            empty_list = []
            years = description[1]
            # print(years)
            values = line[1]
            # print(values)

            key1 = []
            key2 = []
            test = []
            for i in range(len(years)):
                key1.append("Year")
                key2.append("Coverage")

                dictionary1 = dict(zip(key1, years))
                dictionary2 = dict(zip(key2, values))
                dictionary3 = dict(dictionary1, **dictionary2)

                test.append(dictionary3)
            reversed=[]
            for item in range(len(test) - 1, -1, -1):
                reversed.append(test[item])

            reversed={country:reversed}
            json_dict = json.dumps(reversed, indent=3)

            return json_dict

###########################################################################################################


# print(get_year(dataset, "2011"))
# print(get_country(dataset,'RO'))
# print("Average:  ",get_average(dataset,'AT'))
print(json_test(dataset,'RO'))
