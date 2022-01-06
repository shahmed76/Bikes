import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
days=['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']
months=['January', 'February', 'march', 'april', 'may', 'june', 'all']

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
    city_name = ''
    while city_name.lower () not in CITY_DATA:
        city_name = input ("\ n What is city's name? (E.g. Input either chicago, new york city, washington) \ n")
        if city_name.lower () in CITY_DATA:
             # We were able to get the name of the city to analyze data.
             city = CITY_DATA [city_name.lower ()]
        else:
             # We were not able to get the name of the city to analyze data so we continue the loop.
            print ("Sorry we were not able to get the name of the city to analyze data, Please input either chicago, new york city or washington. \ n")


    # TO DO: get user input for month (all, january, february, ... , june)
    while month_name.lower () not in months:
         month_name = input ("\ nWhat is the name of the month to filter data? (E.g. Input either 'all' to apply no month filter or january, february, ..., june) \ n")
         if month_name.lower () in months:
             # We were able to get the name of the month to analyze data.
             month = month_name.lower ()
         else:
             # We were not able to get the name of the month to analyze data so we continue the loop.
             print ("Sorry we were not able to get the name of the month to filter data, Please input either 'all' to apply no month filter or january, february, ..., june. \ n")
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day_name = ''
    while day_name.lower () not in days:
        day_name = input ("\ nWhat is the name of the day to filter data? (E.g. Input either 'all' to apply no day filter or monday, tuesday, ... sunday) \ n")
        if day_name.lower () in days:
             # We were able to get the name of the month to analyze data.
             day = day_name.lower ()
        else:
             # We were not able to get the name of the month to analyze data so we continue the loop.
             print ("Sorry we were not able to get the name of the day to filter data, Please input either 'all' to apply no day filter or monday, tuesday, ... sunday. \ n")

        print ('-' * 40)
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
    df = pd.read_csv (CITY_DATA [city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df ['Start Time'] = pd.to_datetime (df ['Start Time'])
    df ['month'] = df ['Start Time']. dt.month
    df ['day_of_week'] = df ['Start Time']. dt.day_name


    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        month = months.index(month)

    # filter by day of week if applicable

    if day !='all':
        df = df [df ['day_of_week'] == day]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    df ['month'] = df ['Start Time']. dt.month
    common_month= df ['month']. mode () [0]
    print ("The most common month is:" + months [common_month].title ())


# display the most common day of week
    df ['day_of_week'] = df ['Start Time'].dt.week
    common_day_of_week = df ['day_of_week'].mode () [0]
    print (common_day_of_week)


# display the most common start hour
    df ['hour'] = df ['Start Time'].dt.hour
    comm_h= df ['hour'].mode () [0]
    print (comm_h)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print ("The most commonly used start station is", df ['Start Station']. mode () [0], "\ n")

    # TO DO: display most commonly used end station
    print ("The most commonly used end station is", df ['End Station']. mode () [0], "\ n")

    # TO DO: display most frequent combination of start station and end station trip
    df ['combination'] = df ['Start Station'] + '' + df ['End Station']
    print ("The most frequent combination of start station and end station trip is:", df ('combination'). mode () [0])


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print("The total travel time is: " + str(total_travel_time))


    # TO DO: display mean travel time
    print ("Mean time is", df ['Trip Duration']. mean ())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)




def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df.groupby (['User Type']) ['User Type']. count ()
    print (user_types, "\ n")


    # TO DO: Display counts of gender
    gendergender = df.groupby (['Gender']) ['Gender']. count ()
    print (gendergender)


    # TO DO: Display earliest, most recent, and most common year of birth
    mr = sorted (df.groupby (['Birth Year']) ['Birth Year'], reverse = True) [0] [0]
    ey = sorted (df.groupby (['Birth Year']) ['Birth Year']) [0] [0]
    mc = df ['Birth Year']. mode () (0)
    print ("The earliest year of birth is", ey, "\ n")
    print ("The most recent year of birth is", mr, "\ n")
    print ("The most common year of birth is", mc, "\ n")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def individual_data(df):
    # Ask user if they want to see individual trip data.
    start_data = 0
    end_data = 5
    df_length = len(df.index)

    while start_data < df_length:
        raw_data = input("\nWould you like to see individual trip data? Enter 'yes' or 'no'.\n")
        if raw_data.lower() == 'yes':

            print("\nDisplaying only 5 rows of data.\n")
            if end_data > df_length:
                end_data = df_length
            print(df.iloc[start_data:end_data])
            start_data += 5
            end_data += 5
        else:
            break

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        individual_data (df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
