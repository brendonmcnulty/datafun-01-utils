"""
utils_brendon.py

TODO: Change the module name in the docstring at the top (done: utils_brendon.py).
TODO: Add your name as the author.

This file is your personalized utilities module for the Data Analytics Fundamentals class.
It demonstrates using the statistics standard library, loguru for logging, 
and pyttsx3 for text-to-speech output.
"""

# TODO: Review the imports. Do you understand what each one is used for?
import statistics
from loguru import logger
import pyttsx3


def main():
    """Run a simple example of statistics, logging, and text-to-speech."""

    # TODO: Update the logger message to include your name.
    logger.info("Starting main function for Brendon")

    # Example statistics
    # TODO: Replace this data with your own set of numbers.
    data = [2.75, 1.75, 1.25, 0.25, 0.5, 1.25, 3.5]

    # Calculate mean and stdev
    mean = statistics.mean(data)
    stdev = statistics.stdev(data)

    # TODO: Customize this message to make it yours.
    logger.info(f"Mean: {mean}, Standard Deviation: {stdev}")

    # Example voice output
    # TODO: Update the spoken message to make it unique to you.
    engine = pyttsx3.init()
    engine.say("Hello from utils_brendon!")
    engine.runAndWait()


# Standard Python idiom for making code run only when executed directly.
# TODO: Make sure you understand why this is important.
if __name__ == "__main__":
    main()


