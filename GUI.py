from dearpygui.core import *
from dearpygui.simple import *
import csv
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
def clear_table_call(sender, data):
    clear_table("Table")

def callback(sender, data):
    #close all windows except the main search window to clear previous results
    wnds = get_windows()
    for wnd in wnds:
        if(wnd != "Sentiment Analysis"):
            delete_item(wnd)
    clear_table_call

    #call search method in pullTweets.py with srch_val as the search value
    with window("Sentiment Analysis"):
        srch_val = get_value("Input")
        num_tweets = get_value("Number")
        #this calls the Search function in backend.py with the searched term as
        #the parameter and num_tweets as number of tweets
        #be.Search(srch_val, num_tweets)
        print("Searched for " + srch_val + "over " + num_tweets + " tweets.")

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
                #create list of files to open
                if extension == '.png':
                    file_name = file
                    results.append(file_name)
                    tabnames.append(tname)
                #get info about csv file as well
                if extension == '.csv':
                    csv_name = file
                    csv_tab_name = tname

        for i in range(len(tabnames)):
            ti = TabInfo(tabnames[i], results[i])
            tabs.append(ti)

        #open new windows with result graphs
        #the title of the windows will be the same as the filename without extension
        #so save them with the name you want them to display under.
        i = 0
        h = int((940 / len(tabnames)) + 1)

        #open images
        for tb in tabs:
            with window(tb.name, width = 540, height = h):
                set_window_pos(tb.name, 541, i * h)
                add_drawing(tb.name, width = 300, height = 300)
                draw_image(tb.name, tb.result, [10, 10], pmax=[300, 300])
                i += 1
        #open csv
        with window(csv_tab_name, width = 540, height = 470):
            set_window_pos(csv_tab_name, 0, 471)
            with open(csv_name, newline='') as File:
                info = csv.reader(File)
                add_table("Table", ["Index", "Tweet"], hide_headers = True)
                tabledata = []
                for row in info:
                    tabledata.append(row)
        set_table_data("Table", tabledata)



#method to load images ends here

with window("Sentiment Analysis", width = 540, height = 470):
    set_window_pos("Sentiment Analysis", 0, 0)
    add_text("Enter search:")
    add_input_text("Input", label = "")
    add_text("Number of tweets to search: ")
    add_same_line()
    add_combo("Number", items=["250", "500", "750", "1000"], label = "", width = 150)
    add_button("Search", callback = callback, callback_data = lambda: get_value("Input"))

    #add dropdown with 250, 500, 750, 1000 for number of Tweets
    #add view for csv after search under the search bar

start_dearpygui()
