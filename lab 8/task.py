def is_valid_command(command):
    return command in ('0', '1', '2', 'exit')

def can_burn(power, fuel):
    return fuel >= power

def simulate_step(height, speed, fuel, power, gravity, thrust_step):
    fuel -= power

    speed = speed + gravity - thrust_step * power

    if speed < 0:
        speed = 0

    