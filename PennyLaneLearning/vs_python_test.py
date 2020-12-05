import qiskit
from qiskit import QuantumCircuit
from qiskit.visualization import plot_histogram, plot_bloch_vector

mycircuit = QuantumCircuit(2, 2)
mycircuit.h(0)
mycircuit.cx(0,1)
mycircuit.measure([0,1], [0,1])
mycircuit.draw('mpl')

from qiskit import Aer, execute

simulator = Aer.get_backend('qasm_simulator')
result = execute(mycircuit, simulator, shots=10000).result()
counts = result.get_counts(mycircuit)
print(counts)