#Script for mapping genes to gastric cancer samples
import re
import pandas as pd
#Add commas between the sample characters content
with open('/Users/priyaltripathi/SIP(2023-24)/Sample_chars.txt', 'r') as file:
    samples_content = file.read()
elements = re.findall(r'"[^"]+"', samples_content)
comma_separated_string = ','.join(elements)
# with open('/Users/priyaltripathi/SIP(2023-24)/Sample_characteristics_processed.txt', 'w') as output_file:
    # output_file.write(comma_separated_string)

#Add commas between the sample IDs
with open('/Users/priyaltripathi/SIP(2023-24)/Sample_names.txt', 'r') as file:
    samples_num = file.read()
x = re.findall(r'"[^"]+"', samples_num)
comma_separated_str = ','.join(x)
# with open('/Users/priyaltripathi/SIP(2023-24)/Sample_IDs_processed.txt', 'w') as output_file:
    # output_file.write(comma_separated_str)

#Map sample characters to sample IDs
with open('/Users/priyaltripathi/SIP(2023-24)/Sample_IDs_processed.txt', 'r') as keys_file:
        keys_line = keys_file.readline().strip()
        keys = keys_line.split('","')
        keys[0] = keys[0].lstrip('"')
        keys[-1] = keys[-1].rstrip('"')

with open('/Users/priyaltripathi/SIP(2023-24)/Sample_characteristics_processed.txt', 'r') as values_file:
        values_line = values_file.readline().strip()
        values = values_line.split('","')
        values[0] = values[0].lstrip('"')
        values[-1] = values[-1].rstrip('"')
result_dict = dict(zip(keys, values))

df = pd.DataFrame(list(result_dict.items()), columns=['Sample_ID', 'Sample_Characteristics'])
df.to_csv('/Users/priyaltripathi/SIP(2023-24)/Sample_Characteristics.csv', index=False)


#Just ensuring that the values are properly mapped
# print(ordered_values)
# print(type(ordered_values))
# print(samples)
# print(result_dict['B99'])
# if samples in ordered_values:
#     print(f"ordered_values['{key}']: {ordered_values[key]}")
# else:
#     print(f"Key '{key}' not found in ordered_values")
# Assuming ordered_values is a list created from result_dict
# key = 'B99'

# if key in result_dict:
    # index = list(result_dict.keys()).index(key)
#     print(f"ordered_values[{index}]: {ordered_values[index]}")
# else:
#     print(f"Key '{key}' not found in result_dict")


