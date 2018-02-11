import re

def process_date(date):

    # make sure that vdate is YYYY-MM-DD

    if not re.search(r'^\d\d\d\d-\d\d-\d\d$', date):
        raise ValueError('Please submit date in YYYY-MM-DD format')

    print('The submitted date is {0}'.format(date))

process_date('1980-01-03')
process_date('1/3/1980')