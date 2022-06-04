import PySimpleGUI as sg
from model import *
from predict import get_bag_of_words, classify, response
import datetime

def classify_and_response(a):
  classify_ = classify(a)
  class_name = classify_[0]

  now = datetime.datetime.now()
  hour = now.hour

  if hour < 12 and classify_[0] == "greeting":
    respond = f"Halo selamat pagi, {response(class_name)}"
  elif hour < 18 and classify_[0] == "greeting":
    respond = f"Halo selamat siang, {response(class_name)}"
  elif hour > 18 and classify_[0] == "greeting":
    respond = f"Halo selamat malam, {response(class_name)}"
  else:
    respond = f"{response(class_name)}"
    
  return respond
  
sg.theme('GreenTan')
sg.SetOptions(text_color="#e4e4e4", font='opensans 11')

layout = [[sg.Text("Program Chatbot Toko Online", font='sfprodisplay 25 bold')], 
            [sg.Text('Output', size=(40,1))],
            [sg.Output(size=(110,20), key='-OUTPUT-', font=('Helvetica 10'))],
            [sg.Text('Chat', size=(40,1))],
            [sg.Multiline(size=(70,5), enter_submits=False, key='-QUERY-', do_not_clear=False), 
             sg.Button('SEND', button_color=(sg.YELLOWS[0], sg.BLUES[0]), bind_return_key=True),
             sg.Button('EXIT', button_color=(sg.YELLOWS[0], sg.GREENS[0]))]]

window = sg.Window("Chat", layout, font=('Helvetica', '13'), 
                    default_button_element_size=(8,2), 
                    use_default_focus=False)

if __name__ == "__main__":
  while True:
    event, value = window.read()
    if event != "SEND":
        break
    if event == 'SEND':
        query = classify_and_response(value['-QUERY-'])
    print(f"USER : {value['-QUERY-']}\nADMIN : {query}\n")
    
window.close()
    