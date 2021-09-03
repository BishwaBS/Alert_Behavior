**Introduction:**
This package alerts the users whey they happen to touch their mouth and nose 
while working in the computers. Some people develop some unwanted habits such as
nose picking and nail biting while working all day long in computer without thier attention. This package 
can help them destroy such habits by alerting right on time. This package bears more importance in the light of ongoing COVID pandemic.

**Pre-requisites:**
You should have webcam connected to your computer and should be fully functional. You also should have python install in the computer. You can check this video to install python if you do not have it already. https://www.youtube.com/watch?v=4Rx_JRkwAjY&ab_channel=ProgrammingKnowledge2 https://www.youtube.com/watch?v=4gTCQCT_930&ab_channel=TechMeSpot

**Concept:**
There is a really good package for face and hand detection called "mediapipe". This package detects landmarks in face and fingers. These landmarks have unique ids and acquire local image coordinates. The distance between these landmarks can be calculated and analyzed to perform certain tasks such as this

**Steps:**
1.  open up your terminal by typing `cmd` on the navigation address within the folder where you want to download/clone the code from github
2.  clone the github repository by pasting this command  `git clone https://github.com/BishwaBS/Alert_Behavior.git`
3.  change the working directory to Alert_Behavior  `cd Alert_Behavior`
4.  run the setup file found within the Alert_Behavior `python setup.py install`
5.  open up the python program by typing `python`
6.  type `import Alert_Behavior`
7.  type `from Alert_Behavior import alert`
8.  type `alert.start_session().start_alert()`
9.  Yayy! if you see the webcam video launched in imaging window, you successfully started the session. You can try by moving your fingers near to nose and mouth and you will hear the beep sound. If you have a habit of touching nose and mouth with your fingers, this annoying beep sound will deter you from doing that

