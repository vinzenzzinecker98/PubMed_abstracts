

## PubMed_abstracts

simple script for integrating the abstracts (from txt file) into the csv file after exporting a PubMed search query.
Works best when files are in gdrive, simply copy code to google colab, adjust paths and run.

Important: The path data_Pubmedtxt must point to your "PubMed-[..]-set.txt", not "abstract-[...]-set.txt".

Output: csv file with appended column for abstracts

## Scopus Authoraffiliation

Script for generating a better representation of "authoraffiliation" in Scopus Search Exports
Transforms the String "Authors with affiliations" which is structured

`"Author1, ..., Institution1, ..., Country1;Author2, ..., Institution2, ..., Country2"`

into seperated Columns for Institution und Country, appended for each author
