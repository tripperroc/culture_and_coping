import csv


def script():
	
	lang = [2,3,4] #2 for'en', 3 for 'tr' or 4 for 'ko'. These are columns from the csv file
	with open('Language - Sheet1.csv','rb') as file:
		
		line = csv.reader(file)
		fen = open('en.yml','w')
		ftr = open('tr.yml','w')
		fko = open('ko.yml','w')
		fen.write("en:\n")
		ftr.write("tr:\n")
		fko.write("ko:\n")
		for row in line:
			# in case of comments and excluding first row
			if(row[2] != None):
				if(row[1] != "Variable" ):
					#do nothing
					var = row[1]
					translation_en = row[lang[0]]
					translation_tr = row[lang[1]]
					translation_ko = row[lang[2]]
					text_en = "\t%s: \"%s\"\n" % (var,translation_en)
					text_tr = "\t%s: \"%s\"\n" % (var,translation_tr)
					text_ko = "\t%s: \"%s\"\n" % (var,translation_ko)
					fen.write(text_en)
					ftr.write(text_tr)
					fko.write(text_ko)
								
				
script()
