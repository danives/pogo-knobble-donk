# pogo-knobble-donk
Will log peoples messages to if they contain the words "knobble" or "donk" to a webpage

## Installation

You first need to download and install Python 2.7.13 as it's the specific version that streamlabs chatbot uses. You can find the download at https://www.python.org/downloads/release/python-2713/ (choose the version you wish, it's likely the 'Windows x86-64 MSI installer' one).

Once installed, you will need to open your chatbot, go to the "Scripts" tab, and click the cog. There, you will find a place to pick the folder for your Python installation (more precisely, the Lib folder) - this will *likely* be C:\Python27\Lib unless you changed something during install. This will auto-save.

Download the .zip file (or download the folder, and turn it into a zip file). In the "Scripts" tab, click the second icon (the square with an arrow in) and select the zip file. This will install the script.

You will also need to click the "enabled" checkbox to make sure it is running.

## Testing

Right click on the script, and click on "Open Script Folder". In there, you should see a "output.html" file. Double click this, and this will open in your browser.

Now, go to the console of your chatbot and try typing "donk" or "knobble". You should see after it is posted, that the count goes up in the webpage.

It should be noted that it shouldn't go up past 1, as it it restricted to one vote per person. If you try and type "donk" and "knobble" in the same message, you'll get a warning. It should also pick up on any sentences that use the phrase, such as "that was such a DONK" or "crap knobble".

To reset the votes, in scripts simply click on the script and on the right hand side you should see a button called "RESET VOTES". Clicking this will reset the voting, and say the results on chat.

## Improvements

The browser layout leaves a lot to be desired, but it is a working proof-of-concept. This could be altered with any number of graphics, or alternatively the graphics could simply be added extra and instead two webpages created, one for each number.
