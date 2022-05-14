

import pandas as pd
import numpy as np
import altair as alt

df = pd.DataFrame(
     np.random.randn(200, 3),
     columns=['a', 'b', 'c'])


alt.Chart(df).mark_circle().encode(x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])
