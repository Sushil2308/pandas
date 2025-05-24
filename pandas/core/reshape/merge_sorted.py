import heapq
import pandas as pd

def merge_sorted(dfs, sort_column):
    """
    Efficiently merge sorted DataFrames by a common sort_column.
    """
    if not dfs:
        return pd.DataFrame()
    
    iterators = [df.itertuples(index=False, name=None) for df in dfs]
    heap = []

    for i, it in enumerate(iterators):
        try:
            row = next(it)
            key = row[dfs[i].columns.get_loc(sort_column)]
            heapq.heappush(heap, (key, i, row))
        except StopIteration:
            continue

    result = []
    while heap:
        _, i, row = heapq.heappop(heap)
        result.append(row)
        try:
            next_row = next(iterators[i])
            key = next_row[dfs[i].columns.get_loc(sort_column)]
            heapq.heappush(heap, (key, i, next_row))
        except StopIteration:
            continue

    return pd.DataFrame(result, columns=dfs[0].columns)
