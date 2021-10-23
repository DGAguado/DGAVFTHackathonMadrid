from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit
from numpy import pi

def level1_1():

    qreg_q = QuantumRegister(2, 'q')
    creg_c = ClassicalRegister(2, 'c')
    circuit = QuantumCircuit(qreg_q, creg_c)

    circuit.barrier(qreg_q[0])
    circuit.barrier(qreg_q[1])
    circuit.x(qreg_q[0])
    circuit.measure(qreg_q[0], creg_c[0])
    circuit.measure(qreg_q[1], creg_c[1])
    
    return circuit

def level1_2():
    
    qreg_q = QuantumRegister(2, 'q')
    creg_c = ClassicalRegister(2, 'c')
    circuit = QuantumCircuit(qreg_q, creg_c)

    circuit.barrier(qreg_q[0])
    circuit.barrier(qreg_q[1])
    circuit.measure(qreg_q[0], creg_c[0])
    circuit.measure(qreg_q[1], creg_c[1])
    
    return circuit

def level1_3():

    qreg_q = QuantumRegister(2, 'q')
    creg_c = ClassicalRegister(2, 'c')
    circuit = QuantumCircuit(qreg_q, creg_c)

    circuit.barrier(qreg_q[0])
    circuit.barrier(qreg_q[1])
    circuit.x(qreg_q[1])
    circuit.measure(qreg_q[0], creg_c[0])
    circuit.z(qreg_q[1])
    circuit.measure(qreg_q[1], creg_c[1])
    
    return circuit

def level1_4():

    qreg_q = QuantumRegister(2, 'q')
    creg_c = ClassicalRegister(2, 'c')
    circuit = QuantumCircuit(qreg_q, creg_c)

    circuit.barrier(qreg_q[0])
    circuit.barrier(qreg_q[1])
    circuit.h(qreg_q[0])
    circuit.x(qreg_q[0])
    circuit.x(qreg_q[1])
    circuit.measure(qreg_q[0], creg_c[0])
    circuit.measure(qreg_q[1], creg_c[1])
    
    return circuit

def level1_5():

    qreg_q = QuantumRegister(2, 'q')
    creg_c = ClassicalRegister(2, 'c')
    circuit = QuantumCircuit(qreg_q, creg_c)

    circuit.barrier(qreg_q[1])
    circuit.barrier(qreg_q[0])
    circuit.cx(qreg_q[0], qreg_q[1])
    circuit.measure(qreg_q[1], creg_c[1])
    
    return circuit

def level1_6():

    qreg_q = QuantumRegister(2, 'q')
    creg_c = ClassicalRegister(2, 'c')
    circuit = QuantumCircuit(qreg_q, creg_c)

    circuit.barrier(qreg_q[1])
    circuit.barrier(qreg_q[0])
    circuit.swap(qreg_q[0], qreg_q[1])
    circuit.cx(qreg_q[0], qreg_q[1])
    circuit.measure(qreg_q[1], creg_c[1])
    
    return circuit


def level1(i):
    
    if i==1:
        level1_1()
        
    elif i==2:
        level1_2()
        
    elif i==3:
        level1_3()
        
    elif i==4:
        level1_4()
        
    elif i==5:
        level1_5()
        
    elif i==6:
        level1_6()
        
    return circuit