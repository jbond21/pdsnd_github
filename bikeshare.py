import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

days = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'all']

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
    city = input('Which city would you like to analyze? chicago, new york city, or washington ')
    if city.lower() in CITY_DATA.keys():
        print('The chosen city is' +' '+ city)
    else:
        print('Incorrect City. Try again')
        city = input('Which city would you like to analyze? chicago, new york city, or washington ')
        print('The chosen city is' +' '+ city)
    # TO DO: get user input for month (all, january, february, ... , june)
    months = ['january', 'feburary', 'march', 'april', 'may', 'june' ,'all']
    month = input('What month would you like to analyze? Type month or Type all for all months ')
    if month.lower() in months:
        print('You selected' +' '+ month)
    else:
        print('Incorrect Month. Try again')
        month = input('What month would you like to analyze? Type month or Type all for all months ')
        print('You selected' +' '+ month)
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    days = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'all']
    day = input('What day would you like to analyze? Type day or Type all for every day ')
    if day.lower() in days:
        print('You selected' +' '+ day)
    else:
        print('Incorrect Day. Try again')
        day = input('What day would you like to analyze? Type day or Type all for every day ')
        print('You selected' +' '+ day)
    print('-'*40)
    return city.lower(), month.lower(), day.lower()

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
    df['Filter Month'] = df['Start Time'].dt.month
    df['Filter Day'] = df['Start Time'].dt.strftime('%A').str.lower()
    #print(df['Filter Month'])
    #print(df['Filter Day'])
    print(df.columns)
    
    if month != 'all':
        filter_month = {'january': 1, 'february': 2, 'march': 3, 'april': 4, 'may': 5, 'june': 6}
        filtered_month = filter_month[month]
        #print('this is')
        #print(filtered_month)
        df = df.loc[df['Filter Month'] == filtered_month]

    if day != 'all':
        df = df.loc[df['Filter Day'] == day]
    
           
    
    
            

    
    
    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    
    

    # TO DO: display the most common month
    #print(df['Start Time'].dt.month)
    common_month = df['Start Time'].dt.month.mode()[0]
    print('The most common month is:' + ' ' + str(common_month))

    # TO DO: display the most common day of week
    common_day = df['Start Time'].dt.strftime('%A').mode()[0]
    print('The most common day is:' + ' ' + str(common_day))


    # TO DO: display the most common start hour
    common_hour = df['Start Time'].dt.hour.mode()[0]
    print('The most common hour is:' + ' ' + str(common_hour))



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    
   
    
    # TO DO: display most commonly used start station
    start_station_count = df['Start Station'].value_counts()
    #print(start_station_count)
    start_station = (df['Start Station'].mode()[0])
    print('The most common start station is:' + ' ' + str(start_station))
    

    # TO DO: display most commonly used end station
    #end_station_count = df['End Station'].value_counts()
    #print(end_station_count)
    end_station = df['End Station'].mode()[0]
    print('The most common end station is:' + ' ' + str(end_station))

    # TO DO: display most frequent combination of start station and end station trip
    df['combo'] = df['Start Station'] + '_' + df['End Station']
    
    combo = df['combo'].mode()[0]
    print('The combination of most common start and end stations are:' + ' ' + str(combo))

    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('The total amount of time spent on bicycles is:' + ' ' + str(total_travel_time))


    # TO DO: display mean travel time
    total_mean_time = df['Trip Duration'].mean()
    print('The average amount of time spent on bicycles is:' + ' ' + str(total_mean_time))
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print('Below shows the count of User Types')
    user_count = df['User Type'].value_counts()
    print(user_count)
    print('-'*40)
    # TO DO: Display counts of gender
    print("Below shows the count of User's Sex")
    gender_count = df['Gender'].value_counts()
    print(gender_count)
    print('-'*40)
    # TO DO: Display earliest, most recent, and most common year of birth
    birth_min = df['Birth Year'].min()
    print('The oldest person to ride was born in:' + ' ' + str(birth_min))
    
    birth_max = df['Birth Year'].max()
    print('The youngest person to ride was born in:' + ' ' + str(birth_max))
    
    #df.fillna(method='ffill', axis=1)
    most_births = df['Birth Year'].mode()[0]
    print('The birth year with the most riders was:' + ' ' + str(most_births))
    
    

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
        
        rand_five = df[['Start Time', 'End Time', 'Start Station', 'End Station', 'User Type', 'Gender', 'Birth Year']]
        print(rand_five.sample(n=5))
        more_results = input('Would you like to see more results?: yes or no ')
        while more_results.lower() == 'yes':
            print(rand_five.sample(n=5))
            more_results = input('Would you like to see more results?: yes or no ')
            
        
               
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
