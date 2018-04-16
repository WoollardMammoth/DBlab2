#!/bin/bash

## Lab 1-2 Test
for num in {1..5}
do 
	echo Running Test_NR${num}
	python schoolsearch.py -t < ./Tests/Input/Test_NR${num} > ./Tests/MyOut/Test_NR${num}_MyOutput
done 

for num in {1..5}
do 
	echo Diff: Test_NR${num}_Output vs. Test_NR${num}_MyOutput
	diff -y ./Tests/ExpectedOut/Test_NR${num}_Output ./Tests/MyOut/Test_NR${num}_MyOutput
done 


## Lab1-1 Tests
for num in {4..11}
do
	echo Running Test_R${num}
	python schoolsearch.py -t < ./Tests/Input/Test_R${num} > ./Tests/MyOut/Test_R${num}_MyOutput
done 

for num in {4..11}
do 
	echo Diff:  Test_R${num}_Output vs. Test_R${num}_MyOutput
	diff -y ./Tests/ExpectedOut/Test_R${num}_Output ./Tests/MyOut/Test_R${num}_MyOutput
done 

