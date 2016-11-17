from csv import DictReader, DictWriter
import re

def remove_urls (vTEXT):
    vTEXT = re.sub(r'(https|http)?:\/\/(\w|\.|\/|\?|\=|\&|\%)*\b', ' urlhere ', vTEXT, flags=re.MULTILINE)
    return(vTEXT)
def stringFormat(aString):
	
	aString = aString.replace("!","").replace("@","").replace("#","").replace("$","").replace("%","").replace("^","").replace("&","").replace("*","").replace("(","").replace(")","").replace("-","").replace("_","").replace("+","").replace("=","").replace("/","").replace("?","").replace(".","").replace(">","").replace(",","").replace("<","").replace(";","").replace(":","").replace("'","").replace("\\","").replace("|","").replace("}","").replace("]","").replace("{","").replace("[","").replace("~","").replace("`","").replace("\n","").replace('"','')
	aString = aString.lower()

	return aString

if __name__ == "__main__":
	with open('100k_Pics_10downvotes.csv', encoding='utf-8', errors='ignore') as data:
		readData = DictReader(data)
		for row in readData:
			row.pop('NUMBER', None)
			row['BODY'] = remove_urls(row['BODY'])
			row['BODY'] = stringFormat(row['BODY'])
			print(row)

	

