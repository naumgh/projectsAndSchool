
def write_to_file():
	text = "This is my story..."
	# Write "This is my story..." to a file
	# called my_story.txt
	file_handle = open('myStory.txt', "w")
	file_handle.write(text)
	file_handle.close()


def append_to_file():
	author_note = "Written by ..."
	file_handle = open('myStory.txt', "a")
	file_handle.write(author_note)
	file_handle.close()

	# Append "Written by <your name>" onto
	# the back of my_story.txt

def main():
	write_to_file()
	append_to_file()

main()
