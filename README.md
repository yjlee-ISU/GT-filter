# GT-filter
Filtering GT- or GP-reactive metabolites from METASPACE output using aldehyde, ketone, and lactone containing plant COCONUT ids.  
The details of this filtering is described in the associated manuscript submitted to J. Am. Soc. Mass Spectrom (citation will be updated once published). Example files are included used in the paper.

Included files.
1. GT-filter.py
   Python program.
2. GT_GP_lactone.txt
   First input file of this program, a list of GT/GP reactive metabolites generated from plant metabolites in COCONUT 2.0 database (https://coconut.naturalproducts.net/) using SMARTS search (OpenBabel.org) of [#6][CX3](=O)[#6] or [CX3H1](=O)[#6] for ketone or aldehyde functional groups, respectively, and C1(=O)OC1, C1(=O)OCC1, C1(=O)OCCC1, C1(=O)OCCCC1, and C1(=O)OCCCCC1 for alpha, beta, gamma, delta, and epsylon-lactone, respectively.
   One may generate similar GT/GP metabolite lists from other metabolite database using SMARTS search.
4. gta3removed.csv
  Second input file of the program, a METASPACE exported file for MSI dataset with GT or GP derivatization. The first two lines are removed so that it can be read as a dictionary file as well as false positive annotations from control.

Output files.
1. output_file1 = "gta3removed_filterout_lactone0.csv"
   METASPACE annotations that are filtered out as they do not have GT/GP reactive functional groups
2. output_file2 = "gta3removed_NoGT_lact0.csv"
   METASPACE annotations that are not modified. This is not our interest but for the information purpose.
3. output_file3 = "gta3removed_GTfiltered_lact0.tsv"
   METASPACE annotations that have GT/GP reactive functional groups. This is the main ouput file of our interest.
