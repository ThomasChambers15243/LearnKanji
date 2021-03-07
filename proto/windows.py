import PySimpleGUI as sg
import os
import json
import util
from kanjiClass import Kanji, KanjiTest

#sg.popup_auto_close("Name already in use\n(Press enter or X\nto close)", auto_close_duration=2, grab_anywhere = True)
def themeChoicer(currentTheme):
  #sg.preview_all_look_and_feel_themes()
  themeDecided = False
  theme_name_list = sg.theme_list()
  print(theme_name_list)
  userTheme = "null"
  layout = [[sg.Text('All Theme Names')],
            [sg.Multiline(theme_name_list, size=(100, 20), key='textbox')]]
  sg.preview_all_look_and_feel_themes()
  while themeDecided == False:

    themeFinderWindow = sg.Window('Test', layout).Finalize()
    userTheme = util.takeSingleInput("New Theme","Enter a New Theme")
    # Create the Window    
    if userTheme in theme_name_list:
      print("in")
      currentTheme = userTheme
      themeDecided = True
    else:
      sg.popup_auto_close("Theme Not Found\n(Press enter or X\nto close)", auto_close_duration=2, grab_anywhere = True)
  return currentTheme
def createCustomKanjiSet():

    #TODO
    #Add option to remvoe from set
    #Create a copy of the new set to work on, and saving replaces the old, or you can save as a new one


    #def addKanji():
    #  print("add kanji ran")
    #  kanji = "none"
    #  sg.theme('BrightColors')
    #  AddKanjiLayout = [ [sg.Text("Enter new Kanji",justification='center', size = (62,1),font=('Helvetica 20'))],
    #            [sg.Text("", size = (5,1)),sg.InputText(justification='center',size=(15,1), key="newUserKanji",font=('Helvetica 20'))],
    #            [sg.Button('submit', visible=False, bind_return_key=True)],
    #            ]
  
    #  window = sg.Window('Create Custom Kanji Set', AddKanjiLayout,size=(350, 280),
    #                      return_keyboard_events=True, use_default_focus=True)
    #  while True: 
    #    event, values = window.Read()

    #    if event == "submit":
    #      print("enter pressed")
    #      kanji = values["newUserKanji"]
    #      print(kanji)
    #      window.Close()
    #      return kanji
        
    #    #closes loop
    #    if event == sg.WIN_CLOSED:
    #      break;
    #    #if kanji != "":
    #      #break;        
    #  return kanji


    #Main Window
    sg.theme('BrightColors')    
    AddKanjiLayout = [ [sg.Text("Create Custom Set",justification='center', size = (62,1),font=('Helvetica 20'))],
              [sg.Text("", size = (6,1)), sg.ReadButton("New Set", key="newSet"), sg.Text("", size = (6,1)), sg.ReadButton("Load Set", key="loadSet")],
              [sg.Text("", size = (15,1)), sg.ReadButton("Add Kanji ", key="addKanji")], 
              [sg.Text("", size = (15,1)), sg.ReadButton("Save Set", key="saveKanji")], 
              ]
  
    window = sg.Window('Create Custom Kanji Set', AddKanjiLayout,size=(350, 280),
                        return_keyboard_events=True, use_default_focus=False)

    #make these into a dictionary maybeeee
    fileName = "null"
    setLoaded = False
    filePath = "null.null"
    data = {}
    data["kanji"] = []
    #create a new kanji set
    #if event == "newSet":

    def newSet(fileName,setLoaded,filePath):
      newFileName = util.takeSingleInput("File Name", "Enter a New File Name")
      isNewFileName = util.checkIfNewFileName("customKanjiLists",".txt",newFileName)
      if isNewFileName == True:
        filePath = "customKanjiLists\\" + newFileName + ".txt"
        with open(filePath,"w") as outfile:
          print("opened")
          setLoaded = True
          sg.popup_auto_close("File loaded\n(Press enter or X\nto close)", auto_close_duration=2, grab_anywhere = True)
          return setLoaded, filePath
      else:
        print("Name already in use")
        sg.popup_auto_close("Name already in use\n(Press enter or X\nto close)", auto_close_duration=2, grab_anywhere = True)
        return setLoaded, filePath 
        ##kanji = 蜜 and 右 

    def addKanji(fileName,setLoaded,filePath):
      newKanjiArrayDic = {}
      if setLoaded == True:
        #filePath = "customKanjiLists\\newwwww.txt"
        newKanji = util.takeSingleInput("Enter New Kanji","Enter a new Kanji")
        print(newKanji + "funciton Worked")
        kanjiData = req.get_kanji_char_data(newKanji)
        if kanjiData != 404:
            
          #f = open(filePath,"w+")

          ##gets current kanji data from the file but i dont think its needed here as we're only adding a knaji to 
          ##a array that will be passed to the file later in 'save kanji'
          #if os.path.getsize(filePath) != 0:
          #  with open(filePath) as json_file:
          #    currentfiledata = json.load(json_file)
                

          #    #good for extracting the json info
          #    for i in range(0,len(currentfiledata)):
          #      newKanjiArrayData.append({
          #        "kanji" : currentfiledata["kanji"][i]["kanji"],
          #        "on" : currentfiledata["kanji"][i]["on"],
          #        "kun" : currentfiledata["kanji"][i]["kun"],
          #        "name" : currentfiledata["kanji"][i]["name"]                   
          #        })
          #else:
          #  print("file emtpy")
              
          newKanjiArrayDic = {
            "kanji" : kanjiData["kanji"],
            "on" : kanjiData["on_readings"],
            "kun" : kanjiData["kun_readings"],
            "name" : kanjiData["name_readings"]#kanji = 蜜 and 右
            }
        
        else:
          print(404)
          print("kanji not found")
          sg.popup_auto_close("Kanji Not Found\n(Press enter or X\nto close)", auto_close_duration=2, grab_anywhere = True)
      else:
        sg.popup_auto_close("Load a Set First\n(Press enter or X\nto close)", auto_close_duration=2, grab_anywhere = True)
        print("not loaded")
        #popup
      return newKanjiArrayDic

    def saveKanji(fileName,setLoaded,filePath,data):
      if setLoaded == False:
        return 1, setLoaded, filePath
      else:     
        with open(filePath,"w") as outfile:
          try:
            json.dump(data, outfile,indent=4)
            #resets the "knaji" key of the data dcitionary to emtpy again
            data["kanji"] = []
            setLoaded = False
            filePath = "null.null"
            return 0, setLoaded, filePath        
          except IOError:
            return 2, setLoaded, filePath  
    
            
    def loadKanjiList(filename,setLoaded,filePath): 
        data = {}
        data["kanji"] = []
        fileName = util.takeSingleInput("File Name", "Enter File Name")
        filePath = "customKanjiLists\\" + fileName + ".txt"
        fileIsFound = util.checkIfNewFileName("customKanjiLists", ".txt", fileName)
        if fileIsFound:
          filePath = "null.null"
          return False, filePath,data
        else:
          if os.path.getsize(filePath) != 0:
            with open(filePath) as json_file:
              currentfiledata = json.load(json_file)
              print(str(currentfiledata))
              for i in range(0,len(currentfiledata["kanji"])):
                print(str(i))
                data["kanji"].append({
                  "kanji" : currentfiledata["kanji"][i]["kanji"],
                  "on" : currentfiledata["kanji"][i]["on"],
                  "kun" : currentfiledata["kanji"][i]["kun"],
                  "name" : currentfiledata["kanji"][i]["name"]   
                  })
          else:
            print("file emtpy")
          return True, filePath, data

    #event Loop
    while True: 
      event, values = window.Read()

      #load a kanji set to change the data inside
      if event == "loadSet":
        setLoaded, filePath, currentKanjiData = loadKanjiList(fileName,setLoaded,filePath)
        if setLoaded == True:
          print("loaded")
          sg.popup_auto_close("Loaded\n(Press enter or X\nto close)", auto_close_duration=2, grab_anywhere = True)
          if currentKanjiData["kanji"] != []:
            data = currentKanjiData
            print("data is " + str(data))
        else:
          sg.popup_auto_close("File not Found\n(Press enter or X\nto close)", auto_close_duration=2, grab_anywhere = True)
          print("not loaded, file not found")

      #create a new kanji set
      if event == "newSet":
        setLoaded, filePath = newSet(fileName,setLoaded,filePath)


      #add a kanji in a custom list
      if event == "addKanji":
        newKanjiDicEle = addKanji(fileName,setLoaded,filePath)
        if newKanjiDicEle != {}:
          data["kanji"].append(newKanjiDicEle)
          print(data)
          print("knaji ele added")
        else:
          print("kanji ele NOT added")
        

      #save a knaji list
      if event == "saveKanji":
        saved, setLoaded, filePath = saveKanji(fileName,setLoaded,filePath,data)
        if saved == 1:
          print("Load a set first")
          sg.popup_auto_close("Load a set First\n(Press enter or X\nto close)", auto_close_duration=2, grab_anywhere = True)
        elif saved == 2:
          print("Could not save")
          sg.popup_auto_close("Could not Save\n(Press enter or X\nto close)", auto_close_duration=2, grab_anywhere = True)
        else:
          print("saved")
          sg.popup_auto_close("Saved\n(Press enter or X\nto close)", auto_close_duration=2, grab_anywhere = True)

      #closes loop
      if event == sg.WIN_CLOSED:
        break;

    return 0



