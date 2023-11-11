#!/bin/bash

filename="daily_job.log"

if [ -e "$filename" ]; then
    line_count=$(wc -l < "$filename")
    echo "$line_count"
    if [ "$line_count" -gt 40 ]; then
        echo -n > "$filename"
        # echo "File emptied because it contains 30 lines."
    # else
    #     echo "File does not contain 30 lines. Nothing emptied."
    fi
else
    # echo "File does not exist. Creating it."
    touch "$filename"
    # Add any initial content or setup here if needed
fi

