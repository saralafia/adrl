import html.parser

input_file = open('C:/Users/abruggma/Documents/_PhD/Santa_Barbara/ADRL/metadata_table_special_characters_resolved.txt', 'r', encoding="utf-8")
input_lines = input_file.read()
input_file.close()

print ("Inducing the HTML parsing method...")

h = html.parser.HTMLParser()

print ("Starting to parse the HTML-file...")

parsed_html = h.unescape(input_lines)
#print (parsed_html)


# It's important to include the "encoding = "utf-8"" statement at the end of the open statement. Otherwise there will be shown error messages. 

print ("Starting to write the output file...")

output_file = open('C:/Users/abruggma/Documents/_PhD/Santa_Barbara/ADRL/metadata_table_html_parsed.txt', 'w', encoding="utf-8")
output_file.write(parsed_html)
output_file.close()

print ("\n***HTML parsing: DONE***\n")