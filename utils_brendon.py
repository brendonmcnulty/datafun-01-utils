"""
utils_brendon.py

Author: Brendon McNulty


This file is your personalized utilities module for the Data Analytics Fundamentals class.
It demonstrates using the statistics standard library, loguru for logging, 
and pyttsx3 for text-to-speech output.
"""

import statistics
from loguru import logger
import pyttsx3


def main():
    """Run a simple example of statistics, logging, and text-to-speech."""

    
    logger.info("Brendon’s main function has started — ready to crunch some numbers!")


    # Example statistics
   
    data = [5, 7, 12, 18, 23, 42]

    # Calculate mean and stdev
    mean = statistics.mean(data)
    stdev = statistics.stdev(data)

    
    logger.info(f"Crunching numbers: average = {mean:.2f}, spread = {stdev:.2f} — nice work, Brendon!")


    # Example voice output
    
    engine = pyttsx3.init()
    engine.say("Brendon is ready to conquer Data Analytics Fundamentals!")

    engine.runAndWait()


# Standard Python idiom for making code run only when executed directly.

if __name__ == "__main__":
    main()


