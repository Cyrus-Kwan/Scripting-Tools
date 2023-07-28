import pandas as pd
import re
import os

# In this current iteration, the read_as_string function is unable to read filepaths that use backslash \. 
# When specifying a file to read, please replace all instances of backslash \ with a forwardslash /.
def read_as_string(file_path):
    raw_path = repr(file_path)
    directory = open(file_path, 'r')
    return directory.read()

def words_to_df(list_of_words):
    unique_words = []
    word_count = []
    for word in list_of_words:
        if (word not in unique_words) and (word != ''):
            unique_words.append(word)
    for word in unique_words:
        word_count.append(list_of_words.count(word))
        
    df = pd.DataFrame({"words" : unique_words, "count" : word_count})
    df = df.sort_values(by="count")
    return df

def create_bow_file(file_path):
    file_name_re = r"(?!.+[\\/]|[\\/]).+(?=\.)"             # This regular expression is used to store the name of the given document without the file extension.
    file_name = re.findall(file_name_re, file_path)[0]      # Example: "C:/Documents/test_data/this.is.a.test.file.txt" will be stored as "this.is.a.test.file"
    word_list = [word.lower() for word in re.split(r"[^a-zA-Z]+", read_as_string(f"{file_path}"))]
    df = words_to_df(word_list)

    try:
        df.to_csv(f"./output_csv/{file_name}.csv", index=False)
    except OSError:
        os.mkdir("./output_csv")
        df.to_csv(f"./output_csv/{file_name}.csv", index=False)
