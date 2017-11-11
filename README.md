# NDSR presentation and workshop
*November 13, 2017*  
*Library of Congress*

Materials for an invited talk and workshop on metadata enrichment and collections-as-data for the 2016-2017 National Digital Stewardship Residency (NDSR) program.  

## Presentation  

Slides available here.  

## Workshop -- Exploring collections-as-data with Google Sheets

(Full tutorial available [here](https://docs.google.com/document/d/1uNZ34FEn-vGwXc2SUFPrPLMt17mjMePNe6ZMdBQFME0/edit?usp=sharing).)  

In this workshop, we’ll be learning how to use some basic and intermediate functionality of Google Sheets to familiarize ourselves with a new dataset and manipulate the data with the goal of plotting some digital collection items in [Timeline.js](https://timeline.knightlab.com/), an online timeline creation tool.   

### Before we start…
Here are a few tips for working with spreadsheets or coding in general and making the most of today’s workshop:  
1. The first rule of spreadsheet club is __always make a copy__! Either a copy of the file or a copy of the tab in the same spreadsheet. This will come in handy when you…
2. __Mess up__. Mess up a lot! If you’re not breaking things, you’re not learning. Embrace error messages as new friends and then Google the hell out of them. They are not reflections on your self-worth or technical ability.
3. __There is more than one way to do just about everything__, and don’t worry that you’re doing it the “wrong” way. If you’re getting the result you want, you’re doing it right! Once you learn one right way, learn others that might be more efficient or work better in other contexts. 
4. __Map your path.__ Keep track each step you take on your spreadsheet journey. This will help if you want to reproduce your work or if you mess up and need to start over. You might find it helpful to open up a new tab in your spreadsheet for tracking your progress step by step.
5. __It’s okay to get stumped.__ A lot of this kind of work involves sitting with the discomfort of trying to solve hard problems (or more often, seemingly trivial ones). When you’re ready to give up and ask questions, try sitting with the problem for just 10 minutes longer (or get up and take a break, sleep on it, walk around the block and come back). You’ll be amazed at how often you find your answer in this space.  
6. __But it’s also okay to ask questions!__ (Especially today when we only have about an hour. If you’re stuck, stick your post-it note to the top of your computer, and someone will come help!) Find a colleague, buddy, or mentor with whom you feel comfortable asking questions, and let them know you already did step 5. Code clubs or dedicated slack channels can also be a great source of help. Finding or creating a group of people in the same boat willing to help each other can take some of the fear out of asking questions. 
7. __Help others.__ If you know something, share it! Even if you think you’re a beginner, you’ve likely learned different skills and tricks than other beginners. Helping someone else is also a good way to cement techniques you’ve already learned. (In today’s workshop, if you find you’re all caught up, take a look around the room for post-it notes, and see if you can help out.) But PLEASE be considerate! Think of how you would like to be helped. None of this: “I can’t believe you don’t know about [*completely reasonable thing to not know about--basically anything*]!!!” or this: “It’s so easy, all you do is just [*bunch of things that do not seem easy*].” And no Windows shaming, Mac folks! 


### Get the data:  
We’ll be working with a tabular dataset I created from the MODS XML metadata of two digitized women’s suffrage collections from [NYPL](https://digitalcollections.nypl.org/collections/schwimmer-lloyd-collection#/about?tab=about) and [Library of Congress](https://www.loc.gov/collections/national-american-woman-suffrage-association/about-this-collection/). In my presentation, I talked about Frictionless Data packages as a standardized method of sharing data and related documentation. I’ve created one for this dataset in the [womens-suffrage-collections-data](https://github.com/saverkamp/loc-talk-2017/tree/master/womens-suffrage-collections-data) of this repo. Here you can access the data, read more about the dataset--context on the collections as well as information on how the data was created, and see the Python scripts I used to harvest and convert the data from MODS XML to CSV.   

The data package above includes a CSV file you can import into Google Sheets (“File” > “Import...” > “Upload”) , BUT because of our short time today, let’s all: 
1. Copy a [Google Sheet already loaded with the data](https://docs.google.com/spreadsheets/d/10cmbW74m600wy1xW-kTV1CEHQPLNR5DuIELEwjXucO0/edit?usp=sharing)
2. In the upper left navigation, click “File” > “Make a copy”  
3. You should get a prompt to rename your copy and put it in the Google Drive directory of your choosing. Click “OK”. You should now be in your copy of the data. Close the tab with the original data--you won’t need this again.  

### Get the Timeline.js template:  
We’ll be copying and pasting some of our data into another Google Sheet--a template for powering an online timeline app. Let’s get this template now, so we can see what form we’ll need to shape our data into:  
1. Go to [https://timeline.knightlab.com/](https://timeline.knightlab.com/) and click the “Make a Timeline” button.
2. Under step 1, click the “Get the Spreadsheet Template” button. This will open a new tab in your browser and prompt you to make a copy. Click the “Make a copy” button. You should now have your own copy of the template Google Sheet. (You can rename this whatever you like.)  

If you'd like to follow along or move at your pace, you can find a full tutorial for this workshop with screenshots [over here](https://docs.google.com/document/d/1uNZ34FEn-vGwXc2SUFPrPLMt17mjMePNe6ZMdBQFME0/edit?usp=sharing).  
