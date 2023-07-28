# Bag of words tool

This program can be used to do a basic extraction of alphanumeric words from a given .txt file. The words are then counted and the result is stored according to the respective `word` row in a dataframe.

The resulting dataframe is finally output to a .csv file with the same file name as was given in the input path.

**Required imports**
> ``` python
> import pandas as pd
> import re
> import os
> ```

### Known Issues:
- read_as_string function is unable to read file paths containing backslashes. To remedy this, please replace all instances of backslash `\` with forwardslash `/`.