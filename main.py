def AddStudentDetails():  
  import os
  StudentName=str(input("Enter student name: "))
  valid="False"
  while valid=="False":
    valid="True"
    for x in range (len(StudentName)):
      if StudentName[x].lower()<"a" or StudentName[x].lower()>"z":
        valid="False"
        StudentName=str(input("Error, please re-enter student name: "))
        break
  StudentCode=str(input("Enter 4-digit candidate number of student: "))
  valid="False"
  while valid=="False":
    valid="True"
    file=open("Student.txt","r")
    line=file.readline()
    while line!="":
      if line[:4]==StudentCode:
        valid="False"
        break
      line=file.readline()
    file.close()
    if StudentCode<"0000" or StudentCode>"9999" or len(StudentCode)!=4:
      valid="False"
    if valid!="True":
      StudentCode=str(input("Error, please re-enter candidate number: "))
    

  file=open("Student.txt","a")
  line=StudentCode+"_"+StudentName
  if os.path.getsize("Student.txt")==0:
    file.write(line)
  else:
    file.write("\n")
    file.write(line)
  file.close()
  MockMarks=str(input("Enter mock marks, out of 75, of student (only two-digits): "))
  while MockMarks<"00" or MockMarks>"75" or len(MockMarks)!=2 :
    MockMarks=str(input("Error, please re-enter mock marks: "))
  PreMockMarks=str(input("Enter premock marks, out of 75, of student (only two-digits): "))
  while PreMockMarks<"00" or PreMockMarks>"75" or len(PreMockMarks)!=2:
    PreMockMarks=str(input("Error, please re-enter premock marks: "))
  ClassMarks=str(input("Enter class assessment marks, out of 50, of student ((only two-digits): "))
  while ClassMarks<"00" or ClassMarks>"50" or len(ClassMarks)!=2:
    ClassMarks=str(input("Error, please re-enter class assessment marks: "))
  file=open("Grades.txt","a")
  line=StudentCode+"_"+MockMarks+"_"+PreMockMarks+"_"+ClassMarks
  if os.path.getsize("Grades.txt")==0:
    file.write(line)
  else:
    file.write("\n")
    file.write(line)
  file.close()
  EvidenceForM=str(input("Enter Y/N whether a scan of the answer script has been provided for the mock: "))
  while EvidenceForM!="Y" and EvidenceForM!="N":
    EvidenceForM=str(input("Error, please only enter Y for yes, or N for no: "))
  EvidenceForPM=str(input("Enter Y/N whether a scan of the answer script has been provided for the premock: "))
  while EvidenceForPM!="Y" and EvidenceForPM!="N":
    EvidenceForPM=str(input("Error, please only enter Y for yes, or N for no: "))
  EvidenceForCM=str(input("Enter Y/N whether a scan of the answer script has been provided for the class assessment: "))
  while EvidenceForCM!="Y" and EvidenceForCM!="N":
    EvidenceForCM=str(input("Error, please only enter Y for yes, or N for no: "))
  file=open("Evidence.txt","a")
  line=str(StudentCode)+"_"+EvidenceForM+"_"+EvidenceForPM+"_"+EvidenceForCM
  if os.path.getsize("Evidence.txt")==0:
    file.write(line)
  else:
    file.write("\n")
    file.write(line)
  file.close()
def FindStudentCode(Name):
  file=open("Student.txt","r")
  Flag="False"
  line=file.readline()
  while line!="":
    if line[5:5+len(Name)]==Name:
      CandidateNum=line[:4]
      Flag="True"
      return CandidateNum
      break
    line=file.readline()
  if Flag=="False":
    return Flag
  file.close()  
def GiveGrade(Number):
  file=open("Grades.txt","r")
  line=file.readline()
  while line!="":
    if line[:4]==Number:
      marks=int(line[5:7])+int(line[8:10])+int(line[11:13])
      percentage=(marks/200)*100
      break
    line=file.readline()
  file.close()
  YES=0
  file=open("Evidence.txt","r")
  line=file.readline()
  while line!="":
    if line[:4]==Number:
      if line[5:6]=="Y":
        YES=YES+1
      if line[7:8]=="Y":
        YES=YES+1
      if line[9:10]=="Y":
        YES=YES+1
      break
    line=file.readline()
  file.close()
  if YES>=2:
    if percentage>=80:
      grade="A"
    elif percentage>=70 and percentage<80:
      grade="B"
    elif percentage>=60 and percentage<70:
      grade="C"
    elif percentage>=50 and percentage<60:
      grade="D"
    elif percentage>=40 and percentage<50:
      grade="E"
    else:
      grade="F"
  else:
    grade="U"
  return grade, percentage
