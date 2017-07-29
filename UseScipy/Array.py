import sys

def main():
    # the example to use numpy
    import numpy as np
    
    print('create an array filled with random values')
    e = np.random.random((2, 2))
    print(e)
    
    # the example to use scipy
    from scipy.fftpack import fft
    
    # Number of sample points
    N = 600
    
    # sample spacing
    T = 1.0 / 800.0
    x = np.linspace(0.0, N*T, N)
    y = np.sin(50.0 * 2.0*np.pi*x) + 0.5*np.sin(80.0 * 2.0*np.pi*x)
    yf = fft(y)
    xf = np.linspace(0.0, 1.0/(2.0*T), N//2)
    
    import matplotlib.pyplot as plt
    plt.plot(xf, 2.0/N * np.abs(yf[0:N//2]))
    plt.grid()
    plt.show()
    
if __name__ == "__main__": 
    main()
    
