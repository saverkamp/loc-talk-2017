# mods2csv scripts

MODS XML can be difficult to work with, so these scripts allow you to harvest and parse MODS XML records as CSV files for a given collection from NYPL and Library of Congress.  

These scripts run on Python 2.7 and use the following third-party libraries:  
`lxml`  
`requests`  

The NYPL script requires a Digital Collections API key, which can be obtained at [http://api.repo.nypl.org/sign_up](http://api.repo.nypl.org/sign_up). Add this key to the `config.ini` file as the value of `token`.

To generate a CSV of items from an NYPL collection, run the `getNyplMods.py` script on the command line, including a collection uuid as a second argument (You can find the collection uuid at the bottom of the "About" tab of the left sidebar of any [Digital Collections collection page](https://digitalcollections.nypl.org/collections).):  

`>> python getNyplMods.py 5e789350-c5dc-012f-1163-58d385a7bc34`  

This should create a new CSV file in your directory with a file name that reflects the source library and the collection uuid (ex. "nypl5e789350-c5dc-012f-1163-58d385a7bc34.csv")  

To generate a CSV of items from a Library of Congress collection, run the `getLoCMods.py` script on the command line, including a collection slug from the digital collection URL as a second argument. (You can find this on any [Library of Congress digital collection page](https://www.loc.gov/collections/). NOTE that this script ONLY works with collections that have corresponding MODS records. Not all do! You can tell if a collection has MODS records if you click into an item page and see a link to "MODS Record" under "Additional Metadata Formats" near the bottom of the metadata details.):  

`>> python getLoCMods.py national-american-woman-suffrage-association`  

This should create a new CSV file in your directory with a file name that reflects the source library and the collection uuid (ex. "loc_national-american-woman-suffrage-association.csv")   

Sometimes you will see mostly blank rows in your output CSV file. This usually means that the XML was not well-formed and so the script was unable to parse it.