import rclpy
from pymycobot.mycobot import MyCobot
from rclpy.node import Node
from sensor_msgs.msg import JointState
import os
import time
import math
import numpy as np

class Unity_Subscriber(Node):
    def __init__(self): 
        super().__init__("control_slider")

        self.angle_base = 0.0
        self.angle_shoulder = 0.0
        self.angle_elbow = 0.0
	
        self.subscription = self.create_subscription(JointState, "/unity/joint_states", self.listener_callback, 10)
        self.subscription


        self.publisher_ = self.create_publisher(JointState, '/joint_states', 10)
        timer_period = 0.1  # segundos
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.joint_state = JointState()

        self.joint_state.name = ['joint_1', 'joint_2', 'joint_3', 'joint_4', 'joint_5', 'joint_6', 'gripper_joint_left']  # Nombres de las articulaciones
        self.joint_state.position = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]  # Posiciones iniciales de las articulaciones

        
    def listener_callback(self, msg):
        self.angle_base = msg.position[0]
        self.angle_shoulder = msg.position[1]
        self.angle_elbow = msg.position[2]
        

    def timer_callback(self):
        self.joint_state.header.stamp = self.get_clock().now().to_msg()
        
        # Aquí puedes actualizar los ángulos de las articulaciones
        self.joint_state.position[0] = self.angle_base
        self.joint_state.position[1] = np.deg2rad(90) - self.angle_shoulder
        self.joint_state.position[2] = np.deg2rad(90) - self.angle_elbow

        self.publisher_.publish(self.joint_state)
        self.get_logger().info('Publishing joint states: "%s"' % str(self.joint_state.position))

def main(args=None):
    rclpy.init(args=args)
    untiy_subscriber = Unity_Subscriber()
    
    rclpy.spin(untiy_subscriber)
    
    untiy_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()
  
