if [ $# -eq 0 ]; then
  echo "No file provided"
  exit 1
fi
file=$1
echo "Filename: $file"
echo "Line count: $(wc -l < $file)"
echo "Word count: $(wc -w < $file)"
echo "Char count: $(wc -m < $file)"
