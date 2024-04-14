sample_dict = {'apple': 5, 'banana': 2, 'cherry': 8, 'date': 1}

sorted_dict_keys_asc = dict(sorted(sample_dict.items()))
print("Ascending order by keys:", sorted_dict_keys_asc)

sorted_dict_keys_desc = dict(sorted(sample_dict.items(), reverse=True))
print("Descending order by keys:", sorted_dict_keys_desc)




