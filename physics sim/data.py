import matplotlib.pyplot as plt
def transform_to_file(data):
        
        # Plot the data
        plt.figure(figsize=(10, 5))
        plt.plot(data, marker='o', linestyle='-', color='blue', label='Delta Values')
        plt.title("Delta Values Over Time")
        plt.xlabel("Frame Index")
        plt.ylabel("Delta (Seconds)")
        plt.grid(True)
        plt.legend()
        plt.show()