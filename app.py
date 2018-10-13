from flask import Flask, render_template, request, stringify
import urllib.request
#terms_of_service
terms_of_service_by_line = []  # .txt file of the ToS
line_nums_bolded = [] # line numbers of all the subheaders
subheaders = [] # list of all the subheaders
read_in_file_name = "websiteHTML.txt"
write_to_file_name = "summary.html "
bold_tags = [ "<body>", "<strong>"] # list of html tags that indicate bolded text
bold_endtags = [ "</body>", "</strong>"]

app = Flask(__name__)

#@app.route('/')
#def index():
	#return render_template('index.html')

@app.route('/urlStuff/', methods=['POST'])
def urlStuff():
    url_link = request.form.get("urllink")
    htmldata = process_website(url_link)
    data = {'htmldata':htmldata}
    data = stringify(data)
    return data

if __name__ == '__main__':
    app.run(debug=True)

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



# the central processing method for the terms of service file
def process_website(url):
  terms_of_service = get_html(url)
  split_file(file_name) # add url param for get_html()
  find_section_header_locations(file_name)
  write_summary(write_to_file_name)
  return open(write_to_file_name, "").read()


# FINISHED: returns file_name as a list of lines
def split_file(file_name):
  file = open(file_name, "r")
  lines = file.read().split("\n")
  for line in lines:
    terms_of_service_by_line.append(line)
  file.close()


# FINISHED: finds all the bolded section headers within the ToS document
# returns a list containing the line #s of where the subheaders are
def find_section_header_locations(file_name):
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
    file.close()


# using preset keywords using ML or hardcoding
#def find_key_words(file_name):


# writes the summary using the bolded subheaders and the sentence containing keywords
# ONLY WRITES THE SUBHEADERS: TO FIX LATER
def write_summary(file_name):
    output_file = open(file_name, "w")
    for line_num in line_nums_bolded:
        line = terms_of_service_by_line[line_num + 1]
        output_file.write(line + "\n")
    output_file.close()
