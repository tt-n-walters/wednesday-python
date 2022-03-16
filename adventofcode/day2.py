from aoc_tools import get_input

instructions = get_input(2).splitlines()

horizontal = [ins for ins in instructions if ins.startswith("forward")]
vertical = [ins for ins in instructions if not ins.startswith("forward")]


def parse_instruction(instruction):
    direction, amount = instruction.split()
    if direction == "up":
        return int(amount) * -1
    else:
        return int(amount)
    

h_movements = list(map(parse_instruction, horizontal))
v_movements = list(map(parse_instruction, vertical))

aim = v_movements.copy()
aim_movements = []
for i, h in enumerate(h_movements[:10]):
    current_aim = sum(aim[:i+1])
    print(i, h, aim[i], current_aim)
    aim_movements.append(h * current_aim)


print(aim_movements)
exit()


total_h = sum(h_movements)
total_v = sum(v_movements)
total = total_h * total_v

print(total_h)
print(total_v)
print(total)