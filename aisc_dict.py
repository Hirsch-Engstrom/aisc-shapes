import csv
with open('ps_pack/AISC_Database_v14_1.csv','rU') as data:
	aiscfile = csv.DictReader(data, dialect='excel')
	aisc={}
	num = 0
	for row in aiscfile:
		k = row['AISC_Manual_Label']
		v = row
		aisc[k] = v
	for i in aisc:
		num += 1
		for j in aisc[i]:
			if j == 'AISC_Manual_Label':
				continue
			elif j == 'Type':
				continue
			elif j == 'T_F':
				continue
			else:
				try:
					aisc[i][j] = float(aisc[i][j])
					break
				except ValueError:
					print 'Error on row ', num 
						