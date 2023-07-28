# Bag of words tool

This program can be used to do a basic extraction of alphanumeric words from a given .txt file.

**Required imports**
> ``` python
> import pandas as pd
> import re
> import os
> ```

### Known Issues:
- read_as_string function is unable to read file paths containing backslashes. To remedy this, please replace all instances of backslash `\` with forwardslash `/`.