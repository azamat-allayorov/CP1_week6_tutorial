
def first_tool_position(tools, wanted):
    for i in range(len(tools)):
        if tools[i] == wanted:
            return i
    return -1


def all_tool_positions(tools, wanted):
    positions = []
    for i in range(len(tools)):
        if tools[i] == wanted:
            positions.append(i)
    return positions

tools = ["hammer", "drill", "saw", "drill", "wrench"]

wanted = "hammer"

for wanted in ['drill', "wrench"]:
    first = first_tool_position(tools, wanted)
    all = all_tool_positions(tools, wanted)
    print(f"{wanted}: first position = {first}, all positions = {all}")
