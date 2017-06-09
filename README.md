# Galter Library Web of Science citation analysis scripts

This page is intended to provide technical documentation for an ongoing citation analysis and collection development project at the Galter Health Sciences Library at Northwestern University's Feinberg School of Medicine. The scripts in this repository are designed to assist in performing basic citation analysis on cited references from citations exported from Web of Science (WOS). This project will be presented at the NASIG Annual Conference in June, 2017, after which slides will be made available.

## Getting started

It is assumed working files are in .txt format, exported from WOS as full records with cited references in tab-delimited (Win) format.


### System Requirements

These scripts should be run in a Python 3 environment.

### Basic instructions:

1. Run the WOS_clean_concat.py script, specifying the directory containing your WOS .txt files and the desired output directory. This will output .csv files corresponding to each .txt file, and a .pkl file for all of the data combined into one file.
2. Run the WOS_citation_analysis.py script using the output .pkl file.
3. OPTIONAL STEP: Add code snippet WOS_specific_journal.py to output publication year of a specific journal title(s). Must use WOS journal title abbreviation from MaxCitedJournals list, to be specified jn# ==. Expand code as needed to gather multiple titles at once.

### Outputs

The WOS_citation_analysis.py script will output several .csv data files and generate basic figures related to the analysis. Output file can be renamed per local conventions.

**Data**

- MaxCitedJournals.csv - List of most cited journals from the cited references list sorted by count. Modify p = cc.most_common() to specify number of journals desired in result
- OriginalArticle_Year_RefCount.csv - List giving publication year of citing (original) article and a count of the number of references cited by each article.
- CitedJournalAge.csv - List giving age of cited reference in years (in relation to publication date of citing article) and the publication year of the cited reference.
- ReferenceStats.csv - List giving the average number of references per article, per year, and the total number of cited references for each year.
- SpecificJournalYears.csv - Output if including code snippet from WOS_specific_journal.py. Returns year of cited references for all references to a specific journal title. Useful if interested in investigating library's coverage of a particular journal if heavily cited.

**Figures**

- Figure 1 - Number of articles published per year
- Figure 2 - Year of publication of cited reference articles
- Figure 3 - Age of cited articles (in years) compared to the date of publication of the citing article 
- Figure 4 - Total number of citations per year
- Figure 5 - Average number of citations per article, per year

## Working with abbreviated titles

The journal titles as extracted from the WOS citations are abbreviated, and as such so is the output when working with the files using Python. One option to automate the retrieval of full titles and ISSN information from the abbreviated titles is to utilize the NLM E-utilities API. This allows you to query the NLM catalog, retrieve matching catalog records when available, and output Title, ISSN, and other fields of your choosing to a file.

**Brief instructions for using NLM's E-utilities**


1. In a Unix terminal, install EDirect software (see instructions
[here](https://dataguide.nlm.nih.gov/edirect/install.html))
2. Place a list of the journal title abbreviations in your working directory as a .txt file (in this example, titles.txt). The results will be more accurate if each title is enclosed with quotation marks (").
3. Execute the following search in your Unix terminal:

```
while read -u 10 list; do esearch -db nlmcatalog -query "$list" | efetch -format xml | xtract -pattern NLMCatalogRecord -element TitleMain/Title MedlineTA TitleAlternate/Title ISSN; done 10< titles.txt > FullJournalTitles.txt

```

For further documentation about E-Utilities, visit the 
[NLM website](https://dataguide.nlm.nih.gov/)


## Authors 

These scripts were written by Madhuri Kaul, with specifications provided by Joelen Pastva.

## Project Team

Members of the citation analysis project team:

- Karen Gutzman
- Madhuri Kaul
- Ramune Kubilius
- Joelen Pastva
- Jonathan Shank


## License

This project is licensed under the MIT License.