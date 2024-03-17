# Electromagnetic-balance-bar-with-pid
Use electromagnetic balance to help keep the rod down

#This is a device that won the third national prize at the 9th cupec

（CHINA UNDERGRADUATE PHYSICS EXPERIMENT COMPETITION）

Describe:

The primary objective of the "Unfalling Rod" experiment is to deepen the understanding of physical concepts such as angular momentum, moment of inertia, and equilibrium stability, while exploring how objects maintain balance under minor disturbances. Through this experiment, we can investigate the stability and equilibrium conditions of objects and derive formulas such as the rotational inertia of a rod, thereby enhancing comprehension of the law of conservation of angular momentum. Furthermore, this experiment aids in exploring various phenomena and principles in physics, including rotation, precession, and stability, thereby improving the experimental skills and scientific literacy of learners.

Creating a practical application device or experimental research apparatus to help a rod remain stable and upright under the influence of forces such as wind primarily involves constructing a physical system capable of maintaining balance and stability. Balanced systems are encountered in various aspects of our lives, with common examples including objects like a "Tippy Toy," which increases resistance to tipping by altering the center of mass, gyroscopes that rely on moment of inertia, and dampers that utilize their significant inertia. Additionally, industrial applications utilize counterforce structures, among others. Our unique approach in this experiment innovatively utilizes electricity and magnetism. By employing principles such as electromagnetic induction and control through circuitry, we aim to apply a controllable magnetic force to the rod, opposing external forces and preventing it from falling.

In principle, we utilize electromagnetic induction, along with Faraday's law, to establish a circuit comprising an ESP32 development board, MOSFET transistors for control, servo motors, and a solenoid coil. This setup enables automatic correction of the rod's vertical position in response to wind forces. The operation of the circuit proceeds as follows:
1. Adjust the speed and angle of the electric fan to exert a stable force on the center of the rod, causing it to tilt.
2. The MPU6050 three-axis accelerometer module, aligned with the rod, detects changes in angular velocity, transmitting data to the computer for analysis and display.
3. The computer receives angle change data, analyzes it, determines the direction of the rod's tilt, and swiftly controls the servo motor to rotate to the appropriate position, maximizing the effectiveness of the solenoid coil.
4. Simultaneously, upon receiving data on the rod's angle change, the MOSFET transistor is adjusted to control the current flowing through the coils, thereby altering the magnetic field. The rod returns to its balanced state under the influence of the magnetic field, and the experiment concludes.

In terms of innovation, our experiment significantly deviates from traditional methods, both in principle and approach. We autonomously constructed a system comprising a calculator and circuitry to facilitate automated measurement and data collection, leveraging sensors like the three-axis accelerometer to achieve superior advantages over manual measurements. Additionally, based on measured data, our internal code automatically calculates and precisely adjusts the solenoid coil's current, generating a magnetic force equal in magnitude and opposite in direction to the wind force, thereby achieving vertical correction automatically.

Extensive experimentation confirms the scientific and practical validity of our device, demonstrating both its innovative approach and feasibility. It effectively stabilizes the rod under wind forces while providing convenient experimental results, quantifying its ability to resist external forces. Moreover, its characteristics of automation and high precision hold substantial potential value, making it suitable for real-world applications such as:
1. Direct utilization as a wind measurement instrument.
2. Due to its rapid electromagnetic balancing capabilities, it can be widely applied to various objects requiring continuous balance maintenance, such as self-balancing vehicles.
3. As an auxiliary balancing device, its precision adjustment capabilities enable it to interface with other devices, such as cameras or scientific instruments requiring stability, ensuring vertical balance even in outdoor environments prone to disturbances, thus reducing measurement errors.
4. Vertical attitude correction can be applied to solar panels, wind turbines, and even aerospace vehicles like rockets and satellites.

Overall, the "Unfalling Rod" experiment holds substantial promise for practical applications across various fields, ranging from meteorology to aerospace engineering, and its innovative approach and automation capabilities render it highly desirable for scientific research and industrial utilization.
