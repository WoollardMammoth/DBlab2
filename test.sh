#!/bin/bash


for num in {4..11}
do
	echo Running Test_R${num}
	python schoolsearch.py -t < ./Tests/Input/Test_R${num} > ./Tests/MyOut/Test_R${num}_MyOutput
done 

for num in {4..11}
do 
	echo Diff Output Test_R${num} vs. Test_R${num}_MyOutput
	diff ./Tests/ExpectedOut/Test_R${num}_Output ./Tests/MyOut/Test_R${num}_MyOutput
done 