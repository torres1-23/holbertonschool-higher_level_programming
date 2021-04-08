#!/bin/bash
# Script that sends a JSON POST request to a URL passed as the first argument, and displays the body of the response.
curl -sH "Content-Type: application/json" -d "data=@"$2" "$1"
