import pandas as pd
from pandas.core.reshape.merge_sorted import merge_sorted

def test_merge_sorted_basic():
    df1 = pd.DataFrame({"x": [1, 3, 5]})
    df2 = pd.DataFrame({"x": [2, 4, 6]})
    result = merge_sorted([df1, df2], sort_column="x")
    expected = pd.DataFrame({"x": [1, 2, 3, 4, 5, 6]})
    pd.testing.assert_frame_equal(result, expected)
