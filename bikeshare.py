import time
import pandas as pd
import numpy as np

CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    city = input("please choose one of the following cities (chicago , new york city , washington) \n").lower()

    while city not in CITY_DATA.keys():
        print("ivalid input. please enter the name of the city again.\n")
        city = input("please choose one of the following cities (chicago , new york city , washington) \n").lower()

    # TO DO: get user input for month (all, january, february, ... , june)
    months = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
    month = input("choose a month from january to june OR type \"all\" if you want to check all those months\n").lower()

    while month not in months:
        print("invalid input. please try again.\n")
        month = input(
            "choose a month from january to june OR type \"all\" if you want to check all those months\n").lower()

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    days = ["saturday", "sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "all"]
    day = input("pick a day of the week (sunday, monday, ...etc) OR type \"all\" to check the whole week.\n").lower()

    while day not in days:
        print("invalid input. please try again.\n")
        day = input(
            "pick a day of the week (sunday, monday, ...etc) OR type \"all\" to check the whole week.\n").lower()

    print('-' * 40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])

    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['weekday'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour

    # filtering by month :

    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']

        month = months.index(month) + 1

        df = df[df['month'] == month]

    # filtering by weekday

    if day != 'all':
        df = df[df['weekday'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month

    most_common_month = df['month'].mode()[0]
    print("the most common month is : ", most_common_month)

    # TO DO: display the most common day of week

    most_common_day = df['weekday'].mode()[0]
    print("the most common day is : ", most_common_day)

    # TO DO: display the most common start hour

    most_common_Starting_hour = df['hour'].mode()[0]
    print("the most common starting hour is : ", most_common_Starting_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station

    most_common_start_station = df['Start Station'].mode()[0]
    print("the most popular start station is : ", most_common_start_station)

    # TO DO: display most commonly used end station

    most_common_end_station = df['End Station'].mode()[0]
    print("the most common end station is : ", most_common_end_station)

    # TO DO: display most frequent combination of start station and end station trip

    df['path'] = df['Start Station'] + "," + df['End Station']
    print("the most common route is : ", df['path'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time

    total_travel_time = df['Trip Duration'].sum().round()

    print("the total travelling time is : ", total_travel_time / 3600, "hours")

    # TO DO: display mean travel time

    mean_travel_time = df['Trip Duration'].mean().round()
    print("the average travelling time is : ", mean_travel_time / 60, "minutes")

    # to display the longest trip time

    longest_trip = df['Trip Duration'].max().round()
    print("the longest trip takes : ", longest_trip / 3600, "hours")

    # to display the shortest trip

    shortest_trip = df['Trip Duration'].min().round()
    print("the shortest trip takes : ", shortest_trip / 60, "minutes")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    print('\nUser Type Stats:\n')
    # TO DO: Display counts of user types

    user_types_count = df['User Type'].value_counts().to_frame()
    print(user_types_count)

    # TO DO: Display counts of gender

    if city != 'washington':
        print("\ngender counts :\n")
        counts_of_gender = df['Gender'].value_counts().to_frame()
        print(counts_of_gender)

        # TO DO: Display earliest, most recent, and most common year of birth

        print("\nbirth year stats :\n")

        most_common_year = df['Birth Year'].mode()[0]

        print('most common year of birth is :', most_common_year)

        most_recent_year = df['Birth Year'].max()

        print('most recent year of birth is :', most_recent_year)

        earliest_year = df['Birth Year'].min()

        print('earliest year of birth is :', earliest_year)

    else:

        print("\ngender and birth year data is not available for the city you chose\n")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def display_raw_data(df):
    # gives the user the option to inspect raw data 5 rows at a time

    print("\n you have the option to check out some raw data \n")

    i = 0
    option = input("\nwould you like to look into 5 rows of raw data? (please type in \"yes\" or \"no\" )\n").lower()

    if option not in ["yes", "no"]:

        print("invalid input. please try again\n")
        option = input(
            "\nwould you like to look into 5 rows of raw data? (please type in \"yes\" or \"no\" )\n").lower()

    elif option != "yes":

        print("thank you")

    else:

        while i + 5 < df.shape[0]:

            print(df.iloc[i:i + 5])

            i += 5

            option = input("do you want to display 5 more rows of data? (please type in \"yes\" or \"no\" )\n").lower()

            if option != "yes":
                print("thank you")

                break


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)
        display_raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()