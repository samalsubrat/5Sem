#!/bin/bash

# Check if exactly three arguments are provided
if [[ $# -ne 3 ]]; then
    echo "Invalid input. Please provide three arguments: op1 operator op2"
    exit 1
fi

# Assign arguments to variables
op1="$1"
operator="$2"
op2="$3"

# Perform the calculation based on the operator
case "$operator" in
    +)
        result=$((op1 + op2))
        ;;
    -)
        result=$((op1 - op2))
        ;;
    \*)
        result=$((op1 * op2))
        ;;
    /)
        if [[ "$op2" -eq 0 ]]; then
            echo "Error: Division by zero is not allowed."
            exit 1
        else
            result=$((op1 / op2))
        fi
        ;;
    %)
        if [[ "$op2" -eq 0 ]]; then
            echo "Error: Modulus by zero is not allowed."
            exit 1
        else
            result=$((op1 % op2))
        fi
        ;;
    ^)
        result=$((op1 ** op2))
        ;;
    *)
        echo "Invalid operator. Please use + - * / % ^"
        exit 1
        ;;
esac

# Output the result
echo "$op1 $operator $op2 = $result"

