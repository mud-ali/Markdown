import os
import re

global outputCount
outputCount = 0

def convert(file, output):
    global outputCount
    htmlHead = '<!DOCTYPE html>\n<html lang="en">\n<head>\n\t<meta charset="UTF-8">\n\t<meta http-equiv="X-UA-Compatible" content="IE=edge">\n\t<meta name="viewport" content="width=device-width, initial-scale=1.0">\n\t<title>Document</title>\n\t<link rel="stylesheet" href="md.css">\n</head>\n<body>\n\t\n'
    htmlBody = "\n"
    htmlClosing = "\n</body>\n</html>"
    with open(file, 'r') as markdown:
        for line in markdown.readlines():
            

            if "**" in line:
                line= boldify(line)

            if line.startswith("# "):
                h1Cont = line.replace('# ','').replace('\n','')
                htmlBody += f"\t<h1>{h1Cont}</h1>\n"

            elif line.startswith("#") and re.search('^#*\s', line):
                #TODO: allow hashtags elsewhere in the string
                headingType = line.count("#") if line.count("#") <=6 else 6
                headingContent = re.sub('^#*\s', '' ,line).replace('\n','')
                htmlBody += f"\t<h{headingType}>{headingContent}</h{headingType}>\n"

            elif line.startswith("- "):
                lineContent = re.sub("^-\s",'',line).replace('\n','')
                htmlBody += f"\t<ul>\n\t\t<li>{lineContent}</li>\n\t</ul>\n"

            elif not line.isspace():
                line = line.replace("\n",'')
                htmlBody += f"\t<p>{line}</p>\n"

            
                
    htmlBody = cleanLists(htmlBody)
    with open("output/"+output+str(outputCount)+".html", 'a+') as htmlFile:
        outputCount += 1
        with open("tmp/outputCount","w") as outputCounter:
            outputCounter.write(str(outputCount))
        htmlFile.write(htmlHead+htmlBody+htmlClosing)

def cleanLists(html):
    return html.replace("</ul>\n\t<ul>","\t").replace("/li>\n\t\t\n<li",'/li>\n\t\t<li')

def boldify(text):
    s=text
    print(s)
    results = re.findall('\*\*.*?\*\*', s)
    for res in results:
        s = s.replace(res, "\t<b>"+res.replace("**",'')+"</b>\n")
    return s

#add similar functions for italics, etc.            


if __name__ == '__main__':
    outputCount = int(open("tmp/outputCount").read())
    convert('testing/testing.md','output')