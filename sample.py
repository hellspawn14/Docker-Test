from datetime import datetime
import os, shutil, logging, random, time, requests


def setup_logging(n_base_path, n_execution_dt):
    log_file, log_folder = n_base_path + '/debug.log', n_base_path + '/logs'
    if os.path.exists(log_file):
        os.remove(log_file)

    logging.basicConfig(
        format = '%(asctime)s.%(msecs)03d (%(levelname)s): %(message)s', 
        level = logging.DEBUG, 
        datefmt = '%Y-%m-%d %H:%M:%S', 
        handlers = [
            logging.FileHandler(log_file), 
            logging.StreamHandler()
        ]
    )
    
    logging.info('Starting')
    if not os.path.exists(log_folder):
        logging.info('Logs directory does not exists')
        logging.info('Creating new logs directory')
        os.makedirs(log_folder)

    logging.info('Logs will be stored in ' + log_folder)
    log_file_end = log_folder + '/' + n_execution_dt + '.log'
    return log_file, log_file_end

def get_wait_random_time():
    return random.uniform(0.1, 3)

def get_random_int(n_len):
    return random.randint(0, n_len - 1)

def main(n_base_path, n_execution_dt, n_max_items):
    log_file, log_file_end = setup_logging(n_base_path, n_execution_dt)
    logging.info('Hello world')
    '''
    lottery, winners = list(range(0, n_max_items)), []
    logging.info('Begining lottery!')
    while len(lottery) > 0:
        logging.info('-----------')
        logging.info('# Possible winners: ' + str(len(lottery)))
        logging.info('# Winners: ' + str(len(winners)))
        winner_pos, wait_time = get_random_int(len(lottery)), get_wait_random_time()
        winner_item = lottery.pop(winner_pos)
        winners.append(winner_item)
        logging.info('Winner: ' + str(winner_item))
        logging.info('Sleeping for: ' + str(wait_time))
        time.sleep(wait_time)

        if len(lottery) == 0:
            logging.info('Ending lottery')
            logging.info('-----------')
        else: 
            logging.info('Next Round')
    '''

    logging.info('End of script') # End sample script 
    shutil.copy(log_file, log_file_end) # Save log for current execution
    logging.info('Log file for this execution will be located at ' + log_file_end)



if __name__ == '__main__': 
    base_path, execution_dt = os.path.realpath(__file__).replace('/sample.py', ''), datetime.now().strftime('%Y-%m-%d %H.%M.%S.%f')
    max_items = 1
    main(base_path, execution_dt, max_items)