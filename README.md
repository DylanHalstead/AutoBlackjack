# 🃏 AutoBlackjack
AutoBlackjack is a computer vision application designed to assist users in making informed decisions in the game of Blackjack. Using machine learning techniques and computer vision, AutoBlackjack helps identify the best possible move to make with any hand of Blackjack. *This project was built for Marco Scipioni's Computer Vision with Python (DTSC 3000) course at UNC Charlotte*

https://github.com/DylanHalstead/AutoBlackjack/assets/70990184/8719e4da-a6ef-494f-ad67-76f15d3e805e


## 🤔 What Does it Do
AutoBlackjack captures video from a specified source (e.g., webcam) utilizing OpenCV and processes each frame through YOLOv8 (via the ultralytics package). Utilizing the [Augmented Startups playing cards dataset](https://universe.roboflow.com/augmented-startups/playing-cards-ow27d), YOLOv8 detects playing cards and their respective value/suit. By analyzing the recognized cards and their positions, we determine how many hands are shown, which card is the dealer, and the best action for the player according to standard Blackjack strategies.

https://github.com/DylanHalstead/AutoBlackjack/assets/70990184/c7952118-c263-41c6-82dc-f27b1da0d7eb

## 🚀 Running
To get started, make sure to have Python 3.10+ installed on your machine (used 3.11 in development). Then, create a virtual environment and install through the requirements.txt file with `pip install -r requirements.txt`. Once installed, run the application with `python main.py`.

Note: Press 'q' to exit the application.
