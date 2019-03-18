import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
citynames = ['chicago', 'new york city', 'washington']
months = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday','all']
def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')

    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    print('Would you like to see data for Chicago, New York City or Washington ?')
    def cityname():
        city = str(input('Type city name :'))
        if city not in citynames:
            print('Please select correct city among Chicago, New York City or Washington.')
            city = cityname()
        return city
    city = cityname()

    # get user input for month (all, january, february, ... , june)
    print('Select a month january, february, march, april, may, june or all ?')
    def monthname():
        month = str(input('Type month :'))
        if month not in months:
            print('Please select correct month among january, february, march, april, may, june or all ?.')
            month = monthname()
        return month
    month = monthname()

    # get user input for day of week (all, monday, tuesday, ... sunday)
    print('Select a day monday, tuesday, wednesday, thursday, friday, saturday, sunday or all ?')
    def dayname():
        day = str(input('Type day :'))
        if day not in days:
            print('Please select correct day among january, february, march, april, may, june or all ?.')
            day = dayname()
        return day
    day = dayname()

    print('-'*40)
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
     # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    #df['Birth Year'].fillna(0,inplace = True)
    return df



def time_stats(orignal_df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month

    orignal_df['month'] = pd.DatetimeIndex(orignal_df['Start Time']).month

    months_count = orignal_df['month'].value_counts()

    maxV = months_count.idxmax()
    months = ['january', 'february', 'march', 'april', 'may', 'june']
    print('Most common month is {} and count is {}.'.format((months[maxV-1]).title(),months_count.max()))

    # display the most common day of week
    orignal_df['Week Day'] = pd.DatetimeIndex(orignal_df['Start Time']).weekday_name
    days_count = orignal_df['Week Day'].value_counts()

    maxDay = days_count.idxmax()

    days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    print('Most common day of week is {} and count is {}.'.format(maxDay.title(),days_count.max()))



    # display the most common start hour

    orignal_df['Hours'] = pd.DatetimeIndex(orignal_df['Start Time']).hour
    hours_count = orignal_df['Hours'].value_counts()

    print('Most common hour is {} and count : {}'.format(hours_count.idxmax(),hours_count.max()))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    Start_Station_counts = df['Start Station'].value_counts()
    print('Most commonly used start station is "{}" and count : {}'.format(Start_Station_counts.idxmax(),Start_Station_counts.max()))
    # display most commonly used end station
    End_Station_counts = df['End Station'].value_counts()
    print('Most commonly used end station is "{}" and count : {}'.format(Start_Station_counts.idxmax(),End_Station_counts.max()))
    # display most frequent combination of start station and end station trip
    df['Start End stations'] = df['Start Station'] + df['End Station']
    Start_End_Station = df['Start End stations'].value_counts()

    print('Most commonly used start station and end station is "{}" and counts :"{}".'.format(Start_End_Station.idxmax(),Start_End_Station.max()))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_time_sum = df['Trip Duration'].sum()
    print('Total travel time is {}.'.format(total_time_sum))
    # display mean travel time
    total_time_mean = df['Trip Duration'].mean()
    print('Total traveling mean time is {}.'.format(total_time_mean))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    count_user = df['User Type'].value_counts()
    print('Total Counts of user type are {}.'.format(count_user))
    # Display counts of gender
    df['Gender'].fillna('Not given',inplace=True)
    count_user_gender = df['Gender'].value_counts()
    print('Total Counts of user Gender type are {}.'.format(count_user_gender))


    # Display earliest, most recent, and most common year of birth
    birth_year = df['Birth Year'].value_counts()
    if city == 'new york city' or city== 'washington':
        print('Birth Year is not present for this city {}.'.format(city))

    if city == 'chicago':

        print('Earliest, most recent, and most common year of births are "{}", "{}" and "{}" of {}.'.format(birth_year.idxmin(),df['Birth Year'].iloc[0], birth_year.idxmax(),city))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        orignal_df = pd.read_csv(CITY_DATA[city])
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
