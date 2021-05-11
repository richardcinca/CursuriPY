# nameList= ['ana','rick','mihai']
# new_nameList=[name.upper() for name in nameList]
# print(new_nameList)


# nums=[1,2,3,4,5,6,7,8,9,10]
# my_list=[numar for numar in nums if numar%2 == 0]
# print(my_list)
# SAU FOLOSIND LAMBDA
# my_list = filter(lambda n: n%2 ==0,nums)
# print(my_list)


# nums=[1,2,3,4,5,6,7,8,9,10]
# my_list=[f'{letter}{n}' for letter in 'abcd' for n in range(4) ]
# print(my_list)

names = ['Bruce', 'Clark', 'Peter']
heros = ['Batman','Superman','Spiderman']
my_dict={name:hero for name, hero in zip(names,heros) if name!='Peter'}
print(my_dict)