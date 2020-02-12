import csv
#import querycsv
import os

#with open('WikiArt-Emotions-All.tsv') as tsvfile:
	# reader=csv.reader(tsvfile, delimiter='\t')
	# count = 0
	# headerDictionary = {}
	# for row in reader:
	# 	if(count == 0):
	# 		headers = row
	# 		for i in range(len(headers)):
	# 			headerDictionary[headers[i]] = i
	# 	count += 1

#happy art - we can select a random painting from the first 1/3 or so and then increment in facifier indices for each emotion
os.system("querycsv.py -i WikiArtEmotionsAllEdited.csv -o happyArt.csv \"select ImageURL, Title, Artist, Year, happy from WikiArtEmotionsAllEdited where CAST(happy AS float)>0.5 ORDER BY CAST(happy AS float) DESC;\"")
#sad art
os.system("querycsv.py -i WikiArtEmotionsAllEdited.csv -o sadArt.csv \"select ImageURL, Title, Artist, Year, sad from WikiArtEmotionsAllEdited where CAST(sad AS float)>0.5 ORDER BY CAST(sad AS float) DESC;\"")
#neutral art
os.system("querycsv.py -i WikiArtEmotionsAllEdited.csv -o neutralArt.csv \"select ImageURL, Title, Artist, Year, neutral from WikiArtEmotionsAllEdited where CAST(neutral AS float)>0.5 ORDER BY CAST(neutral AS float) DESC;\"")
#angry art
os.system("querycsv.py -i WikiArtEmotionsAllEdited.csv -o angryArt.csv \"select ImageURL, Title, Artist, Year, angry from WikiArtEmotionsAllEdited where CAST(angry AS float)>0.5 ORDER BY CAST(angry AS float) DESC;\"")
#surprised art
os.system("querycsv.py -i WikiArtEmotionsAllEdited.csv -o surprisedArt.csv \"select ImageURL, Title, Artist, Year, surprised from WikiArtEmotionsAllEdited where CAST(surprised AS float)>0.5 ORDER BY CAST(surprised AS float) DESC;\"")
#afraid art
os.system("querycsv.py -i WikiArtEmotionsAllEdited.csv -o afraidArt.csv \"select ImageURL, Title, Artist, Year, afraid from WikiArtEmotionsAllEdited where CAST(afraid AS float)>0.5 ORDER BY CAST(afraid AS float) DESC;\"")
#disgust art
os.system("querycsv.py -i WikiArtEmotionsAllEdited.csv -o disgustArt.csv \"select ImageURL, Title, Artist, Year, disgust from WikiArtEmotionsAllEdited where CAST(disgust AS float)>0.5 ORDER BY CAST(disgust AS float) DESC;\"")

file = open("emotions_temp.txt", "r")
emotions = []
for line in file: 
    print (line)
    emotions= line.split(',')
print (emotions)
#for emotion in emotions:

#os.system("querycsv.py -i WikiArtEmotionsAllEdited.csv -o output.csv \"select ID from WikiArtEmotionsAllEdited;\"")
#['ID', 'Style', 'Category', 'Artist', 'Title', 'Year', 'Image URL', 'Painting Info URL', 'Artist Info URL', 'Is painting', 'Face/body', 'Ave. art rating', 'Art (image+title): agreeableness', 'Art (image+title): anger', 'Art (image+title): anticipation', 'Art (image+title): arrogance', 'Art (image+title): disagreeableness', 'Art (image+title): disgust', 'Art (image+title): fear', 'Art (image+title): gratitude', 'Art (image+title): happiness', 'Art (image+title): humility', 'Art (image+title): love', 'Art (image+title): optimism', 'Art (image+title): pessimism', 'Art (image+title): regret', 'Art (image+title): sadness', 'Art (image+title): shame', 'Art (image+title): shyness', 'Art (image+title): surprise', 'Art (image+title): trust', 'Art (image+title): neutral', 'ImageOnly: agreeableness', 'ImageOnly: anger', 'ImageOnly: anticipation', 'ImageOnly: arrogance', 'ImageOnly: disagreeableness', 'ImageOnly: disgust', 'ImageOnly: fear', 'ImageOnly: gratitude', 'ImageOnly: happiness', 'ImageOnly: humility', 'ImageOnly: love', 'ImageOnly: optimism', 'ImageOnly: pessimism', 'ImageOnly: regret', 'ImageOnly: sadness', 'ImageOnly: shame', 'ImageOnly: shyness', 'ImageOnly: surprise', 'ImageOnly: trust', 'ImageOnly: neutral', 'TitleOnly: agreeableness', 'TitleOnly: anger', 'TitleOnly: anticipation', 'TitleOnly: arrogance', 'TitleOnly: disagreeableness', 'TitleOnly: disgust', 'TitleOnly: fear', 'TitleOnly: gratitude', 'TitleOnly: happiness', 'TitleOnly: humility', 'TitleOnly: love', 'TitleOnly: optimism', 'TitleOnly: pessimism', 'TitleOnly: regret', 'TitleOnly: sadness', 'TitleOnly: shame', 'TitleOnly: shyness', 'TitleOnly: surprise', 'TitleOnly: trust', 'TitleOnly: neutral']
	#	/Library/Frameworks/Python.framework/Versions/3.6/bin/querycsv.py -i WikiArtEmotionsAll.csv "select ID from WikiArtEmotionsAll;"