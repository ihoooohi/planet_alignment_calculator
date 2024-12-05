# Planet Alignment Calculator

This Python program calculates when planets in our solar system will be aligned. It uses astronomical calculations to determine the positions of planets and identify when they form specific alignments.

**This code is developed as a solution to Question 8 of the Survey for Master of Science (AI for Science) program.**

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