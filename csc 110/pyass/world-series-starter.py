'''SETUP: The WorldSeriesWinners.csv file contains a chronological
list of the World Series' winning teams from 1903 through 2009.
The first line in the file is the name of the team that won in 2018,
and the last line is the name of the team that won in 1903.
(Note the World Series was not played in 1904 or 1994 and so they
have no entry.)'''


import Teams as t
def main():
	#dict_of_seires()
	#dict_of_winners()
	#year_prompt()
	#most_winning_teams()

	objects()


'''Q1: Write a program that reads this file and creates a dictionary
in which the keys are the names of the teams, and each key’s
associated value is the number of times the team has won the World
Series. The program should also create a dictionary in which the
keys are the years, and each key's associated value is the name of
the team that won that year.'''



def dict_of_seires():
	new_dict = {}
	count = 0
	file_handle = open('WorldSeriesWinners.csv', 'r')
	for line in file_handle:
		line = line.rstrip('\n')
		data_list = line.split(',')
		team = data_list[1]
		year = int(data_list[0])
		if team not in new_dict:
			new_dict[year] = team
	file_handle.close()
	#print(new_dict)
	return new_dict


print("")


def dict_of_winners():
	new_dict = {}
	file_handle = open('WorldSeriesWinners.csv','r')
	for line in file_handle:
		line = line.rstrip('\n')
		data_list = line.split(',')
		team_names = data_list[1]
		if team_names in new_dict:
			new_dict[team_names] += 1
		else:
			new_dict[team_names] = 1
	print(new_dict)
	return new_dict
	#file_handle.close()
			#print(count)
			#print(team_names)


	print("")


		#print(key)

'''Q2: The program should prompt the user for a year in the range
of 1903 through 2018. It should then display the name of the team
that won the World Series that year, and the number of times that
team has won the World Series.'''

def year_prompt():
	new_dict = dict_of_seires()
	new_dict2 = dict_of_winners()
	year = int(input("what year do you want to know about? "))
	if year in new_dict:
		team = new_dict[year]
	if team in new_dict2:
		count = new_dict2[team]
	
	print(team,count)



'''Q3: The program should then display the most winning teams and
the number of times they have won'''


def most_winning_teams():
	current_highest = 0
	pop_list= []
	new_dict = dict_of_winners()
	print(new_dict)
	print("")	
	for k,v in new_dict.items():
		new_dict[k] = v
		if v > current_highest:
			current_highest = v

	for k,v in new_dict.items():
		if current_highest == new_dict[k]:
			team_name = k
			print("the current highest team is:")
			print(current_highest,team_name)
			pop_list.append(team_name)
	print("")
	
	for x in pop_list:
		new_dict.pop(x)
	#print(new_dict)
	print("the least winning teams are:")	
	for k,v in new_dict.items():
		if v < 2:
			print(v,k)
	



'''Q4: The program should then display the least winning teams and
the number of times they have won'''







'''Q5: Redo Q1-Q5 so that instead of using a Dictionary, a list of
Objects is used instead. What attributes should each object have?
(the name of each team and list of years the team won might be good
attributes to start, but you might decide to use different/more attributes)'''

def objects():
	list = []
	file_handle = open("WorldSeriesWinners.csv","r")
	for line in file_handle:
		line = line.rstrip("\n")
		line = line.split(",")
		years = line[0]
		names = line[1]
		team_data = t.Teams(years,names)
		list.append(team_data)
	print()
	print(list[2])
	return list






'''Q6: Add a method to the class to determine if the given object
has won the World Series multiple years in a row.'''

'''Q7: Add a method to the class to determine how many different
decades the team has won a World Series in.'''

if __name__ == '__main__':
	main()