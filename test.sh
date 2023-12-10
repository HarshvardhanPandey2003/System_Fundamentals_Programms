
# echo "Enter a File Name :"
# read filename

# words=$(wc -w < "$filename")

# echo "Words are "$words
echo "Enter a Number :"
read n
is_prime=1

for ((i=2;i<n/2;i++));
do
    if [ $((n % i)) -eq 0 ]; then 
        is_prime=0
        break
    fi
done

if [ $is_prime -eq 1 ];
then
    echo " Number $n is a Prime Number  "
else
    echo " Number $n is not a Prime Number  "
fi
