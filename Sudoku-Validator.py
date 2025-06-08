def is_valid_sudoku(board, custom_zones):
    def is_valid_group(values):
        digits = [v for v in values if v != '.']
        return len(digits) == len(set(digits))

    # Validate rows and columns
    for i in range(9):
        row = board[i]
        column = [board[r][i] for r in range(9)]
        if not is_valid_group(row):
            print(f"Invalid row {i}: {row}")
            return False
        if not is_valid_group(column):
            print(f"Invalid column {i}: {column}")
            return False

    # Validate 3x3 boxes
    for row in range(0, 9, 3):
        for col in range(0, 9, 3):
            box = [board[r][c] for r in range(row, row + 3) for c in range(col, col + 3)]
            if not is_valid_group(box):
                print(f"Invalid 3x3 box at ({row},{col}): {box}")
                return False

    # Validate custom zones
    for i, zone in enumerate(custom_zones):
        zone_values = [board[r][c] for r, c in zone]
        if not is_valid_group(zone_values):
            print(f"Invalid custom zone {i}: {zone_values}")
            return False

    return True


#  Example board (can have empty cells represented by '.')
board = [
    ['5', '3', '4', '6', '7', '8', '9', '1', '2'],
    ['6', '7', '2', '1', '9', '5', '3', '4', '8'],
    ['1', '9', '8', '3', '4', '2', '5', '6', '7'],
    ['8', '5', '9', '7', '6', '1', '4', '2', '3'],
    ['4', '2', '6', '8', '5', '3', '7', '9', '1'],
    ['7', '1', '3', '9', '2', '4', '8', '5', '6'],
    ['9', '6', '1', '5', '3', '7', '2', '8', '4'],
    ['2', '8', '7', '4', '1', '9', '6', '3', '5'],
    ['3', '4', '5', '2', '8', '6', '1', '7', '9'],
]
# Example of custom zones (simulating 3x3 blocks)
custom_zones = [
    [(0,0), (0,1), (0,2), (1,0), (1,1), (1,2), (2,0), (2,1), (2,2)],  
    [(0,3), (0,4), (0,5), (1,3), (1,4), (1,5), (2,3), (2,4), (2,5)],
    [(0,6), (0,7), (0,8), (1,6), (1,7), (1,8), (2,6), (2,7), (2,8)],
    [(3,0), (3,1), (3,2), (4,0), (4,1), (4,2), (5,0), (5,1), (5,2)],
    [(3,3), (3,4), (3,5), (4,3), (4,4), (4,5), (5,3), (5,4), (5,5)],
    [(3,6), (3,7), (3,8), (4,6), (4,7), (4,8), (5,6), (5,7), (5,8)],
    [(6,0), (6,1), (6,2), (7,0), (7,1), (7,2), (8,0), (8,1), (8,2)],    
    [(6,3), (6,4), (6,5), (7,3), (7,4), (7,5), (8,3), (8,4), (8,5)],  
    [(6,6), (6,7), (6,8), (7,6), (7,7), (7,8), (8,6), (8,7), (8,8)], 
    ]

# Run the validator
is_valid = is_valid_sudoku(board, custom_zones)
print("Sudoku is valid." if is_valid else "Sudoku is invalid.")
