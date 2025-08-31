"""
utils_brendon.py

This file is your personalized utilities module for the Data Analytics Fundamentals class.
It demonstrates using the statistics standard library, loguru for logging, 
and pyttsx3 for text-to-speech output.
"""

import statistics
from loguru import logger
import pyttsx3


def main():
    """Run a simple example of statistics, logging, and text-to-speech."""
    logger.info("Starting main function")

    # Example statistics
    data = [2.75, 1.75, 1.25, 0.25, 0.5, 1.25, 3.5]
    mean = statistics.mean(data)
    stdev = statistics.stdev(data)
    logger.info(f"Mean: {mean}, Standard Deviation: {stdev}")

    # Example voice output
    engine = pyttsx3.init()
    engine.say("Hello from utils_brendon!")
    engine.runAndWait()


if __name__ == "__main__":
    main()

