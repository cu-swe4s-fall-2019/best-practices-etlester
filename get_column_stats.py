import sys
import math
import argparse


def col_stats(data):
    """Compute the mean and standard deviation
    of a list of numbers

    Parameters
    ----------
    data : float
        list of data points to calculate mean and stdev
    Returns
    -------
    mean : float
        The mean of data
    stdev : float
        The standard deviation of data
    """
    mean = sum(data)/len(data)
    stdev = math.sqrt(sum([(mean-x)**2 for x in data]) / len(data))
    return mean, stdev


def main():
    """Compute the mean and stdev of a column in a matrix

    Parameters
    ----------
    file_name : array of int
                Non-empty array containing numbers. The mean and standard
                deviation will be calculated for indicated column
   col_num : int
            Integer indicating the column in file_name to
            calculate the mean and standard deviation
    Returns
    -------
    mean
        Mean of the values in the indicated column in file_name
    stdev
        Standard deviation of the values in the indicated column in
        file_name
    """
    parser = argparse.ArgumentParser(
                description='Pass parameters',
                prog='get_column_stats')

    parser.add_argument('--file_name',
                        type=str,
                        help='Name of the file',
                        required=True)

    parser.add_argument('--col_num',
                        type=int,
                        help='The column number',
                        required=True)

    args = parser.parse_args()
    # determine if the file is present and if the correct
    # permissions are present
    try:
        f = open(args.file_name, 'r')
    except FileNotFoundError:
        print >> sys.stderr, 'Could not find ' + args.file_name
        sys.exit(1)
    except PermissionError:
        print >> sys.stderr, 'Could not open ' + args.file_name
        sys.exit(1)

    V = []

    for l in f:
        A = [int(x) for x in l.split()]
        try:
            V.append(A[args.col_num])
        except IndexError:
            # print('The column number is not within the dataframe')
            print >> sys.stderr, 'column number not in dataframe'
            sys.exit(1)

    [mean, stdev] = col_stats(V)

    print('mean:', mean)
    print('stdev:', stdev)


if __name__ == '__main__':
    main()
