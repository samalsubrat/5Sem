#!/bin/bash
echo "Enter two numbers:"
read num1 num2
echo "Addition: $(echo "$num1 + $num2" | bc)"
echo "Subtraction: $(echo "$num1 - $num2" | bc)"
echo "Multiplication: $(echo "$num1 * $num2" | bc)"
echo "Division: $(echo "scale=2; $num1 / $num2" | bc)"

