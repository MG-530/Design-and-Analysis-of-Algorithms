def tower_of_hanoi(n: int, source: str, auxiliary: str, destination: str, moves: list) -> None:
    if n == 1:
        moves.append(f"Move disk from rod {source} to rod {destination}")
        return
    
    # Move n-1 disks from source to auxiliary
    tower_of_hanoi(n-1, source, destination, auxiliary, moves)
    
    # Move nth disk from source to destination
    moves.append(f"Move disk from rod {source} to rod {destination}")
    
    # Move n-1 disks from auxiliary to destination
    tower_of_hanoi(n-1, auxiliary, source, destination, moves)

def main():
    # Read input
    with open('input.txt', 'r') as f:
        n = int(f.read().strip())
    
    # Solve Tower of Hanoi
    moves = []
    tower_of_hanoi(n, 'A', 'B', 'C', moves)
    
    # Write output
    with open('output.txt', 'w') as f:
        for move in moves:
            f.write(move + '\n')
        f.write(f"Total moves: {len(moves)}")

if __name__ == "__main__":
    main() 