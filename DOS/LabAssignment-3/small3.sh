#!/bin/bash
echo "Enter first number: "
read first
echo "Enter second number: "
read second
echo "Enter third number: "
read third

if (( first <= second && first <= third )); then
    echo "$first is the smallest."
elif (( second <= first && second <= third )); then
    echo "$second is the smallest."
else
    echo "$third is the smallest."
fi

