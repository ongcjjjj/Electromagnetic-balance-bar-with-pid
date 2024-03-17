from machine import Pin, I2C
from time import sleep_ms
import math

# Define MPU6050 registers
MPU6050_ADDR = 0x68
MPU6050_REG_PWR_MGMT_1 = 0x6B
MPU6050_REG_GYRO_CONFIG = 0x1B
MPU6050_REG_ACCEL_CONFIG = 0x1C
MPU6050_REG_ACCEL_XOUT_H = 0x3B
MPU6050_REG_GYRO_XOUT_H = 0x43

# Define pins for MOSFET control
MOSFET_PIN_1 = 12  # Change to your pin numbers
MOSFET_PIN_2 = 13  # Change to your pin numbers

# Define PID parameters
kp = 1.0  # Proportional gain
ki = 0.0  # Integral gain
kd = 0.0  # Derivative gain

# Define target yaw angle
target_yaw = 0.0

# Initialize I2C
i2c = I2C(scl=Pin(22), sda=Pin(21))

# Initialize MOSFET pins
mosfet_1 = Pin(MOSFET_PIN_1, Pin.OUT)
mosfet_2 = Pin(MOSFET_PIN_2, Pin.OUT)

# Initialize PID variables
integral = 0.0
prev_error = 0.0

# MPU6050 initialization function
def init_mpu6050():
    i2c.writeto_mem(MPU6050_ADDR, MPU6050_REG_PWR_MGMT_1, b'\x00')  # Wake up MPU6050
    i2c.writeto_mem(MPU6050_ADDR, MPU6050_REG_GYRO_CONFIG, b'\x08')  # Set full scale range for gyroscope
    i2c.writeto_mem(MPU6050_ADDR, MPU6050_REG_ACCEL_CONFIG, b'\x08')  # Set full scale range for accelerometer

# MPU6050 read function
def read_mpu6050():
    accel_z = int.from_bytes(i2c.readfrom_mem(MPU6050_ADDR, MPU6050_REG_ACCEL_XOUT_H, 2), 'big', signed=True) / 16384.0
    gyro_z = int.from_bytes(i2c.readfrom_mem(MPU6050_ADDR, MPU6050_REG_GYRO_XOUT_H, 2), 'big', signed=True) / 131.0
    return accel_z, gyro_z

# PID control function
def pid_control(current_yaw):
    global integral, prev_error
    error = target_yaw - current_yaw
    integral += error
    derivative = error - prev_error
    output = kp * error + ki * integral + kd * derivative
    prev_error = error
    return output

# Function to control MOSFETs based on PID output
def control_mosfets(pid_output):
    if pid_output > 0:
        mosfet_1.value(1)
        mosfet_2.value(0)
    else:
        mosfet_1.value(0)
        mosfet_2.value(1)

# Main loop
def main():
    init_mpu6050()
    while True:
        accel_z, gyro_z = read_mpu6050()
        
        # Calculate yaw angle (rotation around z-axis)
        current_yaw = math.atan2(accel_z, gyro_z) * (180.0 / math.pi)
        
        # PID control to adjust MOSFETs based on current yaw angle
        pid_output = pid_control(current_yaw)
        control_mosfets(pid_output)
        
        print("Current Yaw Angle: {:.2f} degrees, PID Output: {:.2f}".format(current_yaw, pid_output))
        sleep_ms(100)  # Adjust delay as needed

if __name__ == "__main__":
    main()
