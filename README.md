# NISBXtreme 2020

## Overview :	
This repository contains the questions and solutions to the problems asked during NISBXtreme on 24th August 2020.    
Sameple scripts used to generate the test cases are also included.		
<br><br>

## Folder structure :
- Each question has the following folder structure :   
	```
	./Question N
		├── question.txt 
		├── solution.<cpp/py>
		└── generateTestCases.py
	```

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
  - Linus / MacOs
    - ```bash
		$ python3 solution.py
		```
