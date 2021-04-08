from dearpygui.core import *
from dearpygui.simple import *
#import backend.py as be
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
    #close all windows except the main search window to clear previous results
    wnds = get_windows()
    for wnd in wnds:
        if(wnd != "Sentiment Analysis"):
            delete_item(wnd)

    #call search method in pullTweets.py with iv as the search value
    with window("Sentiment Analysis"):
        iv = get_value("Input")
        #this calls the Search function in backend.py with the searched term as
        #the parameter
        #be.Search(iv)
        print("Searched for " + iv)

#method to load images starts here
        results = []
        tabnames = []
        tabs = []
        #change "." to wherever you end up storing the images
        #currently, I'm checking if the file is a .png,
        #but you can || other types or change it if you want.
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
        #the title of the windows will be the same as the filename without extension
        #so save them with the name you want them to display under.
        i = 0
        h = int((940 / len(tabnames)) + 1)

        for tb in tabs:
            with window(tb.name, width = 540, height = h):
                set_window_pos(tb.name, 541, i * h)
                add_drawing(tb.name, width = 300, height = 300)
                draw_image(tb.name, tb.result, [10, 10], pmax=[300, 300])
                i += 1
#method to load images ends here

with window("Sentiment Analysis", width = 540, height = 940):
    set_window_pos("Sentiment Analysis", 0, 0)
    add_text("Enter search:")
    add_input_text("Input", label = "")
    add_button("Search", callback = callback, callback_data = lambda: get_value("Input"))
    #add dropdown with 250, 500, 750, 1000 for number of Tweets
    #add view for csv after search under the search bar

start_dearpygui()
