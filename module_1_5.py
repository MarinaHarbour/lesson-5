immutable_var = 96,8,"new",[5,6]
print(immutable_var)
#immutable_var[0]=97 TypeError: 'tuple' object does not support item assignment
mutable_list=[3,8],[6,9]
mutable_list[1][0]=7
print(mutable_list)