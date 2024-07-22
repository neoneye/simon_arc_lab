# IDEA: wire world
import json
import os
import random
import numpy as np
from simon_arc_lab.rle.serialize import serialize
from simon_arc_lab.image_util import *
from simon_arc_lab.cellular_automaton import *
from simon_arc_lab.image_create_random_advanced import image_create_random_advanced
import matplotlib.pyplot as plt

def generate_dataset_item(seed):
    """
    Do a transformation from one image into another image.

    :param seed: The seed for the random number generator
    :return: A dictionary with the instruction, input, and output
    """
    min_image_size = 4
    max_image_size = 13

    transformation_ids = [
        'gameoflife_wrap',
        'gameoflife_nowrap',
        'highlife_wrap',
        'highlife_nowrap',
        'serviettes_wrap',
        'serviettes_nowrap',
        'cave_wrap',
        'cave_nowrap',
        'maze_wrap',
        'maze_nowrap',
    ]
    # transformation_weights = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
    # transformation_weights = [10, 0, 10, 0, 10, 0, 10, 0, 10, 0]
    transformation_weights = [10, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    transformation_id = random.Random(seed + 1001).choices(transformation_ids, weights=transformation_weights, k=1)[0]

    algorithm_names = [
        'SIMONCELLULARAUTOMATON',
        'SIMONCELLULARAUTOMATA',
        'SIMONSCELLULARAUTOMATON',
        'SIMONSCELLULARAUTOMATA',
        'SIMONCELLULARAUTOMATA',
        'SIMONSCELLULARAUTOMATA',
        'Simon-Cellular-Automata',
        'Simon-Cellular-Automaton',
        'Simons-Cellular-Automata',
        'Simons-Cellular-Automaton',
        'SimonCellularAutomata',
        'SimonCellularAutomaton',
        'SimonsCellularAutomata',
        'SimonsCellularAutomaton',
        'simon-cellular-automata',
        'simon-cellular-automaton',
        'simons-cellular-automata',
        'simons-cellular-automaton',
    ]
    algorithm_name = random.Random(seed + 1004).choice(algorithm_names)

    colors = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    random.Random(seed + 5).shuffle(colors)
    color0 = colors[0]
    color1 = colors[1]

    step_count = random.Random(seed + 1).randint(1, 1)

    instructions_gameoflife_wrap = [
        f'{algorithm_name}, Game of Life with wrapx and wrapy. Steps={step_count}. Dead cells have value {color0}. Alive cells have value {color1}.',
        f'{algorithm_name}, Game of Life with wrapxy. steps={step_count}. {color0} is dead. {color1} is alive.',
        f'{algorithm_name}, Game of Life with wrap. steps={step_count}. dead={color0} alive={color1}',
        f'{algorithm_name}, Game of Life wrap=xy. steps={step_count}. alive={color1}. dead={color0}.',
        f'{algorithm_name}, Game of Life wrap=both. steps={step_count}. live={color1}. dead={color0}.',
        f'{algorithm_name}, game of life wrap=both. steps={step_count}. live={color1}. dead={color0}.',
        f'{algorithm_name}, game-of-life wrap=both. steps={step_count}. live={color1}. dead={color0}.',
    ]

    instructions_gameoflife_nowrap = [
        f'{algorithm_name}, Game of Life without wrap. Steps={step_count}. Dead cells have value {color0}. Alive cells have value {color1}.',
        f'{algorithm_name}, Game of Life with nowrap. steps={step_count}. {color0} is dead. {color1} is alive.',
        f'{algorithm_name}, Game of Life with wrap=none. steps={step_count}. dead={color0} alive={color1}',
        f'{algorithm_name}, Game of Life wrap=no. steps={step_count}. alive={color1}. dead={color0}.',
        f'{algorithm_name}, Game of Life wrap=none. steps={step_count}. live={color1}. dead={color0}.',
        f'{algorithm_name}, game of life wrap=none. steps={step_count}. live={color1}. dead={color0}.',
        f'{algorithm_name}, game-of-life wrap=none. steps={step_count}. live={color1}. dead={color0}.',
    ]

    instructions_highlife_wrap = [
        f'{algorithm_name}, HighLife with wrapx and wrapy. Steps={step_count}. Dead cells have value {color0}. Alive cells have value {color1}.',
        f'{algorithm_name}, HighLife with wrapxy. steps={step_count}. {color0} is dead. {color1} is alive.',
        f'{algorithm_name}, HighLife with wrap. steps={step_count}. dead={color0} alive={color1}',
        f'{algorithm_name}, HighLife wrap=xy. steps={step_count}. alive={color1}. dead={color0}.',
        f'{algorithm_name}, HighLife wrap=both. steps={step_count}. live={color1}. dead={color0}.',
        f'{algorithm_name}, highlife wrap=both. steps={step_count}. live={color1}. dead={color0}.',
        f'{algorithm_name}, high-life wrap=both. steps={step_count}. live={color1}. dead={color0}.',
    ]

    instructions_highlife_nowrap = [
        f'{algorithm_name}, HighLife without wrap. Steps={step_count}. Dead cells have value {color0}. Alive cells have value {color1}.',
        f'{algorithm_name}, HighLife with nowrap. steps={step_count}. {color0} is dead. {color1} is alive.',
        f'{algorithm_name}, HighLife with wrap=none. steps={step_count}. dead={color0} alive={color1}',
        f'{algorithm_name}, HighLife wrap=no. steps={step_count}. alive={color1}. dead={color0}.',
        f'{algorithm_name}, HighLife wrap=none. steps={step_count}. live={color1}. dead={color0}.',
        f'{algorithm_name}, highlife wrap=none. steps={step_count}. live={color1}. dead={color0}.',
        f'{algorithm_name}, high-life wrap=none. steps={step_count}. live={color1}. dead={color0}.',
    ]

    instructions_serviettes_wrap = [
        f'{algorithm_name}, Serviettes with wrapx and wrapy. Steps={step_count}. Dead cells have value {color0}. Alive cells have value {color1}.',
        f'{algorithm_name}, Serviettes with wrapxy. steps={step_count}. {color0} is dead. {color1} is alive.',
        f'{algorithm_name}, Serviettes with wrap. steps={step_count}. dead={color0} alive={color1}',
        f'{algorithm_name}, Serviettes wrap=xy. steps={step_count}. alive={color1}. dead={color0}.',
        f'{algorithm_name}, Serviettes wrap=both. steps={step_count}. live={color1}. dead={color0}.',
        f'{algorithm_name}, serviettes wrap=both. steps={step_count}. live={color1}. dead={color0}.',
    ]

    instructions_serviettes_nowrap = [
        f'{algorithm_name}, Serviettes without wrap. Steps={step_count}. Dead cells have value {color0}. Alive cells have value {color1}.',
        f'{algorithm_name}, Serviettes with nowrap. steps={step_count}. {color0} is dead. {color1} is alive.',
        f'{algorithm_name}, Serviettes with wrap=none. steps={step_count}. dead={color0} alive={color1}',
        f'{algorithm_name}, Serviettes wrap=no. steps={step_count}. alive={color1}. dead={color0}.',
        f'{algorithm_name}, Serviettes wrap=none. steps={step_count}. live={color1}. dead={color0}.',
        f'{algorithm_name}, serviettes wrap=none. steps={step_count}. live={color1}. dead={color0}.',
    ]

    instructions_cave_wrap = [
        f'{algorithm_name}, Cave with wrapx and wrapy. Steps={step_count}. Dead cells have value {color0}. Alive cells have value {color1}.',
        f'{algorithm_name}, Cave with wrapxy. steps={step_count}. {color0} is dead. {color1} is alive.',
        f'{algorithm_name}, Cave with wrap. steps={step_count}. dead={color0} alive={color1}',
        f'{algorithm_name}, Cave wrap=xy. steps={step_count}. alive={color1}. dead={color0}.',
        f'{algorithm_name}, Cave wrap=both. steps={step_count}. live={color1}. dead={color0}.',
        f'{algorithm_name}, cave wrap=both. steps={step_count}. live={color1}. dead={color0}.',
    ]

    instructions_cave_nowrap = [
        f'{algorithm_name}, Cave without wrap. Steps={step_count}. Dead cells have value {color0}. Alive cells have value {color1}.',
        f'{algorithm_name}, Cave with nowrap. steps={step_count}. {color0} is dead. {color1} is alive.',
        f'{algorithm_name}, Cave with wrap=none. steps={step_count}. dead={color0} alive={color1}',
        f'{algorithm_name}, Cave wrap=no. steps={step_count}. alive={color1}. dead={color0}.',
        f'{algorithm_name}, Cave wrap=none. steps={step_count}. live={color1}. dead={color0}.',
        f'{algorithm_name}, cave wrap=none. steps={step_count}. live={color1}. dead={color0}.',
    ]

    instructions_maze_wrap = [
        f'{algorithm_name}, Maze with wrapx and wrapy. Steps={step_count}. Dead cells have value {color0}. Alive cells have value {color1}.',
        f'{algorithm_name}, Maze with wrapxy. steps={step_count}. {color0} is dead. {color1} is alive.',
        f'{algorithm_name}, Maze with wrap. steps={step_count}. dead={color0} alive={color1}',
        f'{algorithm_name}, Maze wrap=xy. steps={step_count}. alive={color1}. dead={color0}.',
        f'{algorithm_name}, Maze wrap=both. steps={step_count}. live={color1}. dead={color0}.',
        f'{algorithm_name}, maze wrap=both. steps={step_count}. live={color1}. dead={color0}.',
    ]

    instructions_maze_nowrap = [
        f'{algorithm_name}, Maze without wrap. Steps={step_count}. Dead cells have value {color0}. Alive cells have value {color1}.',
        f'{algorithm_name}, Maze with nowrap. steps={step_count}. {color0} is dead. {color1} is alive.',
        f'{algorithm_name}, Maze with wrap=none. steps={step_count}. dead={color0} alive={color1}',
        f'{algorithm_name}, Maze wrap=no. steps={step_count}. alive={color1}. dead={color0}.',
        f'{algorithm_name}, Maze wrap=none. steps={step_count}. live={color1}. dead={color0}.',
        f'{algorithm_name}, maze wrap=none. steps={step_count}. live={color1}. dead={color0}.',
    ]

    instructions = None
    if transformation_id == 'gameoflife_wrap':
        instructions = instructions_gameoflife_wrap
    elif transformation_id == 'gameoflife_nowrap':
        instructions = instructions_gameoflife_nowrap
    elif transformation_id == 'highlife_wrap':
        instructions = instructions_highlife_wrap
    elif transformation_id == 'highlife_nowrap':
        instructions = instructions_highlife_nowrap
    elif transformation_id == 'serviettes_wrap':
        instructions = instructions_serviettes_wrap
    elif transformation_id == 'serviettes_nowrap':
        instructions = instructions_serviettes_nowrap
    elif transformation_id == 'cave_wrap':
        instructions = instructions_cave_wrap
    elif transformation_id == 'cave_nowrap':
        instructions = instructions_cave_nowrap
    elif transformation_id == 'maze_wrap':
        instructions = instructions_maze_wrap
    elif transformation_id == 'maze_nowrap':
        instructions = instructions_maze_nowrap
    else:
        raise Exception("Unreachable code reached")

    instruction = random.Random(seed + 1005).choice(instructions)

    width = random.Random(seed + 1).randint(min_image_size, max_image_size)
    height = random.Random(seed + 2).randint(min_image_size, max_image_size)

    ratios = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
    ratio = random.Random(seed + 5).choice(ratios)
    input_image = image_create_random_with_two_colors(width, height, 0, 1, ratio, seed + 6)
    # print(input_image)

    mutate_input_id = random.Random(seed + 3).randint(0, 5)
    # print(mutate_input_id)
    if mutate_input_id == 0:
        pass
    elif mutate_input_id == 1:
        input_image = CARuleGameOfLife().apply_wrap(input_image, wrapx=True, wrapy=True, outside_value=0, step_count=1)
    elif mutate_input_id == 2:
        input_image = CARuleHighLife().apply_wrap(input_image, wrapx=True, wrapy=True, outside_value=0, step_count=1)
    elif mutate_input_id == 3:
        input_image = CARuleServiettes().apply_wrap(input_image, wrapx=True, wrapy=True, outside_value=0, step_count=1)
    elif mutate_input_id == 4:
        input_image = CARuleCave().apply_wrap(input_image, wrapx=True, wrapy=True, outside_value=0, step_count=1)
    elif mutate_input_id == 5:
        input_image = CARuleMaze().apply_wrap(input_image, wrapx=True, wrapy=True, outside_value=0, step_count=1)
    # print(input_image)

    output = None
    if transformation_id == 'gameoflife_wrap':
        output_image = CARuleGameOfLife().apply_wrap(input_image, wrapx=True, wrapy=True, outside_value=0, step_count=step_count)
    elif transformation_id == 'gameoflife_nowrap':
        output_image = CARuleGameOfLife().apply_wrap(input_image, wrapx=False, wrapy=False, outside_value=0, step_count=step_count)
    elif transformation_id == 'highlife_wrap':
        output_image = CARuleHighLife().apply_wrap(input_image, wrapx=True, wrapy=True, outside_value=0, step_count=step_count)
    elif transformation_id == 'highlife_nowrap':
        output_image = CARuleHighLife().apply_wrap(input_image, wrapx=False, wrapy=False, outside_value=0, step_count=step_count)
    elif transformation_id == 'serviettes_wrap':
        output_image = CARuleServiettes().apply_wrap(input_image, wrapx=True, wrapy=True, outside_value=0, step_count=step_count)
    elif transformation_id == 'serviettes_nowrap':
        output_image = CARuleServiettes().apply_wrap(input_image, wrapx=False, wrapy=False, outside_value=0, step_count=step_count)
    elif transformation_id == 'cave_wrap':
        output_image = CARuleCave().apply_wrap(input_image, wrapx=True, wrapy=True, outside_value=0, step_count=step_count)
    elif transformation_id == 'cave_nowrap':
        output_image = CARuleCave().apply_wrap(input_image, wrapx=False, wrapy=False, outside_value=0, step_count=step_count)
    elif transformation_id == 'maze_wrap':
        output_image = CARuleMaze().apply_wrap(input_image, wrapx=True, wrapy=True, outside_value=0, step_count=step_count)
    elif transformation_id == 'maze_nowrap':
        output_image = CARuleMaze().apply_wrap(input_image, wrapx=False, wrapy=False, outside_value=0, step_count=step_count)
    else:
        raise Exception("Unreachable code reached")
    
    color_mapping = {}
    for color_index in range(len(colors)):
        color = colors[color_index]
        color_mapping[color_index] = color

    input_image2 = image_replace_colors(input_image, color_mapping)
    output_image2 = image_replace_colors(output_image, color_mapping)
    input = serialize(input_image2)
    output = serialize(output_image2)

    # print(instruction)
    # print(input_image2)
    # print(output_image2)
    # plt.imshow(input_image, cmap='gray')
    # plt.show()
    # plt.imshow(output_image, cmap='gray')
    # plt.show()

    dict = {
        'instruction': instruction,
        'input': input,
        'output': output
    }
    return dict

def generate_dataset(max_num_samples=1000, max_byte_size=1024*1024, seed_start=400000):
    dataset = []
    dataset_byte_size = 0
    for i in range(max_num_samples):
        item = generate_dataset_item(seed_start + i)
        bytes = len(json.dumps(item))
        if dataset_byte_size + bytes > max_byte_size:
            break
        dataset_byte_size += bytes
        dataset.append(item)
    return dataset

dataset = generate_dataset(
    max_num_samples=100000,
    max_byte_size=1024*1024*60,
)

# Save dataset to file
filename = 'dataset_cellular_automaton.jsonl'
with open(filename, 'w') as f:
    for item in dataset:
        f.write(json.dumps(item) + '\n')

# Summary
file_size = os.path.getsize(filename)
print(f"Generated {len(dataset)} samples, saved to {filename}, file size: {file_size} bytes.")
