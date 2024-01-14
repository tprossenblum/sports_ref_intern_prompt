# sports_ref_intern_prompt

Simple code sample that reads a json file to display a head to head matrix

# Description

1. Code starts by reading the json file that stores the data we want to manipulate. Once the json file is read we store the data and retrieve the keys in a list to later loop through each team. 

2. To display the matrix we need an initial header and then each row so we initialize the string and then loop through each team. In the initial loop we add the team to the header row and adjust spacing as well as adding the same team to the initial column. 

3. Once we initalize the first part we complete the row by nesting a loop that iterates through results of team i. We first check if i is equal to j to skip as that would mean it was the same team playing each other, after we adress that case we append the appropriate win amount to the row, once all matchups are accounted for we go on to the next team. 

4. After the loop completes we print out the header and rows and the matrix is displayed.

## Usage

Files: 
- sport_ref.json
- sports_ref_prompt.py

'''python
import json

Have both files located in the same heirarchy and run the .py file

# Result
![image](https://github.com/tprossenblum/sports_ref_intern_prompt/assets/149984771/9abfa73a-2ea7-4558-b38f-4ee8fa7fb3a5)


# Contact

Thomas Rossenblum
tprossenblum03@gmail.com
(424) 347-0749
