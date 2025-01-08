import re

file_path = 'cq2opensource.sql'

with open(file_path, 'r', encoding='utf-8') as file:
    content = file.read()

line_pattern = re.compile(r'\((\d), (\d\d?), \'(<table.*)\'\);')
pattern = re.compile(r'(tBegin.*?tEnd)')

html_output = '<html>\n<head>\n<title>Extracted Tables</title>\n</head>\n<body>\n'

age_lookup_table = {
    1: "Age of Chaos",
    2: "Age of Recovery",
    3: "Age of Itherian",
    4: "Age of Rebirth",
    5: "Age of Resurgence",
    6: "Age of Conflict",
    7: "Age of Reinforcement",
    8: "Age of Transition"
}

lines = line_pattern.findall(content, re.M);
for line in lines:
    html_output += f'<h1>{age_lookup_table.get(int(line[0]), "Age unknown")} page {line[1]}</h1>\n'
    content = line[2].replace('\\r\\n','').replace('\\n','').replace('<? tBegin("','<br><h2>').replace('"); ?>','</h2>')
    html_output +=  content + '\n'       

html_output += '</body>\n</html>'

output_file_path = 'output.html'
with open(output_file_path, 'w') as output_file:
    output_file.write(html_output)

print(f'HTML file has been created successfully: {output_file_path}')