def knajiCustomTest(filePath,isKunReading,isOnReading):#kunReading,onReading,nameReadings:

  _STATE_ = {
  "running" : False
  }
  sg.theme('BrightColors')
  layout = [ [sg.Text("Kanji reading is:",justification='center', size = (62,1),font=('Helvetica 20'))],
            [sg.Text("", size = (7,1)),sg.Text("", size=(13,1),key="kanjiReading",justification='center',font=('Helvetica 20'))],
            [sg.Text("", size = (7,1)),sg.InputText(justification='center',size=(13,1), key="userKanji",font=('Helvetica 20'))],
            [sg.Text("", size = (10,1)),sg.Text("",size = (20,1),key="answer",font=('Helvetica 20'))],
            [sg.Text("", size = (15,1)), sg.ReadButton("Start", key="butStart"), 
             sg.Button('submit', visible=False, bind_return_key=True)],
            [sg.Text("Correct", size = (6,1), justification='center',font=('Helvetica 14')),
             sg.Text("", size = (3,1)),
             sg.Text("Shown",size = (6,1), justification='center',font=('Helvetica 14')),
             sg.Text("", size = (4,1)),
             sg.Text("Wrong",size = (6,1),justification='center',font=('Helvetica 14'))],
            [sg.Text("0", size = (6,1), justification='center',key="correct",font=('Helvetica 14')),
             sg.Text("", size = (3,1)),
             sg.Text("0",size = (6,1), justification='center',key="shown",font=('Helvetica 14')),
             sg.Text("", size = (4,1)),
             sg.Text("0",size = (6,1),justification='center',key="wrong",font=('Helvetica 14'))],
            ]
  
  window = sg.Window('Kanji Test', layout,size=(350, 280),
                     return_keyboard_events=True, use_default_focus=False)


  ##get all kanji from grade file as data
  #gradeNum = str(grade)
  #filePath = "grades\grade-" + gradeNum + ".txt"
  with open(filePath) as json_file:
    data = json.load(json_file)
    print("DATA IS " + str(data))
  ##kanjiArray were each element in a dictionary holding 1 kanji and its readings
  ##has a boolean "marked" key, this is in use to see if the kanji has been tested before
  kanjiTestArray = KanjiTest([],-1,0,False)
  for i in range(len(data["kanji"])):#for i in data["kanji"]:
    print(str(i))
    #kanjiObj = Kanji(i["kanji"],i["kun"][0],"サ",i["name"],False)
    #testing with a shorter range
    kanjiObj = Kanji(data["kanji"][i]["kanji"],data["kanji"][i]["kun"][0],data["kanji"][i]["on"][0],data["kanji"][i]["name"],False)#data["kanji"][i]["kun"][0],"サ",data["kanji"][i]["name"],False)
    kanjiTestArray.appendTestArray(kanjiObj)

  currentKanjiIndex = kanjiTestArray.getNewKanji()

  print("current kanji index is: " + str(currentKanjiIndex))


  #numbers tracking user's score
  shown = 0
  correct = 0
  wrong = 0
  score = [0]

  shownBefore = False
  passedKanji = False
  #event loop
  while True:
    event, values = window.Read()

    #closes loop
    if event == sg.WIN_CLOSED:
      break
        
    #starts test loop
    if event == "butStart":
      _STATE_["running"] = True
    

    print(str(_STATE_["running"]))#testing
    
    # only takes users input when
    # enter key is pressed
    if event == "submit":
      userKanji = values["userKanji"]
    else:
       userKanji = ""

    #currentKanjiIndex = kanjiTestArray.getNewKanji()
    if _STATE_["running"] == True:
      #shows current kanji
      window["kanjiReading"].Update(kanjiTestArray.getTestArrayEle(currentKanjiIndex).getKanji())

      #checks if usersreading is in on
      correctAnswer = False
      if userKanji != "":
        if isKunReading == True:
          if userKanji in kanjiTestArray.getTestArrayEle(currentKanjiIndex).getKun():
            correctAnswer = True
            print("kun yes")
          else:
            correctAnswer  = False
            print("kun no")
        if isOnReading == True and correctAnswer != True:
          print(kanjiTestArray.getTestArrayEle(currentKanjiIndex).getOn())
          print(userKanji)
          if userKanji in kanjiTestArray.getTestArrayEle(currentKanjiIndex).getOn():
            correctAnswer = True
            print("on yes")
          else:
            correctAnswer = False
            print("on no")
        if correctAnswer == True:
          #displays correct answer
          answer = userKanji + "is correct"
          window.FindElement("answer").Update(answer) #kunReading,onReading,nameReadings
          #clear users input
          window["userKanji"]("")
          shown+=1
          passedKanji = True
        if passedKanji == True:
          if shownBefore != False:
            wrong+=1
            #selcect new kanji
            #randKanjiIndex = random.randint(0,len(kanjiTestArray)-1) 
            #currentKanji = kanjiTestArray[randKanjiIndex]
            if kanjiTestArray.getRepeat() == False: 
              if kanjiTestArray.checkAllTested() == True:
                print("all have been tested")
                break
            currentKanjiIndex = kanjiTestArray.getNewKanji()
            #reset bool tests
            shownBefore = False
            passedKanji = False
          else:
            correct+=1
            #print(testedKanji)
            #print(currentKanjiIndex)
            #select new kanji
            #randKanjiIndex = random.randint(0,len(kanjiTestArray)-1) 
            #currentKanji = kanjiTestArray[randKanjiIndex]
            if kanjiTestArray.getRepeat() == False: 
              if kanjiTestArray.checkAllTested() == True:
                print("all have been tested")
                score = [correct, shown, wrong]
                break
            currentKanjiIndex = kanjiTestArray.getNewKanji()
            #reset bool tests
            shownBefore = False
            passedKanji = False

          #updates scores for user to see
          window["shown"].Update(shown)
          window["correct"].Update(correct)
          window["wrong"].Update(wrong)
        elif userKanji != "":
          answer = userKanji + "is wrong"
          window["answer"].Update(answer)
          shownBefore = True
  #TODO 
  #pop up wiht button to close both windows, 
  #shows scores on that window          
  #closes window and returns with the array score:
  #                               correct, shown, wrong        
  
  #sg.popup_OK('Score was')


  #time.sleep(0.5)
  window.close()
  return score



