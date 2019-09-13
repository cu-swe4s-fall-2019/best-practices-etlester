test -e ssshtest || wget -q \
https://raw.githubusercontent.com/ryanlayer/ssshtest/master/ssshtest
. ssshtest

# test style.py conformity to PEP8
run style_test pycodestyle style.py
assert_no_stdout

# test get_colum_stats.py conformity to PEP8
run get_colum_style_test pycodestyle get_column_stats.py
assert_no_stdout

#This tests whether get_column_stats.py will run on random numbers
(for i in `seq 1 $RANDOM`; do 
    echo -e "$RANDOM\t$RANDOM\t$RANDOM\t$RANDOM\t$RANDOM";
done )> data.txt

run rand_num python get_column_stats.py --file_name data.txt --col_num 2
assert_exit_code 0
assert_no_stderr
assert_stdout
assert_in_stdout "mean:"
assert_in_stdout "stdev:"

#This tests whether get_column_stats.py will run on a specific table 
#and will return an expected value

for a in `seq 1 10`;
do
    V=$a
    (for i in `seq 1 $RANDOM`; do 
        echo -e "$V\t$V\t$V\t$V\t$V";
    done )> data.txt

    run known_input python get_column_stats.py --file_name data.txt --col_num 2
    assert_exit_code 0
    assert_no_stderr
    assert_stdout
    assert_in_stdout mean: $V
    assert_in_stdout stdev: 0.0
done

#test whether non existant input file error handling is correct
run no_input python get_column_stats.py --file_name asdjfk.txt --col_num 1
assert_exit_code 1
assert_in_stderr 'Could not find'
assert_no_stdout

#test whether incorrect permission error handling is correct
(for i in `seq 1 $RANDOM`; do
    echo -e "$RANDOM\t$RANDOM\t$RANDOM\t$RANDOM\t$RANDOM";
done )> data1.txt

chmod 000 data1.txt
run bad_perm python get_column_stats.py --file_name data1.txt --col_num 1
assert_exit_code 1
assert_in_stderr 'Could not open'
assert_no_stdout

#This tests whether get_column_stats.py will throw an error when given a
#letter for column rather than an integer
run letter_input python get_column_stats.py --file_name data.txt --col_num a
assert_exit_code 2
assert_in_stderr "invalid int value:"
assert_no_stdout

#This tests whether get_column_stats.py will throw an error when given a
#column that is out of bounds

(for i in `seq 1 $RANDOM`; do
    echo -e "$RANDOM\t$RANDOM\t$RANDOM\t$RANDOM\t$RANDOM";
done )> data.txt

run out_of_bounds python get_column_stats.py --file_name data.txt --col_num 7
assert_exit_code 1
assert_in_stderr 'column number not in dataframe'
assert_no_stdout
