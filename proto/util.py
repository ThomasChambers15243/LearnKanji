import json
import PySimpleGUI as sg
from os import listdir
from os.path import isfile, join


#addKanji
def getFileNames(myPath):
  files = [f for f in listdir(myPath) if isfile(join(myPath, f))]
  return files #returns an array of the names of all the file 

def takeSingleInput(windowTitle,enterText):
      word = "none"
      sg.theme('BrightColors')
      AddKanjiLayout = [ [sg.Text(enterText,justification='center', size = (62,1),font=('Helvetica 20'))],
                [sg.Text("", size = (5,1)),sg.InputText(justification='center',size=(15,1), key="newUserWord",font=('Helvetica 20'))],
                [sg.Button('submit', visible=False, bind_return_key=True)],
                ]
  
      window = sg.Window(windowTitle, AddKanjiLayout,size=(350, 280),
                          return_keyboard_events=True, use_default_focus=True)
      while True: 
        event, values = window.Read()

        if event == "submit":
          print("enter pressed")
          word = values["newUserWord"]
          print(word)
          window.Close()
          return word
        
        #closes loop
        if event == sg.WIN_CLOSED:
          break;
        #if kanji != "":
          #break;        
      return word

#return True if the file is new, False if the name already exits int the dir
def checkIfNewFileName(path,fileType,newFileName):
  newFileName = newFileName + fileType
  files = getFileNames(path)
  isNewFileName = True
  for file in files:
    if newFileName == file:
      isNewFileName = False
      break;
  return isNewFileName


##funciton to turn a knaji char into its utf-8 ascii rep for a url
def kanji_to_utf8_ascii_url_string(kanji):
  
  #list of chars to remove from kanji
  expell = ["x","\'"] 
  #encodes turns to string, then removes the first 4 chars of the string
  kanji = kanji.encode("utf-8")
  kanji = str(kanji)
  kanji = kanji[4:]

  #removes uneeded chars
  for i in kanji:
    if i in expell:
      kanji=kanji.replace(i,"")
    elif i == "\\":
      kanji=kanji.replace(i,"%")
    else:
      kanji=kanji.replace(i,i.upper())
  #adds % at the start
  kanji = "%" + kanji

  return kanji

#creates grade JSON txt files

#ctrl+k+C to comment
#ctrl+k+u to uncomment

#def createGradeJSONFiles():
#  #grade = "grade-"
#  #for i in range(1,8):
#  #  if i == 7:
#  #    i = 8
#    #currentGrade = i
#    #gradeName = grade + str(currentGrade) + ".txt"
#    #data = req.get_kanji_grade_data(i)
#    #print(data) ##testing

#  #accept kun, on, name and custumn


#  grade = "grade-"
#  TOTALKANJI = 0
#  for i in range(1,8):#一
#    data = {}
#    data['kanji'] = []
#    if i == 7:
#      i = 8
  
#    currentGrade = i
#    gradeName = grade + str(currentGrade) + ".txt"
#    gradeList =  grade + str(currentGrade)
#    listData = req.get_kanji_list_data(gradeList)

#    kanjiCharReadings = []
#    print(listData)
#    num = 1
#    for kanji in listData:
#      print(kanji)
#      kanjiData = req.get_kanji_char_data(kanji)
#      kun = kanjiData["kun_readings"],
#      on = kanjiData["on_readings"],
#      name = kanjiData["name_readings"]
#      print("###########################################################################")
#      print("Grade is " + str(currentGrade))
#      print(num)
#      print("###########################################################################")
#      data['kanji'].append({
#        'kanji': kanji,
#        'kun' : kun,
#        'on' : on,
#        'name' : name
#        })
#      num+=1
#    with open(gradeName,"w") as outfile:
#      json.dump(data, outfile,indent=4)
#    TOTALKANJI+=num
#    if i == 8:
#      break
#  print("#########################")
#  print("#########################")
#  print("Totoal number of kanji added are:")
#  print(TOTALKANJI)
#  print("#########################")
#  print("#########################")
#createGradeJSONFiles()













##gets all chars from a text file
def getCharsFromtxt(file):
    chars = []
    for line in file:
      for char in line:
        chars.append(char)
    return chars