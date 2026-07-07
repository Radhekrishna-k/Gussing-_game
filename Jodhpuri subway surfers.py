"""
Jodhpuri Subway Surfers - An endless runner game
A fun game inspired by Subway Surfers set in Jodhpur!
"""

import random
import time


class Player:
    """Represents the player in the game."""
    
    def __init__(self):
        self.position = 1  # 0: left, 1: center, 2: right
        self.score = 0
        self.lives = 3
        self.is_alive = True
    
    def move_left(self):
        """Move player to the left lane."""
        if self.position > 0:
            self.position -= 1
    
    def move_right(self):
        """Move player to the right lane."""
        if self.position < 2:
            self.position += 1
    
    def get_hit(self):
        """Player gets hit by an obstacle."""
        self.lives -= 1
        if self.lives <= 0:
            self.is_alive = False
    
    def add_score(self, points):
        """Add points to the score."""
        self.score += points


class Obstacle:
    """Represents an obstacle on the track."""
    
    def __init__(self, position):
        self.position = position
        self.y = 0
    
    def move_down(self):
        """Move obstacle down the screen."""
        self.y += 1


class Game:
    """Main game controller."""
    
    def __init__(self):
        self.player = Player()
        self.obstacles = []
        self.running = True
        self.level = 1
        self.spawn_rate = 0.3  # Probability of spawning obstacle
    
    def spawn_obstacle(self):
        """Randomly spawn obstacles in different lanes."""
        if random.random() < self.spawn_rate:
            lane = random.randint(0, 2)
            self.obstacles.append(Obstacle(lane))
    
    def update(self):
        """Update game state."""
        self.spawn_obstacle()
        
        # Move all obstacles down
        for obstacle in self.obstacles:
            obstacle.move_down()
        
        # Check collisions
        for obstacle in self.obstacles[:]:
            if obstacle.position == self.player.position and obstacle.y > 10:
                self.player.get_hit()
                self.obstacles.remove(obstacle)
            elif obstacle.y > 15:
                self.obstacles.remove(obstacle)
                self.player.add_score(10)
        
        # Increase difficulty
        if self.player.score % 100 == 0 and self.player.score > 0:
            self.level += 1
            self.spawn_rate += 0.05
        
        if not self.player.is_alive:
            self.running = False
    
    def draw(self):
        """Display the game state."""
        print("\n" * 2)
        print("=" * 30)
        print(f"🎮 JODHPURI SUBWAY SURFERS")
        print(f"Score: {self.player.score} | Lives: {self.player.lives} | Level: {self.level}")
        print("=" * 30)
        
        # Draw track
        for y in range(15):
            line = ""
            for x in range(3):
                if x == 1:
                    line += "|"
                
                # Draw player
                if y == 12 and x == self.player.position:
                    line += "🚂"
                # Draw obstacles
                elif any(obs.position == x and obs.y == y for obs in self.obstacles):
                    line += "⚠️ "
                else:
                    line += "  "
            print(line)
        
        print("=" * 30)
        print("Use A/D or ← → to move | Q to quit")
    
    def handle_input(self):
        """Handle player input."""
        # For console, we'll simulate input
        try:
            user_input = input("Move (a/d or q to quit): ").lower().strip()
            if user_input == 'a':
                self.player.move_left()
            elif user_input == 'd':
                self.player.move_right()
            elif user_input == 'q':
                self.running = False
        except:
            pass
    
    def play(self):
        """Main game loop."""
        print("\n🎉 Welcome to Jodhpuri Subway Surfers!")
        print("Dodge obstacles and survive as long as you can!\n")
        time.sleep(2)
        
        while self.running:
            self.draw()
            self.handle_input()
            self.update()
            time.sleep(0.5)
        
        self.show_game_over()
    
    def show_game_over(self):
        """Display game over screen."""
        print("\n" + "=" * 30)
        print("💀 GAME OVER!")
        print(f"Final Score: {self.player.score}")
        print(f"Level Reached: {self.level}")
        print("=" * 30)


def main():
    """Run the game."""
    while True:
        game = Game()
        game.play()
        
        play_again = input("\nPlay again? (yes/no): ").lower().strip()
        if play_again not in ['yes', 'y']:
            print("Thanks for playing! 👋")
            break


if __name__ == "__main__":
    main()
