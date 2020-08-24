# NISBXtreme 2020

## Overview :	
This repository contains the questions and solutions to the problems asked during NISBXtreme on 24th August 2020.    
Sample scripts used to generate the test cases are also included in some of the folders.		
<br><br>

## Folder structure :
- Each question has the following folder structure :   
	```
	./Question N
		├── Assets/ [ optional ]  
		├── question.txt 
		├── solution.<cpp/py> 
		└── generateTestCases.py [ optional ]
	```
	The Assets folder contains all the images / gifs used in problem.

- The root also contains a `requirements.txt` for the modules needed for the generation of test cases.

## Run :
- All cpp files were compiled and tested on `g++ v 7.5.0 ( Ubuntu 7.5.0-3ubuntu1~18.04 )`   
	- ```bash
		$ g++ solution.cpp -o solution.out && ./solution.out
		```
- All python solutions will work on `python 3.x` without any additonals modules to be installed
  - Windows: 
    -  ```bash
  		$ python solution.py
  		```
  - Linux / MacOs
    - ```bash
		$ python3 solution.py
		```

## Final Notes:   
There may be other faster and more efficient algorithms ,these are the solutions we came up with which can solve the hackerrank limits quite easily. Pull requests are always welcome.
