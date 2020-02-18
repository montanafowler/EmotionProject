# EmotionProject

There were three products of our EmotionProject based on the input of a person's face with their emotion.

For our emotion detection we used this facifier project: https://github.com/rionaldichandraseta/facifier
We used the Wiki Art Emotion Database to return the art associated with the detected emotion
We generated tweets using a GPT-2 Model trained on a Thoughts of a Dog twitter account.
We used Flask to run the python server and have our web browser

slides: https://docs.google.com/presentation/d/1INWKxh70ifuw8dK-9JXeYtGtZ0BT_JJt--kexAVEr7E/edit?usp=sharing




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
