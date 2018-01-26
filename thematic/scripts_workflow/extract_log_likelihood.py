import re

input_file = open('C:/mallet/data_ucsb/adrl_hyper_par_ll.txt', 'r')
input_lines = input_file.readlines()
input_file.close()
output_file = open('C:/mallet/data_ucsb/adrl_hyper_par_extract_ll.txt', 'w')

output_file.write('topic_nr' + "\t" + 'LLT' + "\n")

for line in input_lines:
    if 'Mallet LDA: ' in line:
        #print line
        substitute_tags = re.sub(r'Mallet LDA\: ', '', line)
        substitute_tags = re.sub(r' topics.*', '', substitute_tags)
        substitute_tags = re.sub(r'\n', '', substitute_tags)
        print substitute_tags
        output_file.write(substitute_tags + "\t")
        
    elif '<1000>' in line:
        #print line
        substitute_tags = re.sub(r'\<1000\> LL/token\: ', '', line)
        print substitute_tags
        output_file.write(substitute_tags)

output_file.close()
        