def EditStudentGrades(Number):
  file=open("Grades.txt","r")
  line=file.readline()
  while line!="":
    if line[:4]==Number:
      print("Mock marks  of student stored: ", line[5:7], "/75")
      print("Premock marks of student stored: ", line[8:10], "/75")
      print("Class assessment marks of student stored: ", line[11:13], "/50")
      break
    line=file.readline()
  file.close()
  flagM=str(input("Do you want to edit the student's mock marks? Type in Y/N to change the saved marks: "))
  while flagM!="Y" and flagM!="N":
    flagM=str(input("Error, please only enter Y for yes, or N for no: "))
  if flagM=="Y":
    mock=str(input("Enter in mock marks (out of 75 - only two-digits): "))
    while mock<"00" or mock<"75" or len(mock)!=2:
      mock=str(input("Error, please re-enter mock marks: "))
    file=open("Grades.txt","r")
    copy=file.readlines()
    file.close()
    file=open("Grades.txt","r")
    line=file.readline()
    while line!="":
      if line[:4]==Number:
        break
      line=file.readline()
    replacement=line[:5]+mock+line[7:]
    file.close()
    for x in range (len(copy)):
      check=copy[x]
      if check[:-1]==line:
        copy[x]=replacement+"\n"
      elif check==line:
        copy[x]=replacement
    file=open("Grades.txt","w")
    file.writelines(copy)
    file.close()

  flagPM=str(input("Do you want to edit the student's premock marks? Type in Y/N to change the saved marks: "))
  while flagPM!="Y" and flagPM!="N":
    flagPM=str(input("Error, please only enter Y for yes, or N for no: "))
  if flagPM=="Y":
    premock=str(input("Enter in premock marks : "))
    while premock<"00" or premock>"75" or len(premock)!=2:
      premock=str(input("Error, please re-enter premock marks: "))
    file=open("Grades.txt","r")
    copy=file.readlines()
    file.close()
    file=open("Grades.txt","r")
    line=file.readline()
    while line!="":
      if line[:4]==Number:
        break
      line=file.readline()
    replacement=line[:8]+premock+line[10:]
    file.close()
    for x in range (len(copy)):
      check=copy[x]
      if check[:-1]==line:
        copy[x]=replacement+"\n"
      elif check==line:
        copy[x]=replacement
    file=open("Grades.txt","w")
    file.writelines(copy)
    file.close()
    
  flagCA=str(input("Do you want to edit the student's class assessment marks? Type in Y/N to change the saved marks: "))
  while flagCA!="Y" and flagCA!="N":
    flagCA=str(input("Error, please only enter Y for yes, or N for no: "))
  if flagCA=="Y":
    classs=float(input("Enter in class assessment marks (out of 50 - only two-digits): "))
    while classs<"00" or classs>"50" or len(classs)!=2:
      classs=str(input("Error, please re-enter class assessment marks: "))
    file=open("Grades.txt","r")
    copy=file.readlines()
    file.close()
    file=open("Grades.txt","r")
    line=file.readline()
    while line!="":
      if line[:4]==Number:
        break
      line=file.readline()
    replacement=line[:11]+classs+line[13:]
    file.close()
    for x in range (len(copy)):
      check=copy[x]
      if check[:-1]==line:
        copy[x]=replacement+"\n"
      elif check==line:
        copy[x]=replacement
    file=open("Grades.txt","w")
    file.writelines(copy)
    file.close()
