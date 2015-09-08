
#! /bin/bash


#cgi file that controls the login information for the web application

echo "X-COMP-490: ${USER}"
echo "Content-type: text/html"
echo ""


USERNAME='echo "$QUERY_STRING" | sed -n
's/^.*username=\([^&]*\).*$/\1/p' | sed "s/%20/&/ /g"

PASSWORD='echo "$QUERY_STRING" | sed -n
's/^.*password=\([^&]*\).*$/\1/p' | sed "s/%20/&/ /g"

WHATTODO='echo "$QUERY_STRING" | sed -n
's/^.*whatToDo=\([^&]*\).*$/\1/p' | sed "s/%20/&/ /g"

echo "<html><head><title>What You Said</title></head>"
echo "<body>Here's what you said:
echo "You entered $USERNAME for username and $PASSWORD for password and wanted the action to be
$ACTION.
