import PySimpleGUI as sg
import json
import urllib.request
import util
import req
import random
import time
import os
import windows
from kanjiClass import Kanji, KanjiTest
##from PIL import Image

#import sys
#import codecs
#######################################
#https://kanjiapi.dev/
#######################################

###theme decider
  #layout = [[sg.Text('Theme Browser')],
  #          [sg.Text('Click a Theme color to see demo window')],
  #          [sg.Listbox(values=sg.theme_list(), size=(20, 12), key='-LIST-', enable_events=True)],
  #          [sg.Button('Exit')]]

  #window = sg.Window('Theme Browser', layout)

  #while True:  # Event Loop
  #    event, values = window.read()
  #    if event in (sg.WIN_CLOSED, 'Exit'):
  #        break
  #    sg.theme(values['-LIST-'][0])S
  #    sg.popup_get_text('This is {}'.format(values['-LIST-'][0]))

  #window.close()

sg.theme('BrightColors')
#sg.theme(windows.themeChoicer(sg.theme()))
def mainWindow():
  mainLayout = [ [sg.Text("Which Grade")],
            [sg.ReadButton("Choose Theme",key="themeChooser")],
            [sg.ReadButton("Test Grade 1",key="gradeTest1"),sg.Radio('Only Kun Reading', "choice", default=True, key = "kunRead")],#sg.Checkbox('kun Readings', default=True,key="kunRead"), sg.Checkbox('On Readings', key="onRead")],
            [sg.ReadButton("Test Grade 2",key="gradeTest2"),sg.Radio('Only On Reading', "choice", default=False, key="onRead")],
            [sg.ReadButton("Test Grade 3",key="gradeTest3"),sg.Radio('Both Readings', "choice", default=False, key="bothRead")],
            [sg.ReadButton("Test Grade 4",key="gradeTest4")],
            [sg.ReadButton("Test Grade 5",key="gradeTest5")],
            [sg.ReadButton("Test Grade 6",key="gradeTest6")],
            [sg.ReadButton("Test Grade 8",key="gradeTest8")],
            [sg.ReadButton("Custom Set",key="customSet"),sg.ReadButton("Create Custom Set",key="createCustomSet")],
            ]

  MainWindow = sg.Window('Kanji Test', mainLayout,size=(400, 400),
                       return_keyboard_events=True, use_default_focus=False)

  testType= ["gradeTest1","gradeTest2","gradeTest3","gradeTest4","gradeTest5","gradeTest6","gradeTest8","customSet","createCustomSet"]

  while True:
    event, values = MainWindow.Read()
    if event == sg.WIN_CLOSED:
      break
    if event["themeChooser"]:###############WORK ON THIS TOMORROW
      sg.theme(windows.themeChoicer(sg.theme()))
    for i in range(0,len(testType)):
      if event == testType[i]:
        if values["bothRead"] == False:
          isKunReading = values["kunRead"]
          isOnReading = values["onRead"]
        else:
          isKunReading = True
          isOnReading = True
        
        
        if i < 7:
          customTest = "null"
          gradeNum = testType[i][-1:]
        else:
          customTest = testType[i]

        if customTest == "customSet":
          #Load custom set decision window
          customName = util.takeSingleInput("Custom Set Name", "Enter a custom set name")
          customFilePath = "customKanjiLists\\" + customName + ".txt"
          if util.checkIfNewFileName("customKanjiLists\\",".txt",customName):
            print("Custom Set Not Found")
            sg.popup_auto_close("Custom Set Not Found\n(Press enter or X\nto close)", auto_close_duration=2, grab_anywhere = True)
          else:
            print("FoundFile")
            test = windows.knajiCustomTest(customFilePath,isKunReading,isOnReading)            
        elif customTest == "createCustomSet":
          #load custom set creation window
          test = windows.createCustomKanjiSet()
          print("cusotm ran")
          print("")
          test = ["1"]
        else:
          print(gradeNum)
          gradeFilePath = "grades\grade-" + gradeNum + ".txt" 
          print(gradeFilePath)
          test = windows.knajiCustomTest(gradeFilePath,isKunReading,isOnReading)
        if len(test) == 1:
          print("TEST WORKED")
        else:
          sg.Popup('Your Score, out of ' + str(test[1]) + ' shown was:',
          'Correct: ' + str(test[0]),
          'Wrong: ' + str(test[2]))
        




########################### start in customs kanji window ###########################
#windows.createCustomKanjiSet()
########################### start in main window ###########################
mainWindow()
#windows.knajiCustomTest("grades\grade-1.txt", True, True)
########################### start in a grade test ###########################
#windows.kanjiGradePrac("1",True,False)

