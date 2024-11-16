#!/bin/bash
echo "Enter cost price"
read cp
echo "Enter sell price"
read sep

if (( sep > cp )); then
    profit=$(( sep - cp ))
    echo "Net profit is: $profit"
else
    loss=$(( cp - sep ))
    echo "Net loss is: $loss"
fi

