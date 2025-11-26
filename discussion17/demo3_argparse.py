import argparse
import numpy as np
import matplotlib.pyplot as plt

# ---- Argument Parser Setup ----
parser = argparse.ArgumentParser(description="Plot Blackbody Spectrum from Temperature")
parser.add_argument("temperature", type=float, help="Temperature in Kelvin")
parser.add_argument("-save", type=bool, help="Save the plot")
parser.add_argument("-outfile", type=str, default="blackbody.png", help="Output filename for the plot")


# ---- Parse Arguments ----
args = parser.parse_args()
print(f"Temperature: {args.temperature} K")

# ---- Define Plotting Function ----
def plot_blackbody_spectrum(temperature, save=False, outfile=args.outfile):
    
    # Define Constants
    h = 6.626e-34  # Planck's constant (J*s)
    c = 3.0e8      # Speed of light (m/s)
    k = 1.381e-23  # Boltzmann's constant (J/K)

    # Define wavelength range 
    wavelength = np.linspace(1e-9, 3e-6, 1000)  # 1 nm to 3000 nm

    # Planck's Law
    intensity = (2.0*h*c**2) / (wavelength**5) / (np.exp((h*c) / (wavelength*k*temperature)) - 1.0)

    # Plotting
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(wavelength * 1e9, intensity, label=f'T = {temperature} K')  # Convert to nm for x-axis
    ax.set_title('Blackbody Spectrum at {} K'.format(temperature))
    ax.set_xlabel('Wavelength [nm]')
    ax.set_ylabel('Intensity [W/m²/nm]')
    plt.legend()
    plt.grid()

    if save:
        plt.savefig(outfile)
        print(f"Plot saved as {outfile}")

    plt.show()

# ---- Generate Plot ----
plot_blackbody_spectrum(args.temperature, 
                        save=args.save,
                        outfile=args.outfile)

    
