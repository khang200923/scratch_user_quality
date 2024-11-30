# Scratch User Quality

This project evaluates the quality of Scratch projects and users based on various metrics.

## Features

- Fetches Scratch user projects from the Scratch API.
- Evaluates the quality of individual Scratch projects, using gpt-4o-mini.
- Calculates the overall quality of a Scratch user based on their top projects.

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/khang200923/scratch_user_quality.git
    cd scratch_user_quality
    ```

2. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

3. Create a `.env` file in the root directory and add your OpenAI API key:
    ```env
    OPENAI_API_KEY=your_openai_api_key
    ```

## Usage

Run the main script:
```sh
python [main.py]
```

You can then input a Scratch username to get the quality evaluation of their projects.
Example:
```
>> griffpatch
"Appel v1.4": 6.00 hours
"Massive Multiplayer Platformer v1.3": 3.75 hours
"Level EATEN! - v0.12": 3.00 hours
"slither.io v1.11 server 2": 4.75 hours
"Minecraft-ish MMO v1.7": 11.00 hours
"Griffpatch's Blue Line Filter": 3.17 hours
"Ball Physics Scroll v0.4": 2.42 hours
"CUBES v0.19 - Work In Progress": 3.50 hours
"Cloud Platformer Multiplayer Fun v1.42 #3": 5.00 hours
"slither.io v1.13 (#3)": 4.75 hours
@griffpatch: 105.77 hours
>> Will_Wam
"Dungeon Journey 2": 3.42 hours
"Cube Jumper": 1.33 hours
"Way of the Ninja": 2.83 hours
"Castle of Shadows": 2.83 hours
"Armenia Rush": 2.25 hours
"Beach Volleyball": 1.67 hours
"Super Mario Bros. Level Pack 2023": 2.50 hours
"Fortune Cookie Simulator": 1.00 hours
"☁ Cloud Vote [Spring Edition]": 1.67 hours
"Will_Wam Text Engine": 1.33 hours
@Will_Wam: 46.55 hours
```
