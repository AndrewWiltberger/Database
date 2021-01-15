#Andrew Wiltberger PA3
#Header Files
import sql
#Modules
import sys

#Free Function Definitions
#Read in each line and call sqll
def readLine(line):
	#Exit Function
	if(line.upper().find(".EXIT", 0, 5) != -1):
	
		exit("All Done.")
	#Comments and Empty Lines
	elif((line.find("--", 0, 2) != -1) or (len(line) < 2)):
		return
	#Everything Else/SQL sql
	#For new sql, just add onto the if-else statements and 
	#create it's appropriate function in sql.py
	else:
		if(line.upper().find("CREATE DATABASE ") != -1):#use
			sql.createDatabase(line)
		elif(line.upper().find("USE ") != -1): #use
			sql.use(line)
		elif(line.upper().find("CREATE TABLE ") != -1): #use
			sql.createTable(line)
		elif(line.upper().find("SELECT *") != -1 and line.upper().find("LEFT OUTER JOIN") != -1):
			sql.leftouterjoin(line)
		elif(line.upper().find("SELECT *") != -1 and line.upper().find("INNER JOIN") != -1):
			sql.innerjoin(line)
		elif(line.upper().find("SELECT *") != -1):
			sql.joinStar(line)
		elif((line.upper().find("INSERT ") != -1) and (line.upper().find(" INTO") != -1)):
			sql.insertIntoTable(line)
		else:
			print("!Invalid command found.")
	return

#Main Function
if __name__ == '__main__':
   
	if(len(sys.argv) < 2):
		exit("!No filename found.")
	sqlFile = open(str(sys.argv[1]), "r")#.read().splitlines()
	temp = ""
	line = ""
	lineList = sqlFile.readlines()
	flag = 0
	
	for line in lineList:
		#print(line)
		if( ((line.find("--", 0, 2) != -1) or (len(line) < 2)) and flag == 0):
			flag = 0
		elif((line.find(";") != -1) and flag == 0): 
			readLine(line)
			#print("called elif 1:" + temp)
		elif(flag == 2):
			temp += line
			flag = 0
			nlist = temp.splitlines()
			finalLine = nlist[0]
			finalLine += nlist[1]
			finalLine += nlist[2]
			#print("final Line:" + finalLine)
			readLine(finalLine)
			temp = ""
			#print("call elif 2")
		elif(flag == 3):
			temp += line
			flag = 2
			#print("elif 3")
		else:
			temp = line
			flag = 3
			#print("else")
	print("All Done.")




   