from datetime import datetime
from datetime import timedelta


def order_calculator(order_quantity, processing_minutes_per_item, shifts, working_days, start_date):
    """
    Returns the calendar days an order will take to complete along with the expected date of completion.

    :param int order_quantity: The number of items to be processed
    :param int processing_minutes_per_item: Amount of time in minutes that it takes to process one item
    :param list[dict] shifts: Working hours for the day
    :param list[int] working_days: The days of the week in that work occurs
    :param str start_date: Starting date for the order formatted as 'YYYY-MM-DD'

    :return: A dictionary with two keys:
        calendar_days: The number of calendar days taken to complete the order
        completion_date: The date when the order will be completed
    """
    minutes_to_complete = processing_minutes_per_item * order_quantity

    # validate input types
    if type(order_quantity) != int:
        return 'Error: order_quantity must be of type int'
    if type(processing_minutes_per_item) != int:
        return 'Error: processing_minutes_per_item must be of type int'
    if not all(isinstance(x, int) and 0 <= x <= 6 for x in working_days):
        return 'Error: elements in working_days must be of type int from 0 to 6'
    if type(start_date) != str:
        return 'Error: start_date must be of type str'

    # handle edge cases
    if order_quantity <= 0 and processing_minutes_per_item <= 0:
        return 'Error: order quantity and processing time must be greater than 0'
    if order_quantity <= 0:
        return 'Error: order quantity must be greater than 0'
    if processing_minutes_per_item <= 0:
        return 'Error: processing time must be greater than 0'
    if len(working_days) <= 0 and len(shifts) <= 0:
        return 'Error: specify working days and shifts'
    if len(working_days) <= 0:
        return 'Error: specify working days'
    if len(shifts) <= 0:
        return 'Error: specify shifts'

    # check for duplicates in working_days
    if len(working_days) != len(set(working_days)):
        return 'Error: working_days cannot contain duplicates'

    # edge cases for start date
    try:
        datetime.strptime(start_date, '%Y-%m-%d')
    except ValueError:
        return 'Error: start_date must be in format: "YYYY-MM-DD"'

    else:
        days = 0

        # initialize day and date
        curr_date = datetime.strptime(start_date, '%Y-%m-%d')
        curr_day = curr_date.weekday()

        while minutes_to_complete > 0:
            # if there is work today
            if curr_day in working_days:
                # process shifts for day
                for shift in shifts:
                    try:
                        start_time = datetime.strptime(shift['start_time'], '%H:%M')
                        end_time = datetime.strptime(shift['end_time'], '%H:%M')
                    # catch edge case errors
                    except TypeError:
                        return 'Error: shift start_time and end_time must be of type str'
                    except ValueError:
                        return 'Error: shift start_time and end_time must follow format "HH:MM"'
                    except KeyError:
                        return 'Error: shift object must include keys "start_time" and "end_time"'

                    shift_minutes = (end_time - start_time).seconds / 60

                    if shift_minutes <= 0:
                        return 'Error: shift start and end time cannot be the same'

                    minutes_to_complete -= shift_minutes

            if curr_day == 6:
                curr_day = 0
            else:
                curr_day += 1

            days += 1

        end_date = curr_date + timedelta(days=days - 1)  # subtract 1 from days to include start date

        return {
            'calendar_days': days,
            'completion_date': str(end_date.date())
        }
