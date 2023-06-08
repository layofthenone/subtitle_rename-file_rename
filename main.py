import os


"""
def movie_name_extension():
    dot_index = movie_files.__getitem__(1).index(".")
    movie_file_extension = (movie_files[1])[dot_index:]

    movie_file_name_before_extension = (movie_files[1])[:dot_index]
    return movie_file_extension, movie_file_name_before_extension


def sub_name_extension():
    dot_index = subtitle_files.__getitem__(1).index(".")
    subtitle_file_extension = (subtitle_files[1])[dot_index:]

    movie_file_name_before_extension = (movie_files[1])[:dot_index]
    return subtitle_file_extension, movie_file_name_before_extension
"""


def subtitle_file_rename(MOVIES_DIRECTORY = 'D:\TORRENT\Monster [Ultimate Collection] By Kira [SEV]\movie' + "\\",
                     SUBTITLE_DIRECTORY = 'D:/TORRENT/Monster [Ultimate Collection] By Kira [SEV]/sub/' + "\\"):

    movie_files = os.listdir(MOVIES_DIRECTORY)
    subtitle_files = os.listdir(SUBTITLE_DIRECTORY)

    for file_index, file_name in enumerate(subtitle_files):
        os.rename(SUBTITLE_DIRECTORY + file_name,
                  SUBTITLE_DIRECTORY + ((movie_files[file_index])[:movie_files.__getitem__(file_index).index(".")]) +
                  (subtitle_files[file_index])[subtitle_files.__getitem__(file_index).index("."):])


def remove_word_in_file_name(FILE_DIRECTORY = "D:\TORRENT\Monster [Ultimate Collection] By Kira [SEV]\Yeni klasör" + "\\",
                             DELETING_WORD = "dam"):
    files = os.listdir(FILE_DIRECTORY)
    for file in files:
        if DELETING_WORD in file:
            file.find(DELETING_WORD)  # word's starting index
            len(DELETING_WORD)  # word's total char
           # print(file[(file.find(DELETING_WORD)):(file.find(DELETING_WORD))+len(DELETING_WORD)])
           # print(file[(file.find(DELETING_WORD))+len(DELETING_WORD):])  # after the word
           # print(file[:(file.find(DELETING_WORD))])  # before the word
            new_file_name = file[:(file.find(DELETING_WORD))] + file[(file.find(DELETING_WORD))+len(DELETING_WORD):]

            os.rename(FILE_DIRECTORY + file, FILE_DIRECTORY + new_file_name)

if __name__ == "__main__":
    # subtitle_file_rename()
    remove_word_in_file_name()
