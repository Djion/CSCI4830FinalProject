from csv import DictReader, DictWriter
import re

def remove_urls (vTEXT):
	try:
		vTEXT = re.sub(r'(https|http)?:\/\/(\w|\.|\/|\?|\=|\&|\%)*\b', ' urlhere ', vTEXT, flags=re.MULTILINE)
		return(vTEXT)
	except Exception:
		return('BYTE LIKE ERROR')
def stringFormat(aString):
	
	aString = aString.replace("!","").replace("@","").replace("#","").replace("$","").replace("%","").replace("^","").replace("&","").replace("*","").replace("(","").replace(")","").replace("-","").replace("_","").replace("+","").replace("=","").replace("/","").replace("?","").replace(".","").replace(">","").replace(",","").replace("<","").replace(";","").replace(":","").replace("'","").replace("\\","").replace("|","").replace("}","").replace("]","").replace("{","").replace("[","").replace("~","").replace("`","").replace("\n","").replace('"','')
	aString = aString.lower()

	return aString

if __name__ == "__main__":
	'''
	with open('../raw_data/100k_Askreddit_100upvotes.csv', encoding='utf-8', errors='ignore') as data:
		readData = DictReader(data)
		for row in readData:
			row.pop('NUMBER', None)
			row['BODY'] = remove_urls(row['BODY'])
			row['BODY'] = stringFormat(row['BODY'])
			print(row)
	'''
	lines = [x for x in DictReader(open('../raw_data/100k_Askreddit_100upvotes.csv', encoding='utf-8', errors='ignore'))]
	#print(lines)
	with open('../raw_data/100k_upvotes_formatted.csv', 'w') as csvfile:
		fieldnames = ['SCORE', 'BODY']
		writer = DictWriter(csvfile, fieldnames=fieldnames)
		writer.writeheader()
		for row in lines:
			row.pop('NUMBER', None)
			row['BODY'] = remove_urls(row['BODY'])
			row['BODY'] = stringFormat(row['BODY'])
			writer.writerow(row)

	lines = [x for x in DictReader(open('../raw_data/100k_Askreddit_10downvotes.csv', encoding='utf-8', errors='ignore'))]
	with open('../raw_data/100k_downvotes_formatted.csv', 'w') as csvfile:
		fieldnames = ['SCORE', 'BODY']
		writer = DictWriter(csvfile, fieldnames=fieldnames)
		writer.writeheader()
		for row in lines:
			row.pop('NUMBER', None)
			row['BODY'] = remove_urls(row['BODY'])
			row['BODY'] = stringFormat(row['BODY'])
			writer.writerow(row)

