import matplotlib.pyplot as plt


dataset = 'C3'

total_A3 = 1709185
total_B3 = 2540597
total_C3 = 2577857

#input_filename = f'{dataset}/{dataset}_results_seq_cnt.txt'
input_filename = f'{dataset}/{dataset}_results_seq90_cnt.txt'

results_file = open(input_filename, 'r')
results = results_file.readlines()

x_axis = []
y_axis = []

for i in range(1, 693):
    x_axis.append(i)
    y_axis.append(0)

# Normalized frequency results using total number of query sequences
for line in results:
    y, x = line.split()
    x = int(x)
    y = float(y)
    y_axis[x - 1] = (y * 1.0 / total_C3) * 100
    y_axis[x - 1] = round(y_axis[x - 1], 2)


f = plt.figure(1)
plt.bar(x_axis, y_axis)
plt.title(f'{dataset} Results')
plt.xlabel('Sequences')
plt.ylabel('Frequency (%)')
# ylim for plot
#plt.ylim([0, 5])
# ylim for 90plot
plt.ylim([0, 1])
#plt.savefig(f'{dataset}/{dataset}_plot.png')
plt.savefig(f'{dataset}/{dataset}_90plot.png')

g = plt.figure(2)
plt.bar(x_axis[400:], y_axis[400:])
plt.title(f'{dataset} Results (Sequence 400 ~ 692)')
plt.xlabel('Sequences')
plt.ylabel('Frequency (%)')
# ylim for plot
#plt.ylim([0, 5])
# ylim for 90plot
plt.ylim([0, 1])
#plt.savefig(f'{dataset}/{dataset}_plot_2.png')
plt.savefig(f'{dataset}/{dataset}_90plot_2.png')



# x_axis: sequences, each number is a sequence ID
# y_axis: number of hits for each sequence (in percentage)
# plot.png: all sequences
# plot_2.png: only for sequences 400~692
# 90plot.png: plot for sequences that have hit results > 90%