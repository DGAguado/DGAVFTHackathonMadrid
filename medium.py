from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit
from numpy import pi

def level2_1():

    qreg_q = QuantumRegister(3, 'q')
    creg_c = ClassicalRegister(3, 'c')
    circuit = QuantumCircuit(qreg_q, creg_c)

    circuit.barrier(qreg_q[0])
    circuit.barrier(qreg_q[1])
    circuit.barrier(qreg_q[2])
    circuit.y(qreg_q[0])
    circuit.ccx(qreg_q[2], qreg_q[0], qreg_q[1])
    circuit.h(qreg_q[0])
    circuit.measure(qreg_q[1], creg_c[1])
    
    return circuit

def level2_2():

    qreg_q = QuantumRegister(3, 'q')
    creg_c = ClassicalRegister(3, 'c')
    circuit = QuantumCircuit(qreg_q, creg_c)

    circuit.barrier(qreg_q[0])
    circuit.barrier(qreg_q[1])
    circuit.barrier(qreg_q[2])
    circuit.cx(qreg_q[2], qreg_q[1])
    circuit.cx(qreg_q[1], qreg_q[0])
    circuit.cx(qreg_q[0], qreg_q[2])
    circuit.measure(qreg_q[0], creg_c[0])
    
    return circuit

def level2_3():

    qreg_q = QuantumRegister(3, 'q')
    creg_c = ClassicalRegister(3, 'c')
    circuit = QuantumCircuit(qreg_q, creg_c)

    circuit.barrier(qreg_q[0])
    circuit.barrier(qreg_q[1])
    circuit.h(qreg_q[1])
    circuit.barrier(qreg_q[2])
    circuit.swap(qreg_q[1], qreg_q[2])
    circuit.z(qreg_q[1])
    circuit.h(qreg_q[2])
    circuit.swap(qreg_q[0], qreg_q[1])
    circuit.h(qreg_q[0])
    circuit.measure(qreg_q[1], creg_c[1])
    
    return circuit

def level2_4():

    qreg_q = QuantumRegister(3, 'q')
    creg_c = ClassicalRegister(3, 'c')
    circuit = QuantumCircuit(qreg_q, creg_c)

    circuit.barrier(qreg_q[0])
    circuit.barrier(qreg_q[1])
    circuit.barrier(qreg_q[2])
    circuit.y(qreg_q[2])
    circuit.cx(qreg_q[2], qreg_q[1])
    circuit.cx(qreg_q[0], qreg_q[1])
    circuit.h(qreg_q[2])
    circuit.h(qreg_q[1])
    circuit.z(qreg_q[2])
    circuit.measure(qreg_q[1], creg_c[1])
    circuit.measure(qreg_q[2], creg_c[2])

    return circuit
    
def level2_5():

    qreg_q = QuantumRegister(3, 'q')
    creg_c = ClassicalRegister(3, 'c')
    circuit = QuantumCircuit(qreg_q, creg_c)

    circuit.barrier(qreg_q[0])
    circuit.barrier(qreg_q[2])
    circuit.x(qreg_q[0])
    circuit.barrier(qreg_q[1])
    circuit.ccx(qreg_q[0], qreg_q[1], qreg_q[2])
    circuit.swap(qreg_q[0], qreg_q[1])
    circuit.swap(qreg_q[1], qreg_q[2])
    circuit.y(qreg_q[1])
    circuit.ccx(qreg_q[2], qreg_q[0], qreg_q[1])
    circuit.measure(qreg_q[1], creg_c[1])
    
    return circuit



def level2(i):
    
    if i==1:
        level2_1()
        
    elif i==2:
        level2_2()
        
    elif i==3:
        level2_3()
        
    elif i==4:
        level2_4()
        
    elif i==5:
        level2_5()
        
    return circuit