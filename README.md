# Planet Alignment Calculator

This Python program calculates when planets in our solar system will be aligned. It uses astronomical calculations to determine the positions of planets and identify when they form specific alignments.

## Features

- Calculates planetary positions using astronomical formulas
- Determines when planets are in alignment (within a specified angular threshold)
- Supports calculations for Mercury, Venus, Earth, Mars, Jupiter, and Saturn
- Provides results with dates and angular positions

## How It Works

The program uses these key concepts:

1. **Orbital Elements**: Uses each planet's orbital parameters (semi-major axis, eccentricity, etc.)
2. **Position Calculation**: Converts orbital elements to heliocentric coordinates
3. **Alignment Detection**: Checks angular separation between planets
4. **Time Iteration**: Steps through time to find alignment events

## Usage

1. Run the program:
```python
python planet_alignment_calculator.py
```

2. The program will output dates when planets are aligned, along with their angular positions.

## Requirements

- Python 3.x
- math module (built-in)
- datetime module (built-in)

## Example Output

```
Checking alignments from 2024-01-01 to 2024-12-31
Found alignment on 2024-XX-XX:
- Mercury: XX degrees
- Venus: XX degrees
- Mars: XX degrees
```

## Contributing

Feel free to contribute to this project by:
1. Forking the repository
2. Creating a new branch (`git checkout -b feature/improvement`)
3. Making your changes
4. Committing (`git commit -m "Add new feature"`)
5. Pushing (`git push origin feature/improvement`)
6. Creating a Pull Request

## License

This project is open source and available under the MIT License.
