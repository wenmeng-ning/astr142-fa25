import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import median_abs_deviation
from multiprocessing import Pool
from datetime import datetime
import logging
import os
import subprocess
import sys

def process_order(ordernumber, basename='WASP33_nov21_rereduced_fluxes_coadded_order_',plot=False):
    data = np.load(basename+str(ordernumber)+'.npy')
    logging.info('Loaded file: ' + basename+str(ordernumber)+'.npy')
    if plot:
        plt.imshow(data,aspect=15,vmin=0,vmax=1e4)
        plt.show()
    ### Scale each exposure to a consistent median
    for i in range(data.shape[0]):
        data[i] = data[i]/np.nanmedian(data[i])
    ### Now we want to make the median over the time series (y-axis)
    medspec = np.nanmedian(data,axis=0)
    ### Now devide each spectrum in the time series by its median
    for i in range(data.shape[0]):
        data[i] = data[i]/medspec
    ### And let's mask outliers. Use a boolean index for speed
    threshold = 6*median_abs_deviation(data.flatten())
    data[np.abs(data-1)>threshold] = np.nan	

    if plot:
        plt.imshow(data,aspect=15,vmin=0.95,vmax=1.05)
        plt.show()
    logging.info('Done with ' + basename+str(ordernumber)+'.npy')
    return data

if __name__ == '__main__':
    logging.basicConfig(filename='logfile.log',level=logging.INFO)

    orders = [0,1,2,3,4,5,6,7,8]
    
    if len(sys.argv) == 1:
        
        proc_data = []
        t1 = datetime.now()
        logging.info('Starting for loop')
        for order in orders:
            proc_data.append(process_order(order))
        t2 = datetime.now()
        logging.info('For loop time: ' +str(t2-t1))

        ### Here's the pool version
        t3 = datetime.now()
        logging.info('Starting pool')
        pool = Pool(len(orders))
        processed_data = pool.map(process_order, orders)
        pool.close()
        pool.join()
        t4 = datetime.now()
        logging.info('Pool time: ' +str(t4-t3))

    ### Save the output
    # if not os.path.exists('output/'):
    #     os.mkdir('output/')
    # for i in orders:
    #     np.save('output/'+'WASP33_nov21_processed_order'+str(i)+'.npy',processed_data[i])
    #     logging.info('Saved '+'WASP33_nov21_processed_order'+str(i)+'.npy')

    ### Write a use GNU parallel for execution, taking the 
    ### order numbers as command line arguments. How does the runtime compare?
	
    if len(sys.argv) == 2:
        process_order(int(sys.argv[1]))

    cmd = f'parallel -j {len(orders)} python discussion17_activity1_template.py ::: {orders}'
    logging.info('Running GNU parallel command: ' + cmd)
    t5 = datetime.now()
    subprocess.run(cmd,shell=True)
    t6 = datetime.now()
    logging.info('GNU parallel time: ' +str(t6-t5))
    logging.info('Finished GNU parallel execution')
