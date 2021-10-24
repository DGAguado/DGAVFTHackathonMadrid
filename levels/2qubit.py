from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit
from numpy import pi

# Este programa SOBREABUSA de imágenes...
from IPython.display import Image
PATH = "encounters/"

def level1_1():

    qreg_q = QuantumRegister(2, 'q')
    creg_c = ClassicalRegister(2, 'c')
    circuit = QuantumCircuit(qreg_q, creg_c)

    circuit.barrier(qreg_q[0])
    circuit.barrier(qreg_q[1])
    circuit.x(qreg_q[0])
    circuit.measure(qreg_q[0], creg_c[0])
    circuit.measure(qreg_q[1], creg_c[1])
    
    battle=Image(filename = PATH + "encuentro2_1.png", width=300, height=300)
    
    return circuit,battle

def level1_2():
    
    qreg_q = QuantumRegister(2, 'q')
    creg_c = ClassicalRegister(2, 'c')
    circuit = QuantumCircuit(qreg_q, creg_c)

    circuit.barrier(qreg_q[0])
    circuit.barrier(qreg_q[1])
    circuit.measure(qreg_q[0], creg_c[0])
    circuit.measure(qreg_q[1], creg_c[1])
    
    battle=Image(filename = PATH + "encuentro2_2.png", width=300, height=300)
    
    return circuit,battle

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
    
    battle=Image(filename = PATH + "encuentro2_3.png", width=300, height=300)
    
    return circuit,battle

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
    
    battle=Image(filename = PATH + "encuentro2_4.png", width=300, height=300)
    
    return circuit,battle

def level1_5():

    qreg_q = QuantumRegister(2, 'q')
    creg_c = ClassicalRegister(2, 'c')
    circuit = QuantumCircuit(qreg_q, creg_c)

    circuit.barrier(qreg_q[1])
    circuit.barrier(qreg_q[0])
    circuit.cx(qreg_q[0], qreg_q[1])
    circuit.measure(qreg_q[0], creg_c[0])
    circuit.measure(qreg_q[1], creg_c[1])
    
    battle=Image(filename = PATH + "encuentro2_5.png", width=300, height=300)
    
    return circuit,battle

def level1_6():

    qreg_q = QuantumRegister(2, 'q')
    creg_c = ClassicalRegister(2, 'c')
    circuit = QuantumCircuit(qreg_q, creg_c)

    circuit.barrier(qreg_q[1])
    circuit.barrier(qreg_q[0])
    circuit.swap(qreg_q[0], qreg_q[1])
    circuit.cx(qreg_q[0], qreg_q[1])
    circuit.measure(qreg_q[1], creg_c[1])
    circuit.measure(qreg_q[0], creg_c[0])
    
    battle=Image(filename = PATH + "encuentro2_6.png", width=300, height=300)
    
    return circuit,battle

def level1_7():
    
    qreg_q = QuantumRegister(2, 'q')
    creg_c = ClassicalRegister(2, 'c')
    circuit = QuantumCircuit(qreg_q, creg_c)

    circuit.barrier(qreg_q[0])
    circuit.barrier(qreg_q[1])
    circuit.id(qreg_q[0])
    circuit.reset(qreg_q[1])
    circuit.measure(qreg_q[1], creg_c[1])
    circuit.measure(qreg_q[0], creg_c[0])
    
    battle=Image(filename = PATH + "encuentro2_7.png", width=300, height=300)
    
    return circuit,battle


def level1(i):
    
    if i==1:
        circuit,battle=level1_1()
        
    elif i==2:
        circuit,battle=level1_2()
        
    elif i==3:
        circuit,battle=level1_3()
        
    elif i==4:
        circuit,battle=level1_4()
        
    elif i==5:
        circuit,battle=level1_5()
        
    elif i==6:
        circuit,battle=level1_6()
        
    elif i==7:
        circuit,battle=level1_7()
        
    return circuit,battle