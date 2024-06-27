#Data import
import pandas as pd
import numpy  as np
metadata = pd.read_csv("/Users/priyaltripathi/Downloads/metadata.tsv", sep='\t')
metabolites = pd.read_csv("/Users/priyaltripathi/Downloads/mtb.tsv", sep ='\t')
genera_counts = pd.read_csv("/Users/priyaltripathi/Downloads/genera.counts.tsv",sep ='\t')
# relative_genera = pd.read_csv("/Users/priyaltripathi/Downloads/genera.tsv", sep = "\t")
# species_counts = pd.read_csv("/Users/priyaltripathi/Downloads/species.counts.tsv",sep ='\t')
# relative_species = pd.read_csv("/Users/priyaltripathi/Downloads/species.tsv", sep = "\t")

df = metadata.merge(metabolites, on="Sample")
mask1 = df['Study.Group'] == 'Gastrectomy'
df_metabolites = df[mask1]
# print(df_metabolites.shape[0])
df1 = metadata.merge(genera_counts, on = "Sample")
df_metagenome= df1[mask1]
# print(df_metagenome.shape[0])

# print(genera_counts.columns)
print(metadata.columns)
Columns = ['Lung cancer', 'Liver cancer', 'Breast cancer', 'Uterine cancer',
       'Other cancers', 'Stroke', 'Cardiac infarction', 'Angina',
       'Hypertension', 'Diabetes', 'Dyslipidemia', 'Cataract', 'Stomach ulcer',
       'Stomach polyps', 'Duodenal ulcers', 'Colorectal polyps',
       'Chronic hepatitis and liver cirrhosis', 'Gallstone',
       'Ureteral or kidney stones', 'Gout...46', 'Hip fracture',
       'Arm or wrist fracture', 'Femur base fractures', 'Other diseases']
for col in Columns:
    count = metadata[metadata[col]=='Yes'].shape[0]
    print(f"{col}: {count}")
    print()

#Highest is colorectal polyps