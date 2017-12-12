import csv
import pdb


def left(s, amount = 1, substring = ""):
    if (substring == ""):
        return s[:amount]
    else:
        if (len(substring) > amount):
            substring = substring[:amount]
        return substring + s[:-amount]

with open('Question.csv', "rb") as f:
	reader = csv.reader(f,delimiter = ",")
	data = list(reader)
	row_count = len(data)

ID_Max = 0
ID_Temp = 0
for i in range(1,row_count):
	with open('Question.csv', "rb") as ifile:	
		rows = list(csv.reader(ifile))
		ID_Temp = rows[i][1]
		if int(ID_Temp) > int(ID_Max):
			ID_Max = ID_Temp
			#print str(ID_Max)

YNLinkLogic = str("")
for x in range(1, int(ID_Max) + 1):
	with open('Question.csv', "rb") as ifile:	
		rows = list(csv.reader(ifile))
		HText = rows[x][0]
		IntroText = rows[x][2]
		GText = rows[x][3]
		AStyle = rows[x][4]
		NextText = rows[x][5]
		IDtext = rows[x][1]
		NextQ = rows[x][8]
		if str(AStyle) == "YN":
			YLink = rows[x][9]
			NLink = rows[x][10]
		
		filename = str(x) + ".html"
		#print filename
		web = open(filename, "w")
		if len(str(GText)) < 3 and len(str(IntroText)) > 3:
			GText = IntroText
		if str(AStyle) == "SL":
				#Sets string for answer area
				AnSect = """<textarea ID="AnswerArea"></textarea><br>"""
		elif str(AStyle) == "YN": #and int(IDtext) == 6:
				AnSect = '<div id="YN" name="Form001">' + '<input type="radio" name="YN' + str(IDtext) + '"' + """' id="Yes""" + str(IDtext) + '" ' + """value="Yes" onclick='RadioSelect()'><label> Yes</label><br><br><input """ + 'type="radio" name="YN' + str(IDtext) + '"' + """ id="No""" + str(IDtext) + '" ' + """value="No" onclick='RadioSelect()'><label> No</label><br></div> """
				YNLinkLogic = """function RadioSelect() {
   
		        if(document.getElementById('Yes""" + str(IDtext) + """').checked) {
		            document.getElementById('RadioLink').href """ + ' = "' + YLink + """.html";
		        }
				if(document.getElementById('No""" + str(IDtext) + """').checked) {
		            document.getElementById('RadioLink').href = """ + '"' + NLink + """.html";
						}
					}
				"""
				NextButton = """<button type="submit" class="button"><a href=""" + '""' +""" id='RadioLink'>""" + NextText + "</a></button>"""
		elif str(AStyle) == "BB":
				AnSect = """<textarea ID="BigBox"></textarea><br>"""
		else:
				AnSect = ""
		TestQ = left(str(NextQ),2)
		if TestQ == "Ch":
			NextQ = str(int(IDtext) + 1)
		if str(AStyle) != "YN":
			NextButton = '<button type="submit" class="button"><a href="' + str(NextQ) + '.html"' + '>' + NextText + '</a></button>'
			print NextQ
		if int(IDtext) != 1:
			prevtext = '<a ID="prevtext" href="' + str(int(IDtext) - 1) + """.html">Previous</a>"""
		else:
			prevtext = """<a ID="prevtext" href="1.html">Previous</a>"""
		#print (str(len(GText)))anbe7
		if len(GText) < 3:
				GHTML = "<br>"
		else:
				GHTML = """<br> 
				<h2>""" + GText + """</h2>
				<br>"""
		#if int(IDtext) !=ID_Max:
		#	NextLink = 'formaction ="' + str(int(IDtext)+1) + """.html" """
		#else:
		#	NextLink = ' formaction="' + str(ID_Max) + """.html" """

		#data = urllib2.urlopen('https://besch84.github.io/import.css')

		#CSSText = '<link rel="stylesheet" type="text/css" href="http://cdn.rawgit.com/Besch84/Besch84.github.io/1de563a0/import.css">'
		txt = '<link href="https://cdn.rawgit.com/Besch84/Besch84.github.io/8ba19b52/import.css" rel="stylesheet" type="text/css">'
		HHTML = "<html>" + """<head>
  <meta charset="UTF-8">
  <title>Application Form</title>"""  + '\n' + txt + '\n'  + '\n' + '</head>' + """<h3>""" + str(IDtext) + """</h3><script>""" + YNLinkLogic + """</script>""" + '\n' + """<IMG STYLE="position:absolute; TOP:50px; LEFT:50px; WIDTH:150px; HEIGHT:150px" SRC="https://iviewplus.digital.nhs.uk/css/images/NHSDigitalLogo.svg"> """ + '\n' + """<hr width="100%" STYLE="position:absolute; top:220px">""" + '\n' + """<!--Breadcrumb Text-->""" + '\n' +  """<hr width="100%" STYLE="position:absolute; top:260px">""" + '\n' + "<body>" + '\n' + """<div style="position: absolute; TOP: 300px; left:100px">""" + "<h1>" + HText + "</h1>" + '\n' + "<br>" + '\n' + GHTML + '\n' + AnSect + '\n' + NextButton + "<br>" + prevtext + "</div>" + "</body>" +  '\n' + "</html>"
		#print HHTML
		web.write(HHTML)
		web.close()





ifile.close()