import pandas as pd
import numpy as np
import time

CITY_DATA = {"New York City":"new_york_city.csv","Chicago":"chicago.csv","Washington":"washington.csv"}
MONTHS = ['january', 'february', 'march', 'april', 'may', 'june','all']
WEEKDAYS = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday','all']

def filter():
    print('Hello let\'s explore some US bikeshae data! ')
    while True:
        city  = input('Entrer the city you want to investigate (Chicago/New York City/Washington):')
        if city not in ('New York City', 'Chicago', 'Washington'):
            print('Sorry i didn\'t catch that, try again')
            continue
        else:
            break
    while True:
        month = input('Entrer the mounth to study(junary - june) (OR) (Enter all no month filter):')
        if month not in MONTHS:
            print('Sorry i didn\'t catch that, try again  ')
            continue
        else:
            break
    while True:
        day = input('Entrer the day to study(monday - sunday) (OR) (Enter all no month filter):')
        if day not in WEEKDAYS:
            print('Sorry i didn\'t catch that, try again  ')
            continue
        else:
            break
    print('-'*40)
    return city,month,day

def load_data(city,month,day):
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'],errors='coerce')
    df['month']  = df['Start Time'].dt.month
    df['day'] = df['Start Time'].dt.dayofweek
    df['hour'] = df['Start Time'].dt.hour
    if month != all:
        month = MONTHS.index(month)+1
        df = df[df['month']== month]
    if day != all:
        day  =WEEKDAYS.index(day)+1
        df  = df[df['day']== day ]
    return df

def time_stats(df):
    print('\nCalculating the most frequent times of travel ...')
    start_time = time.time()
    popular_month = df['month'].mode()[0]
    print('Most commun Month:',popular_month)
    popular_day = df['day'].mode()[0]
    print('Most commun Day:' , popular_day)
    popular_hour = df['hour'].mode()[0]
    print('Most commun Hour:',popular_hour)
    print("\nThis took %s seconds" % (time.time() - start_time))
    print('-'*40)
def station_stats(df):
    print('\n Calculating the most popular station and Trip... ')
    start_time  = time.time()
    start_station = df['Start Station'].value_counts().idxmax()
    print('Most Commonly used start station:', start_station)
    end_station = df['End Station'].value_counts().idxmax()
    print('Most Commonly used start station:', end_station)
    combination_station = df.groupby(['Start Station','End Station']).count()
    print('\nMost Commonly used combination of start station and end station trip:', start_station, " & ", end_station)
    print('\nthis toke %s seconds' % (time.time() - start_time))
    print('-'*40)
def trip_duration_stats(df):
    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    total_travel_time = sum(df['Trip Duration'])
    print('total travel time:',total_travel_time)
    average_travel_time = df['Trip Duration'].mean()
    print('average travel time:',average_travel_time)
    print('\nThis took %s second' % (time.time() - start_time))
    print('-'*40)
def User_stats(df):
    print('\nCalculating User Stats...\n')
    start_time = time.time()
    user_type = df['User Type'].value_counts()
    print('User Types:\n', user_type)
    try:
        gender_types = df['Gender'].value_counts()
        print('\nGender Types:\n',gender_types)
    except KeyError:
        print('\n Gender Types:\nNo data available for this month.')
    try:
        Earlies_years = df['Birth Year'].min()
        print('\nEarliest Year:', Earlies_years)
    except KeyError:
        print("\nEarliest Year:\nNo data available for this month.")
    try:
        most_recent_years = df['Birth Years'].max()
        print('\nMost recent Year:', most_recent_years)
    except KeyError:
        print("\nMost  recent Year:\nNo data available for this month.")
    try:
        most_Common_Year = df['Birth Year'].value_counts().idxmax()
        print('\nMost Common Year:', most_Common_Year)
    except KeyError:
        print('\nMost Common Year:\nNo data available for this month.')
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
def main():
    while True:
        city,month,day = filter()
        df = load_data(city,month,day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        User_stats(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() !='yes':
            break

if __name__ == "__main__":
    main()