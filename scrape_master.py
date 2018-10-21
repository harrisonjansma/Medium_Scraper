import os
from medium_scraper import *

#TO RUN THIS FILE YOU NEED SELENIUM, BEAUTIFULSOUP, PANDAS, DATETIME, REGEX, AND OS
#JUST GO TO THE COMMAND LINE AND
#SET WORKING DIRECTORY TO THE DIRECTORY WITH BOTH MEDIUM_SCRAPER.PY AND SCRAPE_MASTER.PY
#THEN ENTER COMMAND "$python scrape_master.py"


#ADD THE TAGS TO SCRAPE HERE
tags = ["data-science"]


#ADD THE DATES TO SCRAPE HERE
yearstart=2017
monthstart=10
yearstop=2018
monthstop=10

#LOOPS THROUGH ALL LISTED-TAGS AND SCRAPES DATA OFF OF MEDIUM/TAG/archive
#SAVES THE FILES TO /TAG_SCRAPES/ IN CSV FORMAT
for tag in tags:
    scrape_tag(tag, yearstart, monthstart, yearstop, monthstop)
    print("Done with tag: ", tag)
print("done")
