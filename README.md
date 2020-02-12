# EmotionProject

## to do
- get facifier in this repo to write to a text file with the emotions separated by commas
- make the facifier call the csv code
	- will likely involve downloading the csvquery code and using my modified version on my mac
	- need to create the csv files? or maybe it will just make them for me
- get the twitter generation/classification combo to work
- run simple html site that will be populated with the art, emotion detection & tweet

## Notes

When installing via pip csvquery you will have to go through the csvquery.py file it puts with python scripts to add parentheses to the print statements i.e. print pp(curs) -> print (pp(curs)) or else it won't compile and run the code for the queryImage.py
the other thing you'll need to fix is a inf.next() -> next(inf)
UnicodeDecodeError: 'charmap' codec can't decode byte 0x81 in position 6981: character maps to <undefined>
	you should then change 
		inf = csv.reader(open(infilename, "rt"), dialect)
		to
		inf = csv.reader(open(infilename, "rt", encoding="utf8"), dialect)
	It is an error for windows

Traceback (most recent call last):
  File "C:\Users\mocfowle\AppData\Local\Programs\Python\Python38\Scripts\querycsv.py", line 308, in <module>
    qcsv(csvfiles, outfile, file_db, keep_db, sqlcmd)
  File "C:\Users\mocfowle\AppData\Local\Programs\Python\Python38\Scripts\querycsv.py", line 215, in qcsv
    qsqldb( conn, sql_cmd, outfilename )
  File "C:\Users\mocfowle\AppData\Local\Programs\Python\Python38\Scripts\querycsv.py", line 179, in qsqldb
    csvout.writerow(headers)
TypeError: a bytes-like object is required, not 'str'

to solve the above error go a few lines above and change this line
	outfile = open(outfilename, "wb")
	to
	outfile = open(outfilename, "w")
