Ryanteck Motor Driver Board
---------------------------

### Cheat Sheet

The rtkmcb Python library allows you to independently control left and right motors, in addition to controlling both at once with a variety of, hopefully, intuitive commands;

#### Left or Right Motor

    # Move forwards at speed 0 ( stopped ) to 100
    mcb.left_motor.forwards( speed )
    
    # Move backwards at speed 0 ( stopped ) to 100
    mcb.left_motor.backwards( speed )
    
    # Set speed of the motor from -100 ( full reverse ) to 100 ( full forward )
    mcb.left_motor.speed( speed )
    
    # Stop
    mcb.left_motor.stop()
    
All of these also work for the "right_motor"

#### Both

    # Set speed of both motors from -100 to 100
    mcb.speed( speed )
    
    # Alternatively, set speed independently
    mcb.speed( left_speed, right_speed )
    
    # Turn left
    mcb.left( speed )
    
    # Turn right
    mcb.right( speed )
    
    # Turn -100 left to 100 right
    mcb.turn( speed ) 
    
    # Stop
    mcb.stop()
