🎥 Video Length Calculator
This Python project provides a simple yet powerful tool to calculate the total duration of all video files within a selected folder. It's built using MoviePy and Tkinter, making it both functional and user-friendly.

📋 Features
🗂️ Folder Selection: Select any folder containing video files via an intuitive GUI.
⏳ Total Duration Calculation: Computes the total length of .mp4 videos in the folder.
⏰ Time Conversion: Displays the total duration in a human-readable format (hours, minutes, seconds).
🛠️ Extensible: Easily add support for more video file extensions.
🖥️ Requirements
Python 3.7+
Installed Python libraries:
moviepy
tkinter
📦 Installation
Clone the repository:
bash
Copy code
git clone https://github.com/schourasia750/just_private_repository.git
cd just_private_repository
Install the required dependencies:
bash
Copy code
pip install moviepy
🚀 Usage
Run the script:
bash
Copy code
python video_length_calculator.py
Use the "Select Folder" button to choose the directory containing your videos.
View the total video length in hours, minutes, and seconds in a pop-up window.
🛠️ How It Works
Folder Walkthrough: The script traverses through the selected folder and identifies .mp4 files.
Video Analysis: Each video’s duration is calculated using moviepy.editor.
Time Aggregation: Total time is converted to a readable format (HH:MM:SS) and displayed in a message box.
📌 Example
Input:
A folder containing the following videos:

video1.mp4 (2m 15s)
video2.mp4 (1h 10m 30s)
Output:
plaintext
Copy code
Total video length: 1h 12m 45s
🖼️ User Interface
Simple GUI built using Tkinter:
A single button to select the folder.
Automatically calculates and displays the result.
🤝 Contribution
Contributions are welcome! Follow these steps:

Fork the repository.
Create a new branch (feature-branch).
Submit a pull request.
📜 License
This project is licensed under the MIT License. See the LICENSE file for details.

📧 Contact
For questions or feedback, reach out to:

GitHub: @schourasia750
