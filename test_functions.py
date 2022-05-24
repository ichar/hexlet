import os
from functions import get_function

os.environ['FUNCTION_VERSION']='fail1'

get = get_function()

# BEGIN (write your solution here)
hash = {
    'name' : 'karo',
    'login' : 'mkaro',
    'email' : 'something',
    'empty' : '' 
}
for key, value in (('name', 'karo'),('email', 'something'),('address', '...'),('empty', '')):
    x = get(hash, key, None)
    msg = f"error:{os.environ['FUNCTION_VERSION']}:with key {key}: {x}|{value}"
    
    #print('-->',os.environ['FUNCTION_VERSION'], key, msg)
    if x != value or x is None:
        raise Exception(msg)
# END
