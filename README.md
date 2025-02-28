We created a software using python in which helps the visually impaired to guide throught the campus. Our software uses the voice recognition to help the 
user to take input of the start point and destination in which the software will guid the blind the person by telling the the number of steps to reach their
desired destination.
In the software we used python using its library (pygame), taking and guiding user through voice with the help of (speech_recognition as sr),(pyttx3) libraries.


FlowChart:
    +----------------------------+
| Start                      |
+----------------------------+
          |
          v
+----------------------------+
| Initialize Pygame & UI      |
+----------------------------+
          |
          v
+----------------------------+
| Initialize Speech & TTS     |
+----------------------------+
          |
          v
+----------------------------+
| Display Maze & Player      |
+----------------------------+
          |
          v
+----------------------------+
| Give Movement Instruction  |
| (TTS: "Move forward...")   |
+----------------------------+
          |
          v
+----------------------------+
| Wait for "Reached" Command |
| (Speech Recognition)       |
+----------------------------+
          |
          v
+----------------------------+
| Move Player Position       |
+----------------------------+
          |
          v
+----------------------------+
| Check if Last Instruction? |
+------------+---------------+
          | No |
          v
+----------------------------+
| Repeat from "Give Movement"|
+----------------------------+
          |
         Yes
          v
+----------------------------+
| Mark Final Position (Red)  |
+----------------------------+
          |
          v
+----------------------------+
| Announce Completion (TTS)  |
+----------------------------+
          |
          v
+----------------------------+
| Exit Game                  |
+----------------------------+