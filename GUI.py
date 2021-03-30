from dearpygui.core import *
from dearpygui.simple import *
#import pullTweets.py
import os

#window settings
set_main_window_size(1080, 980)
set_theme("Cherry")

class TabInfo:
    def __init__(self, name, result):
        self.name = name
        self.result = result

def callback_blank(sender, data):
    return

def callback(sender, data):
    #close all windows except main
    wnds = get_windows()
    for wnd in wnds:
        if(wnd != "Sentiment Analysis"):
            delete_item(wnd)

    #call search funtion with input
    with window("Sentiment Analysis"):
        iv = get_value("Input")
        #call pullTweets.py with q=iv
        print("Searched for " + iv)

        results = []
        tabnames = []
        tabs = []
        for root, dirs, files in os.walk("."):
            for file in files:
                tname, extension = os.path.splitext(file)
                if extension == '.png':
                    file_name = file
                    results.append(file_name)
                    tabnames.append(tname)

        for i in range(len(tabnames)):
            ti = TabInfo(tabnames[i], results[i])
            tabs.append(ti)

        #open new windows with result graphs
        i = 0
        h = int((940 / len(tabnames)) + 1)

        for tb in tabs:
            with window(tb.name, width = 540, height = h):
                set_window_pos(tb.name, 541, i * h)
                add_drawing(tb.name, width = 300, height = 300)
                draw_image(tb.name, tb.result, [10, 10], pmax=[300, 300])
                i += 1


with window("Sentiment Analysis", width = 540, height = 940):
    set_window_pos("Sentiment Analysis", 0, 0)
    add_text("Enter search:")
    add_input_text("Input", label = "")
    add_button("Search", callback = callback, callback_data = lambda: get_value("Input"))

start_dearpygui()
