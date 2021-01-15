#Andrew Wiltberger PA3 
#Header Files
#Modules
import os

#Free Function Definitions

#CREAT DATABASSE <name>;
def createDatabase(m_line):
    dbName = m_line.split(" ")[2]#<name>;
    dbName = dbName.split(";")[0]#<name>
    try:
        os.mkdir(dbName)
        print("Database", dbName, "created.")
    except:
        print("!Failed to create database", dbName, "because is already exists.")
    return

#USE <name>;
def use(m_line):
    dbName = m_line.split(" ")[1]#<name>;
    dbName = dbName.split(";")[0]#<name>
    try:
        os.chdir(dbName)
        print("Using database %s." %dbName)
    except:
        try:
            os.chdir("..")  ##if we are using a diff databasse and need to go back one level
            os.chdir(dbName)
            print("Using database ../%s." %dbName)
        except:
            print("!Cannot access database %s." %dbName)
    return

#CREATE TABLE <Tablename> (<name> <type>,...);
def createTable(m_line):
    temp = m_line.split()[2]
    tableName = temp.split("(")[0]
    args = temp.split("(")[1]
    args += " "
    args += m_line.split()[3]
    args += " "
    args += m_line.split()[4]
    args += " "
    args += m_line.split()[5]
    args = args[:-2]
    args = args.replace(",", "")

    args = args.split()[0] + " " + args.split()[1] + " | " + args.split()[2] + " " + args.split()[3] 
    
    if not (os.path.exists(tableName)):
        fileName = open(tableName, "w")
        fileName.write(args)
        print("Table", tableName, "created.")
        fileName.close()
    else:
        print("!Failed to create table", tableName, "because it already exists.")
    return

#INSERT INTO
def insertIntoTable(m_line):
    tableName = m_line.split(" ")[2]
    paramaters = m_line.split(" ", 3)[3]
    paramaters = paramaters.split(";")[0].replace("\t", "").replace(" ", "").replace("'", "")
    if(paramaters.upper().split("(")[0] == "VALUES"):
        paramaters = paramaters.split("(")[1].replace(",", "|")
        paramaters = paramaters[:-1]
        if os.path.exists(tableName):
            fileName = open(tableName, "a+")
            fileName.write("\n%s" %paramaters)
            fileName.close()
            print("1 new record inserted.")
        else:
            print("!Failed to insert into table %s because it does not exist." %tableName)
    return

def joinStar(m_line):
    line = m_line.split(" ")
    tableName1 = line[3]    #Empolyee
    tableName2 = line[5]    #Sales
    arg1 = line[8]
    arg1 = arg1[2:]  #id
    arg2 = line[10]
    arg2 = arg2[2:]
    arg2 = arg2[:-1]   
    sign = line [9]

    with open(tableName1) as file1: 
        lineList1 = [line.rstrip() for line in file1]
    with open(tableName2) as file2: 
        lineList2 = [line.rstrip() for line in file2]


    table1Arg = lineList1[0]
    table2Arg = lineList2[0]
    print((table1Arg + " | " + table2Arg).replace("\n", ""))

    #will find the positions in each line 
    #where we will need to compare 
    pos1 = table1Arg.find(arg1)
    pos2 = table2Arg.find(arg2)
    #div by 3 bc table args are in sets of 3
    #ie int id | 
    if(pos1 > 0):
        pos1 = pos1/3
    if(pos2 > 0):
        pos2 = pos2/3


    #join
    for line1 in lineList1:
        for line2 in lineList2:
            if(line1.split("|")[pos1] == line2.split("|")[pos2]):
                print((line1 + "|" + line2).replace("\n", ""))


    return

def innerjoin(m_line):
    line = m_line.split(" ")
    tableName1 = line[2]
    tableName2 = line[6]
    arg1 = line[8]
    arg1 = arg1[2:]
    arg2 = line[10]
    arg2 = arg2[2:-1]


    with open(tableName1) as file1: 
        lineList1 = [line.rstrip() for line in file1]
    with open(tableName2) as file2: 
        lineList2 = [line.rstrip() for line in file2]

    table1Arg = lineList1[0]
    table2Arg = lineList2[0]
    print((table1Arg + " | " + table2Arg).replace("\n", ""))
    
    #will find the positions in each line 
    #where we will need to compare 
    pos1 = table1Arg.find(arg1)
    pos2 = table2Arg.find(arg2)
    #div by 3 bc table args are in sets of 3
    #ie int id | 
    if(pos1 > 0):
        pos1 = pos1/3
    if(pos2 > 0):
        pos2 = pos2/3

    #join
    for line1 in lineList1:
        for line2 in lineList2:
            if(line1.split("|")[pos1] == line2.split("|")[pos2]):
                print((line1 + "|" + line2).replace("\n", ""))



    return

def leftouterjoin(m_line):
    #print(m_line)
    line = m_line.split(" ")
    tableName1 = line[2]
    tableName2 = line[7]
    arg1 = line[9]
    arg1 = arg1[2:]
    arg2 = line[11]
    arg2 = arg2[2:-1]

    with open(tableName1) as file1: 
        lineList1 = [line.rstrip() for line in file1]
    with open(tableName2) as file2: 
        lineList2 = [line.rstrip() for line in file2]

    table1Arg = lineList1[0]
    table2Arg = lineList2[0]
    print((table1Arg + " | " + table2Arg).replace("\n", ""))

    pos1 = table1Arg.find(arg1)
    pos2 = table2Arg.find(arg2)
    if(pos1 > 0):
        pos1 = pos1/3
    if(pos2 > 0):
        pos2 = pos2/3

    lineList1.pop(0)
    lineList2.pop(0)
    for line1 in lineList1:
        flag = 0
        for line2 in lineList2:
            if(line1.split("|")[pos1] == line2.split("|")[pos2]):
                print((line1 + "|" + line2).replace("\n", ""))
                flag += 1
        if(flag == 0): #print lines in left with no matches in right
            print(line1+ "|")

    return
