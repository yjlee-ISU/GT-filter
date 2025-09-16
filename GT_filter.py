# GT reactive functional group (aldehyde, carbonyl, lactone) filtering for METASPCAE csv output 
# from the list of COCONUT 2.0 database containing the functional group.
# NOTE: remove the first two lines in METASPACE output
#
# Young Jin Lee, Jun 18, 2025
# 

def input_data1(file1):         # Read GT reactive plant_coconut ids
    gt = []

    with open(file1,'r', newline='') as infile:
        for x in infile:
            xx = x.split(".")
            gt.append(xx[0])
    return gt

# Main

import sys
import math
import csv

csv.field_size_limit(2147483647)

coconut, db, tsv, plant_id, thismol, i = {}, [], [], [], [], 0

# Modify the following file names as needed

input_file1 = "GT_GP_lactone.txt"   # GT-, GP-reactive Conconut 2.0 IDs including lactones
input_file2 = "gta3removed.csv"     # METASPACE output after removing first two lines
output_file1 = "gta3removed_filterout_lactone0.csv"     # METASPACE annotations not having GT-, GP-reactive functional groups
output_file2 = "gta3removed_NoGT_lact0.csv"             # METASPACE annotations that are not modified
output_file3 = "gta3removed_GTfiltered_lact0.tsv"       # METASPACE annotations that have GT-, GP-reactive functional groups

GT_mass = 114.1031
GP_mass = 134.0718
m_mod = GT_mass     # Change to GP-mass for Girard's reagent P

GT_list = input_data1(input_file1)
print(GT_list)

GT_filtered = []
GT_filteredOut = []
No_GT = []
with open(input_file2,'r', encoding='utf-8-sig',newline='') as infile:
    reader = csv.DictReader(infile)
    for row in reader:
        formula = row.get("formula")
        mz = row.get("mz")
        mz0 = float(mz)
        fdr = row.get("fdr")
        ion = row.get("ion")
        id = row.get("moleculeIds")
        ids = id.split(", ")
        count0 = len(ids)
        name = row.get("moleculeNames")
        names = name.split(", ")
        chemMod = row.get("chemMod")
        new_id = []
        new_name = []
        tag = False
        print(ids)
        count = 0
        if chemMod != "":
            for id0 in ids:            
                if id0 in GT_list:
                    new_id.append(id0)
                    new_name.append(names[ids.index(id0)])
                    tag = True
                    count += 1
            if tag == True:
                new_id0 = ""
                new_id0 += ','.join(new_id)
                new_name0 = ""
                new_name0 += ','.join(new_name)
                GT_filtered.append([formula,mz0-m_mod,ion,mz,fdr,id,name,count0,new_id0,new_name0,count])
            else:
                GT_filteredOut.append(row)
        else:
            No_GT.append(row)

# save files

fieldnames = ['formula','Underivatized m/z','ion formula','Derivatized m/z','FDR','Molecules','Molecular Names','# of molecules','Filtered Molecules','Filtered Names','# of filtered']

with open(output_file3, "w", newline='') as outfile:
    file_writer = csv.writer(outfile,delimiter='\t') 
    file_writer.writerow(fieldnames)
    for line in GT_filtered:
        file_writer.writerow(line)

fieldnames = ["group","datasetName","datasetId","formula","adduct","chemMod","ion","mz","msm","fdr","rhoSpatial","rhoSpectral","rhoChaos","moleculeNames","moleculeIds","minIntensity","maxIntensity","totalIntensity","isomers","isobars","offSample","rawOffSampleProb","isobarIons"]
with open(output_file1, "w", newline ='') as outfile:
    file_writer = csv.DictWriter(outfile, fieldnames=fieldnames)
    file_writer.writeheader()
    file_writer.writerows(GT_filteredOut)

with open(output_file2, "w", newline ='') as outfile:
    file_writer = csv.DictWriter(outfile, fieldnames=fieldnames)
    file_writer.writeheader()
    file_writer.writerows(No_GT)
