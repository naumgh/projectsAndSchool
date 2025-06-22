import pandas as pd

def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv')
    print(df.head())


    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df['race'].value_counts()

    # What is the average age of men?
    average_age_sex = df.groupby('sex')['age'].mean()
    #print(average_age_sex)
    average_age_men = round(average_age_sex['Male'],1)
    

    # What is the percentage of people who have a Bachelor's degree?
    edu_count = df['education'].value_counts()
    print(edu_count)
    total_respondants = edu_count.sum()
    total_bachelors = edu_count['Bachelors']
    print(total_respondants, total_bachelors)

    percentage_bachelors = round(total_bachelors/total_respondants * 100,1)
    print(percentage_bachelors)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?
    advanced_degree = ['Bachelors','Masters','Doctorate']
    adv_rich = df[(df['education'].isin(advanced_degree))&(df['salary']=='>50K')]
    print(adv_rich)
    total_advanced = df[df['education'].isin(advanced_degree)]

    nodeg_rich = df[(~df['education'].isin(advanced_degree))&(df['salary']=='>50K')]
    print(len(nodeg_rich))
    total_nodeg = df[~df['education'].isin(advanced_degree)]
    print(len(total_nodeg))
    

    #print(round(len(adv_rich) / len(total_advanced) * 100, 1))
    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education = len(total_advanced)
    lower_education = len(total_nodeg)

    # percentage with salary >50K
    higher_education_rich = round(len(adv_rich) / len(total_advanced) * 100, 1)
    lower_education_rich = round(len(nodeg_rich) / len(total_nodeg) * 100, 1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    print(df['hours-per-week'].min())
    min_work_hours = df['hours-per-week'].min()
    print(len(df[(df['hours-per-week']==min_work_hours)]))
    print(len(df[(df['hours-per-week']==min_work_hours)&(df['salary'] == '>50K')]))


    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = len(df[(df['hours-per-week']==min_work_hours)])

    rich_percentage = round(len(df[(df['hours-per-week']==min_work_hours)&(df['salary'] == '>50K')]) / len(df[(df['hours-per-week']==min_work_hours)]) * 100,1)

    # What country has the highest percentage of people that earn >50K?
    print(df[(df['salary'] == '>50K')])
    high_earners_everywhere = df[(df['salary'] == '>50K')]
    high_earner_by_country = high_earners_everywhere['native-country'].value_counts()
    everyone = df['native-country'].value_counts()
    print(high_earner_by_country)
    print(everyone)
    total_by_country = df['native-country'].value_counts()
    high_earner_percentage_by_country = round((high_earner_by_country / total_by_country) * 100,1)
    #print(high_earner_percentage_by_country)
    #print(max(high_earner_percentage_by_country))
    country_with_highest_percentage = high_earner_percentage_by_country.idxmax()
    highest_percentage = high_earner_percentage_by_country.max()
    print(country_with_highest_percentage)



    highest_earning_country = high_earner_percentage_by_country.idxmax()
    highest_earning_country_percentage = high_earner_percentage_by_country.max()

    # Identify the most popular occupation for those who earn >50K in India.
    high_earners_indoa = df[(df['salary'] == '>50K')&(df['native-country'] == 'India')]
    print(high_earners_indoa)
    india_by_occupation= high_earners_indoa['occupation'].value_counts()
    print(india_by_occupation)
    top_IN_occupation = india_by_occupation.idxmax()

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
