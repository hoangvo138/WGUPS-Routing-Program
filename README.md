# Data Structures and Algorithms II – C950
# WGUPS Routing Program
This is a WGU project in Data Structures and Algorithms II course, which solves a package delivery routing problem. This problem is a different version of the TSP problem. 

In this problem, I implemented the greedy algorithm as my solution to calculate the shortest distance to deliver all packages based on its specific requirements. The total distance to deliver 40 packages was 104.9 miles and the time complexity of greedy algorithm in this project is `O(n^2)`.

## Scenario
The Western Governors University Parcel Service (WGUPS) needs to determine the best route and delivery distribution for their Daily Local Deliveries. 

The Salt Lake City DLD route has three trucks, two drivers, and an average of 40 packages to deliver each day; each package has specific criteria and delivery requirements.

Write a program in Python language that determines and presents a solution delivering all 40 packages on time, according to their criteria while reducing the total number of miles traveled by the trucks. The “Salt Lake City Downtown Map,” provides the location of each address, and the “WGUPS Distance Table” provides the distance between each address.

The supervisor (user) should be able to check the status of any given package at any given time using package IDs, including the delivery times, which packages are at the hub, and which are en route. The intent is to use this program for this specific location and to use the same program in different cities as WGUPS expands its business.

## Assumptions
- All 40 packages must be delivered with the total distance under 140 miles.
- Two drivers and three trucks are available. So no more than two trucks can be away from the hub at the same time.
- The trucks move at a constant speed of 18 miles per hour.
- Trucks can carry a maximum of 16 packages.
- Trucks can leave the hub no sooner than 8:00 a.m.
- Packages can only be loaded onto a truck at the hub.
- You only need to account for the time spent driving. You can ignore the time spent on all other activities, such as loading trucks and dropping off packages.
- The wrong delivery address for package #9, Third District Juvenile Court, will be corrected at 10:20 a.m. The correct address is “410 S State St., Salt Lake City, UT 84111”. You may assume that WGUPS knows the address is incorrect and when it will be corrected.
- Packages #13, #14, #15. #16, #19, and #20 must go out for delivery on the same truck at the same time.
- Packages #3, #18, #36 and #38 can only be loaded on truck 2.
- #6, #25, #28, #32 cannot leave the hub before 9:05 a.m.

## Requirements
```text
Your submission must be your original work. No more than a combined total of 30% of the submission and no more than a 10% match to any one individual source can be directly 
quoted or closely paraphrased from sources, even if cited correctly. An originality report is provided when you submit your task that can be used as a guide.

You must use the rubric to direct the creation of your submission because it provides detailed criteria that will be used to evaluate your work. Each requirement below may be 
evaluated by more than one rubric aspect. The rubric aspect titles may contain hyperlinks to relevant portions of the course.

Section 1: Programming/Coding

A. Identify the algorithm that will be used to create a program to deliver the packages and meets all  requirements specified in the scenario.
    
B. Write a core algorithm overview, using the sample given, in which you do the following:      
	1. Comment using pseudocode to show the logic of the algorithm applied to this software solution.     
	2. Apply programming models to the scenario.      
	3. Evaluate space-time complexity using Big O notation throughout the coding and for the entire program.
	4. Discuss the ability of your solution to adapt to a changing market and to scalability.
	5. Discuss the efficiency and maintainability of the software.
	6. Discuss the self-adjusting data structures chosen and their strengths and weaknesses based on the scenario.
    
C. Write an original code to solve and to meet the requirements of lowest mileage usage and having all  packages delivered on time.
	1. Create a comment within the first line of your code that includes your first name, last name, and student ID.
	2. Include comments at each  block of code to explain the process and flow of the coding.
	
D. Identify a data structure that can be used with your chosen algorithm to store the package data.
	1. Explain how your data structure includes the relationship between the data points you are storing.

Note: Do NOT use any existing data structures. You must design, write, implement, and debug all code that you turn in for this assessment. Code downloaded from the internet or acquired from another student or any other source may not be submitted and will result in automatic failure of this assessment.

E. Develop a hash table, without using any additional libraries or classes, with an insertion function that takes the following components as input and inserts the components into the hash table:
	• package ID number
	• delivery address
	• delivery deadline
	• delivery city
	• delivery zip code
	• package weight
	• delivery status (e.g., delivered, in route)

F. Develop a look-up function that takes the following components as input and returns the corresponding data elements:
	• package ID number
	• delivery address
	• delivery deadline
	• delivery city
	• delivery zip code
	• package weight
	• delivery status (e.g., delivered, in route)

G. Provide an interface for the insert and look-up functions to view the status of any package at any time. This function should return all information about each package, including delivery status.
	1. Provide screenshots to show package status of all packages at a time between 8:35 a.m. and 9:25 a.m.
	2. Provide screenshots to show package status of all packages at a time between 9:35 a.m. and 10:25 a.m.
	3. Provide screenshots to show package status of all packages at a time between 12:03 p.m. and 1:12 p.m.

H. Run your code and provide screenshots to capture the complete execution of your code.

Section 2: Annotations

I. Justify your choice of algorithm by doing the following:
	1. Describe at least  two strengths of the algorithm you chose.
	2. Verify that the algorithm you chose meets all  the criteria and requirements given in the scenario.
	3. Identify two other algorithms that could be used and would have met the criteria and requirements given in the scenario.
		a. Describe how each algorithm identified in part I3 is different from the algorithm you chose to use in the solution.

J. Describe what you would do differently if you did this project again.

K. Justify your choice of data structure by doing the following:
	1. Verify that the data structure you chose meets all  the criteria and requirements given in the scenario.
		a. Describe the efficiency of the data structure chosen.
		b. Explain the expected overhead when linking to the next data item.
		c. Describe the implications of when more package data is added to the system or other changes in scale occur.
	2. Identify two other data structures that can meet the same criteria and requirements given in the scenario.
		a. Describe how each data structure identified in part K2 is different from the data structure you chose to use in the solution.

L. Acknowledge sources, using in-text citations and references, for content that is quoted, paraphrased, or summarized.

M. Demonstrate professional communication in the content and presentation of your submission.
```

## Documentation
The documentation docx file for this project can be found in the main repository, named "Code documentation".
