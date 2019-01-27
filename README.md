Arch-Project
=============================

Final project as a result of the first block of the course "Architecture of information systems". Variant 9

Source
------------
Please make sure that all the files below are available in your source

      static/               
            css/           styles
            js/            Javasctipt files JQuery and selectbox
            /img           pictures
            /templastes    html page
      README.md            readme
      app.py               boot file
      parser.py            data collector and handler



Description
------------
This project is a web service, which consists of a server and client components.
The server part is responsible for collecting, processing and transferring data to the client.
The client part is responsible for data display dynamically.
 
Server
-----------
Server uses Flask for data collection and processing. Server logic can be divided on
two components. The first component is directly responsible for data collection and processing..

The process of collecting 30 text files takes in average about 10 seconds, respectively
it would be unwise to send a user request to the server every time for displaying the data. That is why, it is necessary to set up a rule for restarting the function anyway for restarting parser and saving user from wasting time.

Function update interval is about 25 minutes, cause noticed that the most frequently updating element of the text file is the time (30 min).
The data was collected using the requests library and passed to the JSON processing function due to a technical limitation
Flask and make to give global variables list.

The second server component is responsible for processing the collected information in a format that is convenient for displaying on the html page.
The source format is in the form of a string in JSON format, decoded into a list consisting of strings. There are not enough tags in the source files (Name:), 
therefore, they were added using the re regular expression tool. Next, a dictionary is created, the key to which is
is the METAR code and the value is a list of strings. Also using regular expressions
the values of temperature, wind, atmospheric pressure (Option 9). 

Handled values were matched to the condition and sent by the REST API from the client-per-client in a JSON array of strings. The data is displayed on the html page that is generated Flask routes


Client
----------- 
The client is a selectbox, which lists all the options of METAR codes.
When user clicks on a selectbox element, JQuery sends a POST request to the server with information about the number of the element. 
Selectbox can be controlled with arrow keys. Requested information, and 
conclusions on it is displayed on the right side of the page as text. The source code for the select boxes were taken from the portal of W3C on the rights of open source.


What is next?
-----------
Web service with a relatively complex structure and dynamically displayed content was developed.
Iterations are planning to tighten the design of the client part, as well as add new functionality.


Cnangelog
----------

1.0 - release
1.1 - fixed bugs for Firefox

Vadim Kropotin
kropvad@gmail.com
https://github.com/supahero