def EditStudentEvidence(Number):
  file=open("Evidence.txt","r")
  line=file.readline()
  while line!="":
    if line[:4]==Number:
      print("(Data in files shown below, Y stands for yes, N for no)")
      print("Evidence for mock has been submitted: ", line[5:6])
      print("Evidence for premock has been submitted:  ", line[7:8])
      print("Evidence for class assessment has been submitted: ", line[9:10])
      break
    line=file.readline()
  file.close()
  flagM=str(input("Has evidence for the student's mock been submitted? To change the saved answer, type in Y/N: "))
  while flagM!="Y" and flagM!="N":
    flagM=str(input("Error, please only enter Y for yes, or N for no: "))
  if flagM=="Y":
    mock=str(input("Enter in Y/N for mock evidence: "))
    while mock!="Y" and mock!="N":
      mock=str(input("Error, please only enter Y for yes, or N for no: "))
    file=open("Evidence.txt","r")
    copy=file.readlines()
    file.close()
    file=open("Evidence.txt","r")
    line=file.readline()
    while line!="":
      if line[:4]==Number:
        break
      line=file.readline()
    replacement=line[:5]+mock+line[6:]
    file.close()
    for x in range (len(copy)):
      check=copy[x]
      if check[:-1]==line:
        copy[x]=replacement+"\n"
      elif check==line:
        copy[x]=replacement
    file=open("Evidence.txt","w")
    file.writelines(copy)
    file.close()
  flagPM=str(input("Has evidence for the student's premock been submitted? To change the saved answer, type in Y/N: "))
  while flagPM!="Y" and flagPM!="N":
    flagPM=str(input("Error, please only enter Y for yes, or N for no: "))
  if flagPM=="Y":
    premock=str(input("Enter in Y/N for premock evidence: "))
    while premock!="Y" and premock!="N":
      premock=str(input("Error, please only enter Y for yes, or N for no: "))
    file=open("Evidence.txt","r")
    copy=file.readlines()
    file.close()
    file=open("Evidence.txt","r")
    line=file.readline()
    while line!="":
      if line[:4]==Number:
        break
      line=file.readline()
    replacement=line[:7]+premock+line[8:]
    file.close()
    for x in range (len(copy)):
      check=copy[x]
      if check[:-1]==line:
        copy[x]=replacement+"\n"
      elif check==line:
        copy[x]=replacement
    file=open("Evidence.txt","w")
    file.writelines(copy)
    file.close()
  flagCA=str(input("Has evidence for the student's class assessment been submitted? To change the saved answer, type in Y/N: "))
  while flagCA!="Y" and flagCA!="N":
    flagCA=str(input("Error, please only enter Y for yes, or N for no: "))
  if flagCA=="Y":
    classs=str(input("Enter in Y/N for class assessment evidence: "))
    while classs!="Y" and classs!="N":
      classs=str(input("Error, please only enter Y for yes, or N for no: "))
    file=open("Evidence.txt","r")
    copy=file.readlines()
    file.close()
    file=open("Evidence.txt","r")
    line=file.readline()
    while line!="":
      if line[:4]==Number:
        break
      line=file.readline()
    replacement=line[:9]+classs+line[10:]
    file.close() 
    for x in range (len(copy)):
      check=copy[x]
      if check[:-1]==line:
        copy[x]=replacement+"\n"
      elif check==line:
        copy[x]=replacement
    file=open("Evidence.txt","w")
    file.writelines(copy)
    file.close()
def EditStudentGeneralData(Number):
  file=open("Student.txt","r")
  line=file.readline()
  while line!="":
    if line[:4]==Number:
      print("Candidate number stored: ", line[:4])
      print("Student name stored: ", line[5:5+len(line)])
      break
    line=file.readline()
  file.close()
  NameFlag=str(input("Do you want to change student name? Type in Y/N: "))
  while NameFlag!="Y" and NameFlag!="N":
    NameFlag=str(input("Error, please only enter Y for yes, or N for no: "))
  if NameFlag=="Y":
    name=str(input("Enter in his/her new name: "))
    valid="False"
    while valid=="False":
      valid="True"
      for x in range (len(name)):
        if name[x].lower()<"a" or name[x].lower()>"z":
          valid="False"
          name=str(input("Error, please re-enter student name: "))
          break
    file=open("Student.txt","r")
    copy=file.readlines()
    file.close()
    file=open("Student.txt","r")
    line=file.readline()
    while line!="":
      if line[:4]==Number:
        break
      line=file.readline()
    replacement=line[:5]+name
    file.close()
    for x in range (len(copy)):
      check=copy[x]
      if check==line and check[-1:]=="\n":
        copy[x]=replacement+"\n"
      elif check==line:
        copy[x]=replacement
    file=open("Student.txt","w")
    file.writelines(copy)
    file.close()
  CodeFlag=str(input("Do you want to change saved candidate number of inputted student? Type in Y/N: "))
  while CodeFlag!="Y" and CodeFlag!="N":
    CodeFlag=str(input("Error, please only enter Y for yes, or N for no: "))
  if CodeFlag=="Y":
    code=str(input("Enter new 4-digit candidate number: "))
    valid="False"
    while valid=="False":
      valid="True"
      file=open("Student.txt","r")
      line=file.readline()
      while line!="":
        if line[:4]==code:
          valid="False"
          break
        line=file.readline()
      file.close()
      if code<"0000" or code>"9999" or len(code)!=4:
        valid="False"
      if valid!="True":
        code=str(input("Error, please re-enter candidate number: "))
    file=open("Student.txt","r")
    copy=file.readlines()
    file.close()
    file=open("Student.txt","r")
    line=file.readline()
    while line!="":
      if line[:4]==Number:
        break
      line=file.readline()
    replacement=code+line[4:]
    file.close()
    for x in range (len(copy)):
      check=copy[x]
      if check[:-1]==line:
        copy[x]=replacement+"\n"
      elif check==line:
        copy[x]=replacement
    file=open("Student.txt","w")
    file.writelines(copy)
    file.close()
    file=open("Evidence.txt","r")
    copy=file.readlines()
    file.close()
    file=open("Evidence.txt","r")
    line=file.readline()
    while line!="":
      if line[:4]==Number:
        break
      line=file.readline()
    replacement=code+line[4:]
    file.close()
    for x in range (len(copy)):
      check=copy[x]
      if check[:-1]==line:
        copy[x]=replacement+"\n"
      elif check==line:
        copy[x]=replacement
    file=open("Evidence.txt","w")
    file.writelines(copy)
    file.close()
    file=open("Grades.txt","r")
    copy=file.readlines()
    file.close()
    file=open("Grades.txt","r")
    line=file.readline()
    while line!="":
      if line[:4]==Number:
        break
      line=file.readline()
    replacement=code+line[4:]
    file.close()
    for x in range (len(copy)):
      check=copy[x]
      if check[:-1]==line:
        copy[x]=replacement+"\n"
      elif check==line:
        copy[x]=replacement
    file=open("Grades.txt","w")
    file.writelines(copy)
    file.close()


