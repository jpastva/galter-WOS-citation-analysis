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