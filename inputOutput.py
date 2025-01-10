#INPUT & OUTPUT
infile = open('values.txt', 'rt') #Python Method: 'open' 
    #values.txt - list of numbers

outfile = open('values-totaled.txt', 'wt') #file to store the output

print('Processing input')
sum = 0

for line in infile: #taking one number, converting the str to int, adding it to sum 
    sum += int(line)
    print(line.rstrip(), file=outfile)

print('\nTotal: ' + str(sum), file=outfile)
outfile.close()
print('Output complete')
