from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit
from numpy import pi

def level3_1():
    
    qreg_q = QuantumRegister(5, 'q')
    creg_c = ClassicalRegister(5, 'c')
    circuit = QuantumCircuit(qreg_q, creg_c)

    circuit.barrier(qreg_q[0])
    circuit.barrier(qreg_q[1])
    circuit.barrier(qreg_q[2])
    circuit.barrier(qreg_q[3])
    circuit.barrier(qreg_q[4])
    circuit.z(qreg_q[1])
    circuit.x(qreg_q[3])
    circuit.h(qreg_q[1])
    circuit.cx(qreg_q[3], qreg_q[4])
    circuit.z(qreg_q[1])
    circuit.swap(qreg_q[3], qreg_q[4])
    circuit.ccx(qreg_q[2], qreg_q[4], qreg_q[3])
    circuit.swap(qreg_q[1], qreg_q[2])
    circuit.x(qreg_q[2])
    circuit.ccx(qreg_q[3], qreg_q[2], qreg_q[1])
    circuit.cx(qreg_q[2], qreg_q[0])
    circuit.h(qreg_q[3])
    circuit.cx(qreg_q[0], qreg_q[3])
    circuit.measure(qreg_q[1], creg_c[1])
    circuit.measure(qreg_q[3], creg_c[3])

    return circuit

def level3_2():

    qreg_q = QuantumRegister(5, 'q')
    creg_c = ClassicalRegister(5, 'c')
    circuit = QuantumCircuit(qreg_q, creg_c)

    circuit.barrier(qreg_q[0])
    circuit.barrier(qreg_q[1])
    circuit.barrier(qreg_q[2])
    circuit.barrier(qreg_q[3])
    circuit.barrier(qreg_q[4])
    circuit.ccx(qreg_q[0], qreg_q[1], qreg_q[2])
    circuit.swap(qreg_q[3], qreg_q[4])
    circuit.ccx(qreg_q[1], qreg_q[2], qreg_q[3])
    circuit.swap(qreg_q[0], qreg_q[1])
    circuit.ccx(qreg_q[2], qreg_q[3], qreg_q[4])
    circuit.ccx(qreg_q[3], qreg_q[4], qreg_q[0])
    circuit.ccx(qreg_q[4], qreg_q[0], qreg_q[1])
    circuit.measure(qreg_q[1], creg_c[1])
    
    return circuit

def level3_3():

    qreg_q = QuantumRegister(6, 'q')
    creg_c = ClassicalRegister(6, 'c')
    circuit = QuantumCircuit(qreg_q, creg_c)

    circuit.barrier(qreg_q[0])
    circuit.barrier(qreg_q[2])
    circuit.barrier(qreg_q[3])
    circuit.barrier(qreg_q[4])
    circuit.barrier(qreg_q[5])
    circuit.y(qreg_q[0])
    circuit.barrier(qreg_q[1])
    circuit.y(qreg_q[4])
    circuit.z(qreg_q[5])
    circuit.h(qreg_q[1])
    circuit.ccx(qreg_q[3], qreg_q[5], qreg_q[4])
    circuit.ccx(qreg_q[0], qreg_q[2], qreg_q[1])
    circuit.swap(qreg_q[1], qreg_q[4])
    circuit.swap(qreg_q[0], qreg_q[1])
    circuit.reset(qreg_q[2])
    circuit.reset(qreg_q[3])
    circuit.swap(qreg_q[4], qreg_q[5])
    circuit.cx(qreg_q[1], qreg_q[2])
    circuit.h(qreg_q[4])
    circuit.h(qreg_q[5])
    circuit.cx(qreg_q[4], qreg_q[3])
    circuit.measure(qreg_q[2], creg_c[2])
    
    return circuit


def level3(i):
    
    if i==1:
        level3_1()
        
    elif i==2:
        level3_2()
        
    elif i==3:
        level3_3()
        
    return circuit