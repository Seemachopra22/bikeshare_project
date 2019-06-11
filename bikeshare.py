import time
import pandas as pd
import numpy as np

print("provide information about CITY_DATA, months and days!")
CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
months = ['january','february','march','april','may','june', 'all']
days = ['monday','tuesday','wednesday','thursday','friday','saturday','sunday', 'all']



def get_filters():
    global city, month, day


    """
    Asks user to specify a city, month and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input("Select a city from {}, {} or {}:".format(*CITY_DATA.keys())).strip().lower()
        if city in CITY_DATA.keys():
            break


    # TO DO: get user input for month (all, january, february, ... , june)
    month = user_input('Enter the name of the month to analysed {}:'.format(months)).strip().lower()




    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = user_input('Enter name of the day of week to analyzed {}:'.format(days)).strip().lower()







    print('-'*40)
    return city, month, day


def load_data(city, month, day):

    """
    Loads data for the specified city and filters by month, day and hour if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
        (str) hour - common hour in the day
    Returns:
        df - Pandas DataFrame containing city data filtered by month, day and hour
    """
    # load data into dataframe
    df = pd.read_csv(CITY_DATA[city])
    # convert the starttime column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # extract month, day of week and hour from start time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[ df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    most_common_month = df['month'].value_counts().idxmax()
    print('Most common month: {}'.format(most_common_month))

    # TO DO: display the most common day of week
    most_common_day_of_week = df['day_of_week'].value_counts().idxmax()
    print('Most common day of week: {}'.format(most_common_day_of_week))


    # TO DO: display the most common start hour
    most_common_hour = df['hour'].value_counts().idxmax()
    print('Most common start hour: {}'.format(most_common_hour))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_common_station = df['Start Station'].value_counts().idxmax()
    print('Most commonly used start station: {}'.format(most_common_station))


    # TO DO: display most commonly used end station
    most_common_end_station = df['End Station'].value_counts().idxmax()
    print('Most commonly used end station: {}'.format(most_common_end_station))




    # TO DO: display most frequent combination of start station and end station trip
    most_common_start_end_station = df[['Start Station', 'End Station']].mode().loc[0]
    print('Most frequent combination of start and end station trip: {}'.format(most_common_start_end_station))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('Display total travel time:', total_travel_time)



    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('Display mean travel time:', mean_travel_time)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts
    print('Display counts of user types:', user_types)


    # TO DO: Display counts of gender
    try:
        genders = df['Gender'].value_counts
        print('Gender:', genders)


    except KeyError:
        print("There is not [Gender] column in this spreadsheet!")


    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        earliest_year_of_birth = df['Birth Year'].min()
        print('Birth Year:', earliest_year_of_birth)
        print()
    except KeyError:
        print("There is not [Birth Year] column in this spreadsheet!")
    try:
        recent_year_of_birth = df['Birth Year'].max()
        print('Birth Year:', recent_year_of_birth)
    except KeyError:
        print("There is not [Birth Year] column in this spreadsheet!")
    try:
        most_common_year_of_birth = df['Birth Year'].mode().loc[0]
        print('Birth Year:', most_common_year_of_birth )
    except KeyError:
        print("There is not [Birth Year] column in this spreadsheet!")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():

    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
