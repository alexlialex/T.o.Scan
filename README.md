# T.o.Scan
T.o.Scan (aka 2Scan) aims to promote awareness of online safety and the legal consequences of consenting to a service's "Terms of Service" by providing users with shortened summaries with keywords, either through Chrome extension or webpage.

# Software Used
We set up a web scraper and webpage parser using Python's urllib which was hosted on a local server via Flask. Our Chrome Extension/Website utilized jQuery and Ajax to get the output from our python scripts.

# Issues we ran into 
Since none of us knew JavaScript, which was required for creating any sort of web application, our original goal was to write our program in Python and use a Python to JavaScript translator such as Transcypt to get our necessary files. However things didn't go as planned because urllib, which was the library we utilized to scrape/parse the html on the webpages, didn't have an equivalent in JavaScript. We ended up crash-coursing JavaScript and trying many many frameworks to get code to work. In the end we ended up using the Flask framework to establish a local server for our Python script and used it for our inputs in our JavaScript code.

We also had a tough time deciding which keywords to actually use to summarise the webpages. We ended up consuling mentors and reading articles online to determine that words that had legal implications, formatting, and keys that were determined to be important by our machine learning algorithm.

# Future of T.o.Scan
Extend functionality of our app, which currently only works with websites that put their ToS as .html files.
Implement natural language processing to create seamless and natural summaries.
Add some accessibility functions.

SD Hacks 2018
Alex Li, Michael Wu, Clarence Chen, Madeline Tjoa

