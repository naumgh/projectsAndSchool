''' For the following problems you will use files with course prerequisite data.
    The sample files are formated as rows of comma separated data,
    where each row represents information for a single course.
    The first value in a row is the course and the remaining values
    are 0 or more prerequisites for that course.
    The sample files are: cscprereqs_1.csv and cscprereqs.csv
    You can open these files using Excel (commas will not show) to inspect the data.
    The files you want to use MUST be in the same directory as this file.
    '''
def main():
    print('call your test functions from here')
    prereq_data('cscprereqs_1.csv')
   #prereq_data('cscprereqs_1.csv')

''' Q1. Design a function that takes a filename of course prerequisite data
    and creates a dictionary entry for each row in the file where,
    the course is the key and the prerequisite courses in sorted order is the value.
    The function should return None if there is an error opening/reading the file.
    Examples.
        the dictionary entry for row 1 of cscprereqs_1.csv would be:list to 
            CSC 110': ['MATH 12']
        the returned dictionary for cscprereqs_1.csv would be:
            {'CSC 110': ['MATH 12'],
             'CSC 111': ['MATH 12'],
             'CSC 115': ['CSC 110', 'CSC 111'],
             'CSC 116': ['CSC 110', 'CSC 111']}
    

    '''
def prereq_data(testfile):
    test_list = []
    new_dict = {}
    file_handle = open(testfile, 'r')
    for x in file_handle:
        x = x.strip('\n')
        test_list = x.split(',') 
        #print(test_list[0])
        try:
            new_dict = {test_list[0] : test_list[1]}
            new_nigga = {test_list[0] : test_list[2]}
            newestnigga =[new_dict, new_nigga]
            print(newestnigga)
        except IndexError:
            print("nigga")
    '''
        try:
            for i in range(0, len(test_list)):
                new_dict[test_list[i]] = test_list[i+1]
        except IndexError:
            print(new_dict)

    '''   
    

    #print(a)
    '''
    for x in file_handle:
        x = x.strip('\n')
        test_list.append(x)
    new_dict = {test_list[i]: test_list[i+1] for i in range(0, len(test_list), 2)}
    print(test_list)
    print(new_dict)

    '''
''' Q2. Design a function that takes a dictionary where for each entry,
    the key is a course as a string and the value is a list of prerequisite courses
    as a list of strings.  The function should create and return an alphabetically sorted list of
    the names of the courses for which the course requires one or less prerequisites.
    '''

''' Q3. Design a function that takes a dictionary where for each entry,
    the key is a course as a string and the value is a list of related courses
    as a list of strings. The function should return the maximum length of
    values across all entries - that is, the length of the longest list of courses.
    The function should return 0 if the dictionary is empty.
    Example.
        if data is {'CSC 111': ['MATH 12'],'CSC 115': ['CSC 110', 'CSC 111'], 'CSC 106': [], 'CSC 116': ['CSC 110', 'CSC 111']}
        the function should return 2 as CSC 115 and CSC 116 have values with the longest list of courses
    '''


''' Q4. Design a function that takes a dictionary where for each entry,
    the key is a course as a string and the value is a list of related courses
    as a list of strings.  The function should create and return an alphabetically sorted list of
    the names of the courses that have the most related courses.
    HINT: you will need to find out the maximum length of the values in the dictionary
        before going through the dictionary to select course names.
    '''


''' Q5. Design a function that takes a dictionary where for each entry,
    the key is a course as a string and the value is a list of related courses
    as a list of strings.  The function should create and return a new dictionary from
    the given dictionary where, each of the course names in the lists of values
    is a key in the new dictionary and the value for each key in the new dictionary is
    a list of the courses that are related to that key in sorted order.
    
    Example.
        if data is {'CSC 111': ['MATH 12'], 'CSC 116': ['CSC 110', 'CSC 111'],'CSC 115': ['CSC 110', 'CSC 111'], 'CSC 106': []}
        then the function should return {'MATH 12': [ 'CSC 111'], 'CSC 110': [ 'CSC 115', 'CSC 116'],
        'CSC 111': [ 'CSC 115', 'CSC 116']}
    '''


''' Q6. Design a function that takes a dictionary where for each entry,
    the key is a course as a string and the value is a list of prerequisite courses
    as a list of strings.  The function should create and return a list of
    the course names in data that are the most used prequisites.
    Example.
        if data is {'CSC 111': ['MATH 12'],'CSC 115': ['CSC 110', 'CSC 111'],'CSC 106': [],
                    'CSC 116': ['CSC 110', 'CSC 111'], 'CSC 110': ['MATH 12']}
        then the function should return ['CSC 110', 'CSC 111', 'MATH 12']
            since these courses are most frequently used as prerequisites.
    HINT: Think about how to use the functions you previously defined as helper functions.
          The instructor's solution is only a few lines of code.
    '''







# str, bool -> None
# prints test_name followed by 'passed' if expression evaluates to True,
# prints test_name followed by 'failed' if expression evaluates to False
def print_test(test_name, expression):
    if(expression):
        print(test_name + ': passed')
    else:
        print(test_name + ': failed')


# The following code will call your main function
if __name__ == '__main__':
    main()
