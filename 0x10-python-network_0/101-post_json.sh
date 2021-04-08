#!/bin/bash
# Script that sends a JSON POST request to a URL passed as the first argument, and displays the body of the response.
curl -X POST --data-binary @"$2" "$1"
