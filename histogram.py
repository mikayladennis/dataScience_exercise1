from random import randint

def compute_histogram_bins(data=[], bins=[]):
    """
        Question 1:
        Given:
            - data, a list of numbers you want to plot a histogram from,
            - bins, a list of sorted numbers that represents your histogram
              bin thresdholds,
        return a data structure that can be used as input for plot_histogram
        to plot a histogram of data with buckets bins.
        You are not allowed to use external libraries other than those already
        imported.
    """
    #Dictionary created to store bin labels and corresponding counts
    bin_dict = {}
    
    #loop through the data and count the occurences for each bin
    i = 0
    while i < len(bins):
        count = 0
        for j in range(0,len(data)):
            if i == len(bins)-1:
                if data[j] >= bins[i]:
                    count = count + 1
            else:
                if data[j] >= bins[i] and data[j] < bins[i+1]:
                    count = count + 1
            
        if i == len(bins)-1:
            bin_vals = (bins[i])
            bin_vals = str(bin_vals) + '+'
        else:
            bin_vals = (bins[i], bins[i+1])
            bin_vals = str(bin_vals)
        
        #Store the count for the bin value in the dictionary
        bin_dict[bin_vals] = count
        i = i + 1
        
    return bin_dict


def plot_histogram(bins_count):
    """
        Question 1:
        Implement this function that plots a histogram from the data
        structure you returned from compute_histogram_bins. We recommend using
        matplotlib.pyplot but you are free to use whatever package you prefer.
        You are also free to provide any graphical representation enhancements
        to your output.
    """
    import matplotlib.pyplot as plt
    
    #Plotting bars using the keys and values of the dictionary input
    plt.figure(figsize=(10,6))
    plt.bar(list(bins_count.keys()), bins_count.values())
    plt.xlabel('Connection Duration (s)', fontsize = 15)
    plt.ylabel('Connection Count', fontsize = 15)
    plt.title('Distribution of Connection Durations', fontsize = 18)
    

if __name__ == "__main__":

    # EXAMPLE:

    # inputs
    data = [randint(0, 100) for x in range(200)]
    bins = [0, 10, 20, 30, 40, 70, 100]

    # compute the bins count
    histogram_bins = compute_histogram_bins(data=data, bins=bins)
    

    # plot the histogram given the bins count above
    plot_histogram(histogram_bins)
