from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description(): 
    ld = LaunchDescription()
    
    remap_number_topic = ("number", "my_number")
    
    number_publisher_node = Node(
        package="exo1_py", 
        executable="number_publisher", 
        name="my_number_publisher", 
        remappings=[
            remap_number_topic
        ], 
        parameters=[
            {"number_to_publish": 4}
        ]
    )
    
    number_counter_node = Node(
        package="exo1_py", 
        executable="number_counter",
        name="my_number_counter",
        remappings=[
            remap_number_topic, 
            ("number_count", "my_number_count")
        ]
    )
    
    ld.add_action(number_publisher_node) 
    ld.add_action(number_counter_node)
    return ld 