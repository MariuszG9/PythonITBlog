import pandas as pd
from collections import defaultdict

df = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [4, 5, 6],
    'C': [7, 8, 9]})

# utworzenie pustego defaultdict z domyślną wartością None
d = defaultdict(None)
d = df.to_dict(into=d)

print(df)
print(d)
