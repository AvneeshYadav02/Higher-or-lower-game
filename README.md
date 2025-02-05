# Higher Follower Count Game

## Overview
This is a simple Python game where the player guesses which celebrity has a higher follower count. The game presents two random personalities from a dataset, and the player must choose the one with more followers. The game continues until the player makes an incorrect guess.

## How to Play
1. The game displays two random celebrities along with their descriptions and countries.
2. The player selects one by entering `1` for the first option or `2` for the second.
3. If the player guesses correctly, the higher-follower option is replaced, and a new comparison starts.
4. The game continues until the player makes an incorrect guess, at which point their score is displayed.

## Features
- Randomized selection of personalities for each round.
- Ensures that the two compared choices are always different.
- Input validation to handle incorrect or invalid entries.
- A simple scoring system that tracks consecutive correct guesses.

## Requirements
- Python 3.x
- A dataset containing a list of personalities with their names, descriptions, countries, and follower counts.

## Setup and Installation
1. Clone this repository:
   ```sh
   git clone https://github.com/yourusername/higher-follower-game.git
   ```
2. Navigate to the project folder:
   ```sh
   cd higher-follower-game
   ```
3. Ensure you have the required files:
   - `game_data.py` (containing the list of celebrities and their follower counts)
   - `art.py` (for logo and visual separators)
4. Run the game:
   ```sh
   python game.py
   ```

