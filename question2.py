from peer import Peer
from simulation import Simulation, BINS
from histogram import compute_histogram_bins, plot_histogram

class PeerQ2(Peer):

    def send_data_to_backend(self):
        """
            Question 2:
            This method should return an _array_ of the peer's
            connection durations.
        """
        #Storing each of the connection duration values into an array
        durations = []
        for p in self.peer_pool.values():
            durations.append(p)
            
        return durations
            

class SimulationQ2(Simulation):

    def generate_network(self):
        self.network =  [PeerQ2() for _ in range(self.number_of_peers)]

    def process_backend_data(self):
        """
            Question 2:
            This method should do all necessary processing to return
            the connection durations histogram bins counts.
            Don't call `plot_histogram` in this method, we just want
            to compute the histogram bins counts!
        """

        #Flatten "list of lists" so it works with the compute_histogram_bins function
        data = []
        for peer_list in self.backend_database:
            for i in peer_list:
                data.append(i)
        
        histogram_bins = compute_histogram_bins(data, BINS)
    
        return histogram_bins

if __name__ == "__main__":

    s = SimulationQ2(number_of_peers=10, max_peer_pool_size=2)
    s.run()
    s.report_result()

    s = SimulationQ2(number_of_peers=1000, max_peer_pool_size=10)
    s.run()
    s.report_result()

    s = SimulationQ2(number_of_peers=1000, max_peer_pool_size=100)
    s.run()
    s.report_result()

    s = SimulationQ2(number_of_peers=1000, max_peer_pool_size=1000)
    s.run()
    s.report_result()

    s = SimulationQ2(number_of_peers=10000, max_peer_pool_size=10)
    s.run()
    s.report_result()

    s = SimulationQ2(number_of_peers=10000, max_peer_pool_size=100)
    s.run()
    s.report_result()


