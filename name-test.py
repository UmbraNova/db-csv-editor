import re

fake_names = '''
Carol	MacLeod
Chloe	Rees
Julian	Dickens
Max	Pullman
Jack	Newman
Harry	Hodges
Alexandra	Taylor
Austin	Oliver
Tim	Hudson
Brandon	Ferguson
Lauren	Davidson
Yvonne	Rees
Jack	King
Piers	Robertson
Jessica	Quinn
Kevin	Gill
Mary	Robertson
Sally	Murray
Ella	Rampling
Yvonne	Lewis'''.split(" ")[0]

fake_names = re.split("\t|\n", fake_names)[1:]
