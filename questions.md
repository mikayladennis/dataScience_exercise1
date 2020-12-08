### Questions

#### Question 3

With peers sending such datastructure and our _backend_ server making such operations, we retrieve exactly **all** the connection durations on the network at the moment of the snapshot and we are able to plot the _exact distribution_ of the connection durations.
`question2.py` main has several simulations with increasing numbers of peers and peer pool size. Run the simulations with your implementation. What do you see? Can you explain the limitations of the implementations of question 2 taking into account that a _real_ peer network can have _millions_ of peers? (answer below in this file)

>> Increasing the numbers of peers and peer pool sizes increases the time taken for backend processing. Considering a _real_ peer network can have _millions_ of peers, this implementation is limited by the time to process. Although in the simulation the backend processing was fairly quick, we only used at most 10,000 number of peers or 1,000 as the max peer pool size. It would not be very practical to implement this method in a real situation because it would take too long.

#### Question 4

Go to the file `question4.py`:
Propose new implementations of `send_data_to_backend` and `process_backend_data` that can deal with millions of peers _and_ still provide a good representation of the _distribution_ of the connection duration. You are free to add any written comments, add pictures etc. to enhance your answer.

>> My proposal is to take a random sample of the data to use for constructing the histogram. So long as the sample is sufficient, the distribution should still be representative of the data while significantly reducing the processing time. In this exercise, I used a random sample of 10% of the total connection durations; however, if the processing time on a real dataset was too long, the random sample could be created using a fixed number of samples that would ensure adequate processing time. For the purposes of this exercise, I believe using 10% of the data for a random sample is sufficient in showing the improvements. For example, the simulation using 10,000 number of peers and a max peer pool size of 100 showed the backend processing time decreased from about 3.87 seconds to 0.76 seconds while the histograms still displayed about the same distribution. This distribution comparison can be viewed in the files `all_data_histogram.png` (the histogram generated using functions in question 2) and `sampled_histogram.png` (the histogram generated using functions in question 4).
