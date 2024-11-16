echo "Enter a 5 digit number: "
read num
sum=$((sum + num%10))
num=$((num/10))
sum=$((sum + num%10))
num=$((num/10))
sum=$((sum + num%10))
num=$((num/10))
sum=$((sum + num%10))
num=$((num/10))
sum=$((sum + num%10))
num=$((num/10))

echo "The sum of all digits is: $sum"
