#1.Check the data type of all your variables using type() built-in function
#2.Using the len() built-in function, find the length of your first name
#3.Compare the length of your first name and your last name
#1.
print(type('Mahiraj'))                                          # str
print(type('first_name'))                                         # str
print(type(10))                                                 # int
print(type(3.14))                                               # float
print(type(1 + 1j))                                             # complex
print(type(True))                                               # bool
print(type([1, 2, 3, 4]))                                       # list
print(type({'name':'Mahiraj','age':18, 'is_married':False}))    # dict
print(type((1,2)))                                              # tuple
print(type(zip([1,2],[3,4])))                                   # set

#2.
print('First name:', 'Mahiraj')
print('First name length:', len('Mahiraj'))
print('Last name: ', "baghela" )
print('Last name length: ', len('first_name'))