def kanjiGradePrac(grade,isKunReading,isOnReading):#kunReading,onReading,nameReadings:

  _STATE_ = {
  "running" : False
  }
  sg.theme('BrightColors')
  layout = [ [sg.Text("Kanji reading is:",justification='center', size = (62,1),font=('Helvetica 20'))],
            [sg.Text("", size = (7,1)),sg.Text("", size=(13,1),key="kanjiReading",justification='center',font=('Helvetica 20'))],
            [sg.Text("", size = (7,1)),sg.InputText(justification='center',size=(13,1), key="userKanji",font=('Helvetica 20'))],
            [sg.Text("", size = (10,1)),sg.Text("",size = (20,1),key="answer",font=('Helvetica 20'))],
            [sg.Text("", size = (15,1)), sg.ReadButton("Start", key="butStart"), 
             sg.Button('submit', visible=False, bind_return_key=True)],
            [sg.Text("Correct", size = (6,1), justification='center',font=('Helvetica 14')),
             sg.Text("", size = (3,1)),
             sg.Text("Shown",size = (6,1), justification='center',font=('Helvetica 14')),
             sg.Text("", size = (4,1)),
             sg.Text("Wrong",size = (6,1),justification='center',font=('Helvetica 14'))],
            [sg.Text("0", size = (6,1), justification='center',key="correct",font=('Helvetica 14')),
             sg.Text("", size = (3,1)),
             sg.Text("0",size = (6,1), justification='center',key="shown",font=('Helvetica 14')),
             sg.Text("", size = (4,1)),
             sg.Text("0",size = (6,1),justification='center',key="wrong",font=('Helvetica 14'))],
            ]
  
  window = sg.Window('Kanji Test', layout,size=(350, 280),
                     return_keyboard_events=True, use_default_focus=False)


  ##get all kanji from grade file as data
  gradeNum = str(grade)
  filePath = "grades\grade-" + gradeNum + ".txt"
  with open(filePath) as json_file:
    data = json.load(json_file)
  
  ##kanjiArray were each element in a dictionary holding 1 kanji and its readings
  ##has a boolean "marked" key, this is in use to see if the kanji has been tested before
  kanjiTestArray = KanjiTest([],-1,0,False)
  for i in range(0,2):#for i in data["kanji"]:
    #kanjiObj = Kanji(i["kanji"],i["kun"][0],"サ",i["name"],False)
    #testing with a shorter range
    kanjiObj = Kanji(data["kanji"][i]["kanji"],data["kanji"][i]["kun"][0],data["kanji"][i]["on"][0],data["kanji"][i]["name"],False)#data["kanji"][i]["kun"][0],"サ",data["kanji"][i]["name"],False)
    kanjiTestArray.appendTestArray(kanjiObj)

  currentKanjiIndex = kanjiTestArray.getNewKanji()

  print("current kanji index is: " + str(currentKanjiIndex))


  #numbers tracking user's score
  shown = 0
  correct = 0
  wrong = 0
  score = [0]

  shownBefore = False
  passedKanji = False
  #event loop
  while True:
    event, values = window.Read()

    #closes loop
    if event == sg.WIN_CLOSED:
      break
        
    #starts test loop
    if event == "butStart":
      _STATE_["running"] = True
    

    print(str(_STATE_["running"]))#testing
    
    # only takes users input when
    # enter key is pressed
    if event == "submit":
      userKanji = values["userKanji"]
    else:
       userKanji = ""

    #currentKanjiIndex = kanjiTestArray.getNewKanji()
    if _STATE_["running"] == True:
      #shows current kanji
      window["kanjiReading"].Update(kanjiTestArray.getTestArrayEle(currentKanjiIndex).getKanji())

      #checks if usersreading is in on
      correctAnswer = False
      if userKanji != "":
        if isKunReading == True:
          if userKanji in kanjiTestArray.getTestArrayEle(currentKanjiIndex).getKun():
            correctAnswer = True
            print("kun yes")
          else:
            correctAnswer  = False
            print("kun no")
        if isOnReading == True and correctAnswer != True:
          print(kanjiTestArray.getTestArrayEle(currentKanjiIndex).getOn())
          print(userKanji)
          if userKanji in kanjiTestArray.getTestArrayEle(currentKanjiIndex).getOn():
            correctAnswer = True
            print("on yes")
          else:
            correctAnswer = False
            print("on no")
        if correctAnswer == True:
          #displays correct answer
          answer = userKanji + "is correct"
          window.FindElement("answer").Update(answer) #kunReading,onReading,nameReadings
          #clear users input
          window["userKanji"]("")
          shown+=1
          passedKanji = True
        if passedKanji == True:
          if shownBefore != False:
            wrong+=1
            #selcect new kanji
            #randKanjiIndex = random.randint(0,len(kanjiTestArray)-1) 
            #currentKanji = kanjiTestArray[randKanjiIndex]
            if kanjiTestArray.getRepeat() == False: 
              if kanjiTestArray.checkAllTested() == True:
                print("all have been tested")
                break
            currentKanjiIndex = kanjiTestArray.getNewKanji()
            #reset bool tests
            shownBefore = False
            passedKanji = False
          else:
            correct+=1
            #print(testedKanji)
            #print(currentKanjiIndex)
            #select new kanji
            #randKanjiIndex = random.randint(0,len(kanjiTestArray)-1) 
            #currentKanji = kanjiTestArray[randKanjiIndex]
            if kanjiTestArray.getRepeat() == False: 
              if kanjiTestArray.checkAllTested() == True:
                print("all have been tested")
                score = [correct, shown, wrong]
                break
            currentKanjiIndex = kanjiTestArray.getNewKanji()
            #reset bool tests
            shownBefore = False
            passedKanji = False

          #updates scores for user to see
          window["shown"].Update(shown)
          window["correct"].Update(correct)
          window["wrong"].Update(wrong)
        elif userKanji != "":
          answer = userKanji + "is wrong"
          window["answer"].Update(answer)
          shownBefore = True
  #TODO 
  #pop up wiht button to close both windows, 
  #shows scores on that window          
  #closes window and returns with the array score:
  #                               correct, shown, wrong        
  
  #sg.popup_OK('Score was')


  #time.sleep(0.5)
  window.close()
  return score


