Order Processor Documentation

Algorithm and Approach:
This function determines the amount of days that it will take to produce an order based
on order quantity, processing time per item (in minutes), work shifts, and working days.
The expected completion date of the order is also returned by the function.
My approach was to break down the main problem into smaller problems:
1. The first of these smaller problems was to get the day of the week from the
start_date string. To do this, I used the datetime library which is part of the
standard Python library.
2. After tackling that, I needed to figure out how to process the work days and
shifts. I ended up using a while loop to continuously process shifts while
subtracting minutes from the total remaining minutes. The while loop breaks once
the total remaining minutes is 0 or less.
3. The third subproblem I addressed was keeping track of work days versus off
days. To accomplish this, I used a variable, curr_day, to track the current day of
the week. On each iteration of the while loop, curr_day is incremented by one
and wrapped back to 0 after Sunday (curr_day == 6).

Assumptions:
● Shifts occur within a single day, meaning that there would not be any overnight
work.
● order_quantity and processing_minutes_per_item must be greater than 0.
● Shifts should be passed as an array of objects, with fields for start_time and
end_time.
● Shifts should be longer than 0 minutes.
● That the format for start_date should be “YYYY-MM-DD”.
● That the format for shift start_time and end_time should be “HH:MM”.
● The exact time that the order is processed is not relevant, only the completion
date and calendar days taken matter.
● The start date is inclusive, meaning that it should be counted towards total
calendar days worked.

Edge Cases:
● Invalid data types being passed
● order_quantity being less than or equal to 0
● processing_minutes_per_item being less than or equal to 0
● working_days being empty
● shifts being empty
● Duplicate days in working_days
● start_date being formatted incorrectly
● Shift duration being less than or equal to 0 minutes
● Shift object not containing keys for start_time and end_time
● Wrong format for start_time and end_time

Usage:
Parameters:

order_quantity:
int 
The number of items to beprocessed.

processing_minutes_per_item:
int 
Amount of time in minutes that it takes to process one item.

shifts:
array of objects 
Working hours for the day.

working_days:
array of ints 
The days of the week inthat work occurs. 0-6 (Mon-Fri)

start_date:
str 
Starting date for the order formatted as “YYYY-MM-DD”.

Example Function Input:
OrderCalculator(200, 10, [{"start_time": "09:00", "end_time": "17:00"}], [0, 1, 3],
"2025-04-21"))
Example Function Output:
{'calendar_days': 9, 'completion_date': '2025-04-29'}
