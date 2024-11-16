echo "Enter a day (Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday):"
read day
case "$day" in
    Monday)
      echo "DOS Class Time: 10:00 AM - 12:00 PM"
      echo "Room: A101"
      ;;
    Tuesday)
      echo "DOS Class Time: 2:00 PM - 4:00 PM"
      echo "Room: B202"
      ;;
    Wednesday)
      echo "DOS Class Time: 10:00 AM - 12:00 PM"
      echo "Room: C303"
      ;;
    Thursday)
      echo "DOS Class Time: 2:00 PM - 4:00 PM"
      echo "Room: D404"
      ;;
    Friday)
      echo "DOS Class Time: 10:00 AM - 12:00 PM"
      echo "Room: E505"
      ;;
    Saturday)
      echo "No class on Saturday"
      ;;
    Sunday)
      echo "Holiday"
      ;;
    *)
      echo "Invalid day. Please enter a valid weekday."
      ;;
esac
