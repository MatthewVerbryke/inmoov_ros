#!/usr/bin/env python
# Copyright 2017 University of Cincinnati
# All rights reserved. See LICENSE file at:
# https://github.com/MatthewVerbryke/inmoov-ros
# Additional copyright may be held by others, as reflected in the commit history.


import sys
from std_msgs.msg import Float64
import thread

import rospy


class FingerMimicking():
    """
    A ROS node that implements mimic joints for the InMoov's hands in
    Gazebo. While UDRF and Rviz support mimic joints, Gazebo does not.
    This node takes the overall finger command angle, calculates
    the nessecary positions for all of the joints in the finger (based
    on a 'mimic factor' from the URDF), and then commands these joints
    to the resulting angle. This should replicate how the fingers work
    on the actual InMoov hand.
    
    Mimic factors for the InMoov hand:

    rthumb_fact = [-0.75, 1]
    rindex_fact = [1, 1]
    rmiddle_fact = [1, 1]
    rring_fact = [-0.1, 1, 1]
    rpinky_fact = [-0.1, 1, 1]
    lthumb_fact = [0.75, 1]
    lindex_fact = [1, 1]
    lmiddle_fact = [1, 1]
    lring_fact = [0.1, 1, 1]
    lpinky_fact = [0.1, 1, 1]
    
    NOTE: This is not needed for running on the actual robot.
    """
    
    def __init__(self):
        """Initialize"""
        
        # Initialize node
        rospy.init_node("finger_joint_mimic")

        # Initialize cleanup
        rospy.on_shutdown(self.cleanup)

        # Get a lock
        self.lock = thread.allocate_lock()

        # Number of joints of each type
        Ni = 10 # independent
        self.Nd = 24 # dependent

        # Initialize publish topic list
        self.pubf = [] 

        # Define topics and related parameters
        initstringf = '/inmoov/'
        finalstringf = '/command'

        indep_joint_names = ['right_thumb_controller',
                             'right_index_controller',
                             'right_middle_controller',
                             'right_ring_controller',
                             'right_pinky_controller',
                             'left_thumb_controller',
                             'left_index_controller',
                             'left_middle_controller',
                             'left_ring_controller',
                             'left_pinky_controller']

        dep_joint_names = ['right_thumbCMC_position_controller',
                           'right_thumbIP_position_controller',
                           'right_indexMCP_position_controller',
                           'right_indexDIP_position_controller',
                           'right_middleMCP_position_controller',
                           'right_middleDIP_position_controller',
                           'right_ringCMC_position_controller',
                           'right_ringPIP_position_controller',
                           'right_ringDIP_position_controller',
                           'right_pinkyCMC_position_controller',
                           'right_pinkyPIP_position_controller',
                           'right_pinkyDIP_position_controller',
                           'left_thumbCMC_position_controller',
                           'left_thumbIP_position_controller',
                           'left_indexMCP_position_controller',
                           'left_indexDIP_position_controller',
                           'left_middleMCP_position_controller',
                           'left_middleDIP_position_controller',
                           'left_ringCMC_position_controller',
                           'left_ringPIP_position_controller',
                           'left_ringDIP_position_controller',
                           'left_pinkyCMC_position_controller',
                           'left_pinkyPIP_position_controller',
                           'left_pinkyDIP_position_controller']

        callbacksf = [self.get_RT_command,
                      self.get_RI_command,
                      self.get_RM_command,
                      self.get_RR_command,
                      self.get_RP_command,
                      self.get_LT_command,
                      self.get_LI_command,
                      self.get_LM_command,
                      self.get_LR_command,
                      self.get_LP_command]

        # Setup subscriber topics 
        for i in range(Ni):
            rospy.Subscriber(initstringf + indep_joint_names[i] + finalstringf, Float64, callbacksf[i])

        # Setup publisher topics
        for i in range(self.Nd):
            self.pubf.append( rospy.Publisher(initstringf + dep_joint_names[i] + finalstringf, Float64, queue_size=1) )

        # Wait for topics to be published before beginning
        for i in range(Ni):
            rospy.wait_for_message(initstringf + indep_joint_names[i] + finalstringf, Float64)

        # Run program
        self.finger_mimic_command(self.Nd, self.pubf)

    def finger_mimic_command(self, N, pub):
        """Calculate the nessecary command angles for all dependent 
           finger joints."""

        oldgoal = []

        # Until ROS shutdown
        while not rospy.is_shutdown():

            # Acquire lock
            self.lock.acquire()

            try:
                
                currentgoal =  [self.Rthumb_command,
                                self.Rindex_command,
                                self.Rmiddle_command,
                                self.Rring_command,
                                self.Rpinky_command,
                                self.Lthumb_command,
                                self.Lindex_command,
                                self.Lmiddle_command,
                                self.Lring_command,
                                self.Lpinky_command]

                # If the goal position has not changed...
                if (currentgoal == oldgoal):
                    
                    # Continue publishing
                    for i in range(N):
                        pub[i].publish(fingergoal[i])

                # The goal has changed...
                else:

                    # Compute new dependent joint angles
                    R_angle1 = -0.75 * self.Rthumb_command
                    R_angle2 = self.Rthumb_command
                    R_angle3 = R_angle4 = self.Rindex_command
                    R_angle5 = R_angle6 = self.Rmiddle_command
                    R_angle7 = -0.1 * self.Rring_command
                    R_angle8 = R_angle9 = self.Rring_command
                    R_angle10 = -0.1 * self.Rpinky_command
                    R_angle11 = R_angle12 = self.Rpinky_command

                    L_angle1 = 0.75 * self.Lthumb_command
                    L_angle2 = self.Lthumb_command
                    L_angle3 = L_angle4 = self.Lindex_command
                    L_angle5 = L_angle6 = self.Lmiddle_command
                    L_angle7 = 0.1 * self.Lring_command
                    L_angle8 = L_angle9 = self.Lring_command
                    L_angle10 = 0.1 * self.Lpinky_command
                    L_angle11 = L_angle12 = self.Lpinky_command
            
                    # Amalgamate joint angles into single list
                    fingergoal =   [R_angle1, 
                                    R_angle2, 
                                    R_angle3, 
                                    R_angle4, 
                                    R_angle5, 
                                    R_angle6, 
                                    R_angle7, 
                                    R_angle8, 
                                    R_angle9, 
                                    R_angle10, 
                                    R_angle11, 
                                    R_angle12, 
                                    L_angle1, 
                                    L_angle2, 
                                    L_angle3, 
                                    L_angle4, 
                                    L_angle5, 
                                    L_angle6, 
                                    L_angle7, 
                                    L_angle8, 
                                    L_angle9, 
                                    L_angle10, 
                                    L_angle11, 
                                    L_angle12]

                    # Publish new commands
                    for i in range(N):
                        pub[i].publish(fingergoal[i])

                    # Set current goal as "old goal"
                    oldgoal = currentgoal

            finally:
                
                # Release Lock
                self.lock.release()

    def get_RT_command(self, msg):
        """Right thumb callback function"""
        self.Rthumb_command = msg.data

    def get_RI_command(self, msg):
        """Right index finger callback function"""
        self.Rindex_command = msg.data

    def get_RM_command(self, msg):
        """Right middle finger callback function"""
        self.Rmiddle_command = msg.data

    def get_RR_command(self, msg):
        """Right ring finger callback function"""
        self.Rring_command = msg.data

    def get_RP_command(self, msg):
        """Right pinky finger callback function"""
        self.Rpinky_command = msg.data

    def get_LT_command(self, msg):
        """Left thumb callback function"""
        self.Lthumb_command = msg.data

    def get_LI_command(self, msg):
        """Left index finger callback function"""
        self.Lindex_command = msg.data

    def get_LM_command(self, msg):
        """Left middle finger callback function"""
        self.Lmiddle_command = msg.data

    def get_LR_command(self, msg):
        """Left ring finger callback function"""
        self.Lring_command = msg.data

    def get_LP_command(self, msg):
        """Left pinky finger callback function"""
        self.Lpinky_command = msg.data

    def cleanup(self):
        """Node cleanup function"""
        rospy.loginfo("Shutting down node...")
        rospy.sleep(1)
        

if __name__ == '__main__':
    try:
        FingerMimicking()
    except rospy.ROSInterruptException:
        rospy.loginfo("Finger mimicking node terminated")

# -- EOF--
