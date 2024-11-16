echo "Enter internal marks"
read marks
echo "Enter attendance in percentage"
read att

if((marks >= 20 && att >= 75)); then
	echo "Allowed for Semester"
else
	echo "Not allowed for Semester"
fi
