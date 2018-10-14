from flask import Flask, render_template, request, Response
import sys
import json
#from flask.ext.api import status
import urllib.request
#terms_of_service
terms_of_service_by_line = []  # .txt file of the ToS
line_nums_bolded = [] # line numbers of all the subheaders
subheaders = [] # list of all the subheaders
read_in_file_name = "websiteHTML.txt"
bold_tags = [ "<body>", "<strong>"] # list of html tags that indicate bolded text
bold_endtags = [ "</body>", "</strong>"]

app = Flask(__name__)

#@app.route('/')
#def index():
	#return render_template('index.html')

# FINISHED: input a website url and return a .txt file with the html stuff
def get_html(url):
  try:
    with urllib.request.urlopen(url) as response:
      html = response.read()
      file = open(read_in_file_name, "wb")
      file.write(html)
      file.close()
      return file
  except:
    print("not a url lol")


# FINISHED: returns file_name as a list of lines
def split_file(file_name):
    try:
        file = open(file_name, "r")
        lines = file.read().split("\n")
        for line in lines:
            terms_of_service_by_line.append(line)
        file.close()
    except:
        print("somethings wrong with the fileeee")


# FINISHED: finds all the bolded section headers within the ToS document
# returns a list containing the line #s of where the subheaders are
def find_section_header_locations(file_name):
    try:
        file = open(file_name, "r")
        line_number = 1
        for line in file:
            for tag in bold_tags:
                if line.startswith(tag):
                    line_nums_bolded.append(line_number)
                    #finds the bolded subheader on the current line number
                    temp_pos = bold_tags.index(tag)
                    subheaders.append( line[line.find(tag) + len(tag): line.find( bold_endtags[temp_pos] )])
                line_number = line_number + 1
                print("line_nums_bolded: ", line_nums_bolded)
        file.close()
    except:
        print("file broke")


# using preset keywords using ML or hardcoding
#def find_key_words(file_name):


# writes the summary using the bolded subheaders and the sentence containing keywords
# ONLY WRITES THE SUBHEADERS: TO FIX LATER
def write_summary():
    summary = ""
    for line_num in line_nums_bolded:
        summary = summary + (terms_of_service_by_line[line_num + 1])
    print("summary: " + summary)
    return summary


# the central processing method for the terms of service file
def process_website(url):
    try:
        terms_of_service = get_html(url)
        split_file(read_in_file_name) # add url param for get_html()
        find_section_header_locations(read_in_file_name)
        return write_summary()
    except:
        print("url not work")

#returns the file in string form
@app.route('/urlStuff', methods=['POST'])
def urlStuff():
    print(request.is_json, file = sys.stderr)
    content = request.get_json()

    print(content, file = sys.stderr)

    url_link = content["urllink"]
    htmldata = process_website(url_link)
    data = {'htmldata': htmldata}
    #data = json.stringify(data)
    print(url_link, file = sys.stderr)
    print(data, file = sys.stderr)
    return Response(data, status = 201, mimetype = 'application/json')

if __name__ == '__main__':
    app.run(debug=True)
