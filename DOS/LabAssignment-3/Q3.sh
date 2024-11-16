echo "Enter basic salary: "
read bas

dear=$((40 * bas / 100))
house=$((20 * bas / 100))
gross=$((bas - dear - house))

echo "Gross salary is: $gross"