flag1=str(input("Do you want to add details of a new student? Please type in Y/N: "))
while flag1!="Y" and flag1!="N":
  flag1=str(input("Error, please only enter Y for yes, or N for no: "))
while flag1=="Y":
  AddStudentDetails()
  flag1=str(input("Do you want to add details of another student? Please type in Y/N: "))
  while flag1!="Y" and flag1!="N":
    flag1=str(input("Error, please only enter Y for yes, or N for no: "))


flag2=str(input("Do you want to add in marks/evidence info to an already added student, or edit any aspect of the database? Please type in Y/N: "))
while flag2!="Y" and flag2!="N":
  flag2=str(input("Error, please only enter Y for yes, or N for no: "))
while flag2=="Y":
  StudentName=str(input("Enter student name: "))
  valid="False"
  while valid=="False":
    valid="True"
    for x in range (len(StudentName)):
      if StudentName[x].lower()<"a" or StudentName[x].lower()>"z":
        valid="False"
        StudentName=str(input("Error, re-enter student name: "))
        break
  CandidateNumber=FindStudentCode(StudentName)
  while CandidateNumber=="False":
    StudentName=str(input("Student not found, please re-enter name: "))
    CandidateNumber=FindStudentCode(StudentName)
  EditWhichPart=str(input("Do you want to edit student's grades, evidence, or general data? Please type in G, E or GD: "))
  while EditWhichPart!="G" and EditWhichPart!="E" and EditWhichPart!="GD":
    EditWhichPart=str(input("Error, please only enter G for grades, or E for evidence, or GD for general data: "))
  if EditWhichPart=="G":
    EditStudentGrades(CandidateNumber)
  elif EditWhichPart=="E":
    EditStudentEvidence(CandidateNumber)
  elif EditWhichPart=="GD":
    EditStudentGeneralData(CandidateNumber)
  flag2=str(input("Do you want to add in marks/evidence info to an already added student, or edit any aspect of the database, again? Please type in Y/N: "))
  while flag2!="Y" and flag2!="N":
    flag2=str(input("Error, please only enter Y for yes, or N for no: "))


flag3=str(input("Do you want to see efficiently generated center grade for specific student? Please type in Y/N: "))
while flag3!="Y" and flag3!="N":
  flag3=str(input("Error, please only enter Y for yes, or N for no: "))
while flag3=="Y":
  StudentName=str(input("Enter student name: "))
  valid="False"
  while valid=="False":
    valid="True"
    for x in range (len(StudentName)):
      if StudentName[x].lower()<"a" or StudentName[x].lower()>"z":
        valid="False"
        StudentName=str(input("Error, re-enter student name: "))
        break
  CandidateNumber=FindStudentCode(StudentName)
  while CandidateNumber=="False":
    StudentName=str(input("Student not found, please re-enter name: "))
    CandidateNumber=FindStudentCode(StudentName)
  FinalGrade,Percenatage=GiveGrade(CandidateNumber)
  if FinalGrade=="U":
    print(StudentName, " cannot be graded due to a lack of evidence")
  else:
    print(StudentName," has acquired grade: ", FinalGrade)
    print("Percenatage: ", round(Percenatage,1))
  flag3=str(input("Do you want to see efficiently generated center grade for another student? Please type in Y/N: "))
  while flag3!="Y" and flag3!="N":
    flag3=str(input("Error, please only enter Y for yes, or N for no: "))


print("")
print("")
print("Thank you for using Faizan's COVID-19 grading program :)")
