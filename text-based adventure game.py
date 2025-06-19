import time
import sys
import random
from colorama import init, Fore, Back, Style

init()  # Initialize colorama

class AdventureGame:
    def __init__(self):
        self.inventory = []
        self.health = 100
        self.game_over = False
        self.current_room = "start"
        self.rooms = self._initialize_rooms()
        self.colors = {
            "title": Fore.YELLOW + Style.BRIGHT,
            "header": Fore.CYAN + Style.BRIGHT,
            "text": Fore.WHITE,
            "success": Fore.GREEN + Style.BRIGHT,
            "warning": Fore.YELLOW,
            "danger": Fore.RED + Style.BRIGHT,
            "item": Fore.MAGENTA,
            "health": Fore.GREEN,
            "command": Fore.BLUE,
            "exit": Fore.CYAN,
        }

    def _initialize_rooms(self):
        return {
            "start": {
                "name": "Cave Entrance",
                "description": "You stand before a dark cave mouth, the cool damp air whispering secrets of the depths. To the east, sunlight filters through dense foliage.",
                "exits": {"north": "cave_path", "east": "forest_edge"},
                "items": ["torch"],
                "art": r"""
                    _____
                _-'_____`-_
              _-'________`-_
            _-'____________`-_
          _-'________________`-_
        _-'____________________`-_
                |    |
                |    |
                |    |
                """,
            },
            "cave_path": {
                "name": "Rocky Cave Path",
                "description": "The narrow passage twists deeper into the mountain. Strange echoes bounce off the jagged walls, and something skitters in the darkness.",
                "exits": {"south": "start", "east": "cavern", "down": "underground_lake"},
                "items": [],
                "enemy": {"name": "Cave Bat Swarm", "health": 40, "damage": 15},
                "art": r"""
                    /\/\
                   / /\ \
                  / /  \ \
                 / /    \ \
                /_/      \_\
                """,
            },
            "cavern": {
                "name": "Ancient Cavern",
                "description": "A vast cavern opens before you, its ceiling lost in darkness. Strange carvings cover the walls, glowing faintly.",
                "exits": {"west": "cave_path", "north": "treasure_chamber"},
                "items": ["ancient key"],
                "puzzle": {
                    "question": "What has keys but can't open locks?",
                    "answer": "piano",
                    "hint": "It's a musical instrument",
                    "reward": "golden amulet"
                }
            }
        }

    def clear_screen(self):
        """Clear the console screen"""
        print("\033[H\033[J", end="")

    def typewriter(self, text, color="text", delay=0.03, end="\n"):
        """Print text with typewriter effect and color"""
        try:
            colored_text = self.colors[color] + text + Style.RESET_ALL
            for char in colored_text:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(delay)
            print(end, end="")
        except UnicodeEncodeError:
            # Fallback for characters that can't be displayed
            print(self.colors[color] + text.encode('ascii', 'replace').decode('ascii') + Style.RESET_ALL)

    def display_header(self, title):
        """Display a styled header"""
        self.clear_screen()
        border = "=" * (len(title) + 4)
        self.typewriter(f"/{border}\\", "header")
        self.typewriter(f"|  {title.upper()}  |", "header")
        self.typewriter(f"\\{border}/", "header")
        print()

    def show_status(self):
        """Display player status with health bar"""
        health_bar = "[" + "#" * (self.health // 5) + " " * (20 - (self.health // 5)) + "]"
        self.typewriter(f"{'Health:':<10} {health_bar} {self.health}%", "health")
        
        inv_text = ", ".join(self.inventory) if self.inventory else "Empty"
        self.typewriter(f"{'Inventory:':<10} {inv_text}", "item")
        print()

    def display_room(self):
        """Display the current room with art and description"""
        room = self.rooms[self.current_room]
        
        self.display_header(room["name"])
        
        if "art" in room:
            print(self.colors["text"] + room["art"] + Style.RESET_ALL)
        
        self.typewriter(room["description"], "text")
        print()
        
        # Show exits
        exits = ", ".join([f"[{exit}]" for exit in room["exits"].keys()])
        self.typewriter(f"Exits: {exits}", "exit")
        
        # Show items
        if room["items"]:
            items = ", ".join([f"<{item}>" for item in room["items"]])
            self.typewriter(f"Items here: {items}", "item")
        
        print("\n" + "-" * 50)

    def show_help(self):
        """Display help information"""
        self.display_header("Game Commands")
        commands = [
            ("go [direction]", "Move in a direction (north, south, east, west)"),
            ("get [item]", "Pick up an item"),
            ("use [item]", "Use an item from inventory"),
            ("inspect", "Examine your surroundings more closely"),
            ("inventory", "Check your inventory"),
            ("status", "Check your health and inventory"),
            ("help", "Show this help message"),
            ("quit", "Exit the game")
        ]
        
        for cmd, desc in commands:
            self.typewriter(f"{self.colors['command']}{cmd:<15}{Style.RESET_ALL}{desc}")

    def play(self):
        """Main game loop"""
        self.clear_screen()
        # Simplified title screen without Unicode characters
        self.typewriter("EPIC QUEST", "title")
        self.typewriter("=========", "title")
        self.typewriter("\nWelcome to EPIC QUEST!", "header")
        self.typewriter("A text adventure of danger, mystery, and treasure...\n", "text")
        
        input("Press Enter to begin your adventure...")
        
        while not self.game_over:
            self.display_room()
            self.show_status()
            
            action = input("\nWhat will you do? ").lower().strip()
            
            if not action:
                continue
                
            elif action == "help":
                self.show_help()
                input("\nPress Enter to continue...")
            
            elif action == "inventory":
                if not self.inventory:
                    self.typewriter("\nYour inventory is empty.", "warning")
                else:
                    self.typewriter("\nInventory Items:", "header")
                    for item in self.inventory:
                        self.typewriter(f"- {item}", "item")
                input("\nPress Enter to continue...")
            
            elif action == "status":
                self.show_status()
                input("\nPress Enter to continue...")
            
            elif action == "quit":
                self.typewriter("\nAre you sure you want to quit? (y/n) ", "warning")
                if input().lower() == "y":
                    self.typewriter("\nThanks for playing! Your adventure ends here...", "header")
                    self.game_over = True
            
            elif action.startswith("go "):
                direction = action[3:]
                room = self.rooms[self.current_room]
                
                if direction in room["exits"]:
                    self.current_room = room["exits"][direction]
                    self.typewriter(f"\nYou move {direction}.", "success")
                    time.sleep(1)
                else:
                    self.typewriter("\nYou can't go that way!", "warning")
                    time.sleep(1)
            
            elif action.startswith("get "):
                item = action[4:]
                room = self.rooms[self.current_room]
                
                if item in room["items"]:
                    self.inventory.append(item)
                    room["items"].remove(item)
                    self.typewriter(f"\nYou picked up the {item}.", "success")
                    time.sleep(1)
                else:
                    self.typewriter(f"\nThere is no {item} here.", "warning")
                    time.sleep(1)
            
            else:
                self.typewriter("\nI don't understand that command. Type 'help' for available commands.", "warning")
                time.sleep(1)

# Start the game
if __name__ == "__main__":
    try:
        game = AdventureGame()
        game.play()
    except KeyboardInterrupt:
        print("\n\nGame interrupted. Thanks for playing!")