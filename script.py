import pandas as pd

#update all three paths
data_csv = "/content/drive/MyDrive/Path_to_csv.csv"
data_Pubmedtxt = "/content/drive/MyDrive/Path_To_txt/pubmed-xxxx-set.txt"
output = "/content/drive/MyDrive/PATH/out.csv"


df= pd.read_csv(data_csv, sep=",")
f = open(data_Pubmedtxt, "r")
abstractstring = f.read()
link = {}
df.dropna(subset=["DOI"])
for d in df["DOI"]:
  # find abstract
  position_doi = abstractstring.find(str(d))
  position_start = abstractstring.find("AB", position_doi) + 6
  position_next = abstractstring.find("PMID", position_doi)
  position_end = abstractstring.find(" - ", position_start ) - 3

  #make sure the abstract does not belong to the following entry:
  if position_next > position_start:
    abstract = abstractstring[position_start:position_end]
  else:
    abstract = "kein abstract gefunden"
  #clean string (remove multiple spaces!)
  abstract = ' '.join(abstract.split())

  #save in dict
  link[str(d)]= abstract

r = df["PMID"].count()
df["abstract"]=["kein abstract gefunden"]*r

#write abstracts in Dataframe
for index,row in df.iterrows():
  if str(row["DOI"]) in link:
    df["abstract"].iloc[index]=link[str(row["DOI"])]

#write to csv
df.to_csv(output)
print("done")

#preview
df
