
def function(any_data_struct):
    return f'{any_data_struct} is a {type(any_data_struct)}'



a_lsit = [3,4,6,3,2]

a_tuple = (3,4,6,3,2)

a_set = {3,4,6,3,2}

a_dict = { "name": "Ratul", "country": "Bangladesh" }



print(function(a_lsit))
print(function(a_tuple))
print(function(a_set))
print(function(a_dict))


