import os
import re

def convert(file, output):
    htmlHead = '<!DOCTYPE html>\n<html lang="en">\n<head>\n\t<meta charset="UTF-8">\n\t<meta http-equiv="X-UA-Compatible" content="IE=edge">\n\t<meta name="viewport" content="width=device-width, initial-scale=1.0">\n\t<title>Document</title>\n</head>\n<body>\n\t\n'
    htmlBody = "\n\t"
    htmlClosing = "</body>\n</html>"
    with open(file, 'r') as markdown:
        for line in markdown.readlines():
            if line.startswith("# "):
                htmlBody += f"\t<h1>{line.replace('# ','')}</h1>"

            elif line.startswith("#") and re.search('^#*\s', line):
                #TODO: allow hashtags elsewhere in the string
                headingType = line.count("#") if line.count("#") <=6 else 6
                headingContent = re.sub('^#*\s', '' ,line)
                htmlBody += f"\t<h{headingType}>{headingContent}</h{headingType}>\n"

            elif line.startswith("- "):
                lineContent = re.sub("^-\s",'',line)
                htmlBody += f"\t<ul><li>{lineContent}</li></ul>\n"

            else:
                htmlBody += f"\t<p>{line}</p>"

    with open(output, 'a+') as htmlFile:
        htmlFile.write(htmlHead+htmlBody+htmlClosing)

#TODO: finish checks for bold, italics, or other modifiers that have opening and closing sequences
def boldify(text):
    s=text
    for i,char in enumerate(s):
        occurence = 0
        if char=="*" and s[i+1]=="*":
            occurence += 1
            


if __name__ == '__main__':
    convert('testing/testing.md','output.html')