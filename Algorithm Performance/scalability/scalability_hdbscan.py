import numpy as np
import pandas as pd
import os
import multiprocessing
import sample_counters

def HDB_ProcessingTime():
    # Load data and set up as numpy array
    project = os.path.realpath('./..')
    datadir = os.path.join(project, 'data')

    store = pd.HDFStore(os.path.join(datadir, 'tweets_1M.h5'))
    subset = store.tweets_subset

    data = subset.as_matrix(columns=['lat', 'lng'])

    # HDBSCAN testing:
    eps = 0.00965606698736
    step = 500
    timeout = 60

    for n in range(100, 100000, step):

        filename = 'hdbscan_scale_by{}.csv'.format(step)

        p = multiprocessing.Process(target=sample_counters.hdbscan_samples, args=(data, 100, n, filename))
        p.start()
        p.join(timeout)
        if p.is_alive():
            print("Ending process at {} seconds".format(timeout))
            p.terminate()
            p.join()
            break

    store.close()


if __name__ == '__main__':
    HDB_ProcessingTime()

