# Simple CSV Filter Windows App

![csv filter github](https://github.com/TonnyG95/Simple-CSV-Filtering-App/assets/47572512/41a7d6a2-b8d3-49f7-90cb-c92146b5d46a)

[![Download](https://img.shields.io/badge/download-File-green.svg)](https://rendoms3.s3.eu-west-1.amazonaws.com/Simple+CSV+Filter.exe)


# Table of Contents

- [Introduction](#introduction)
  - [Why I Built This App](#why-i-built-this-app)
  - [Technology Used](#technology-used)
  - [Use Case for This App](#use-case-for-this-app)
- [Features](#features)
  - [Comprehensive Graphical User Interface (GUI)](#comprehensive-graphical-user-interface-gui)
  - [Streamlined Column Selection for Filtering](#streamlined-column-selection-for-filtering)
  - [Direct Value Input for Targeted Filtering](#direct-value-input-for-targeted-filtering)
  - [Messages](#messages)
- [Requirements](#requirements)
- [How to Run This App Locally in Your IDE](#how-to-run-this-app-locally-in-your-ide)
  - [Running the App in Visual Studio Code (VSCode)](#running-the-app-in-visual-studio-code-vscode)
- [About the Code](#about-the-code)


## Introduction 
The Simple CSV Filter is a Windows application designed to simplify the process of filtering CSV files based on specific column values. Users can effortlessly upload the original CSV file, select a desired column for filtering, input the value to filter by, and with a simple click of the 'Filter' button, the app will generate a new CSV file containing only the rows that match the specified criteria. For instance, if you wish to filter out all rows with the value '2' in the 'Age' column, simply enter '2' in the designated textbox, click the 'Filter' button, and you'll receive a new CSV file with just the relevant information.

### Why I Built This App

In the realm of music distribution, I frequently encountered the challenge of managing large CSV files. A pressing need arose for a straightforward method to filter these files by ISRC (International Standard Recording Code) to aggregate detailed information about sales and streams for each song. This necessity led to the initial creation of a simple Python script designed for filtering songs by ISRC. Realizing the potential utility this solution could offer to others, I decided to transform it into a user-friendly Windows Application. This application not only retains the original script's functionality but also introduces an intuitive feature that automatically identifies and lists all available columns from the uploaded CSV file, allowing users to easily select the specific field they wish to filter by.

### Technology Used

Constructed with the Python programming language, this app incorporates the use of Tkinter for the graphical user interface (GUI), and Pandas and Numpy for efficient data handling. While the aesthetics of the UI was not my primary focus, the application stands out for its simplicity and effectiveness. It's designed to do exactly what it's intended for, filtering data with precision—making it a practical tool for those who need to process CSV files without any hassle.

### Use Case for This App

The Simple CSV Filter app serves a broad spectrum of uses related to CSV file management. Whether it's filtering client music by ISRC, sorting through sales records, managing projects, or organizing team members based on specific criteria like country or experience, this simple app offers a versatile solution. I chose to make this tool publicly available, believing in its wide applicability and ease of use. What makes it even more appealing is its no-installation requirement; it's a straightforward run-and-done application, accessible to everyone. Moreover, for Linux and macOS users, this app can be run in any IDE with Python installed, following the installation of required dependencies.

## Features

The Simple CSV Filter app, while modest in its design, is power-packed with features tailored to streamline the CSV filtering process. It's designed with a focus on functionality, ensuring that users can easily upload, filter, and save CSV files with minimal effort. Here's a closer look at its key features:

### Comprehensive Graphical User Interface (GUI)

The GUI of this Simple app is designed with the user's ease and efficiency in mind. While it might not feature the latest design trends, its strength lies in its straightforwardness and functionality, ensuring users can focus on their task without unnecessary complexity:

![csv filter github](https://github.com/TonnyG95/Simple-CSV-Filtering-App/assets/47572512/41a7d6a2-b8d3-49f7-90cb-c92146b5d46a)


### Streamlined Column Selection for Filtering

A hallmark of the Simple CSV Filter app is its intuitively designed feature that allows users to effortlessly select which column they wish to apply the filter to. This capability stands out as one of the app's most valuable functionalities, streamlining the data filtering process:

![image](https://github.com/TonnyG95/Simple-CSV-Filtering-App/assets/47572512/e6f7cb23-5050-4a3c-a55a-41f7703e5d13)

### Direct Value Input for Targeted Filtering

The Simple CSV Filter app provides a straightforward option for users to input the specific value they wish to use as a filter for the CSV file. This direct method of specifying a filter criterion is integral to the app's design, enabling precise data extraction based on user-defined conditions:

User-Defined Filter Values: Through a simple input field, users can enter the exact value they are looking for within a specified column. This value becomes the basis for filtering the CSV file, ensuring that the output file contains only the rows that match the specified criteria.

![image](https://github.com/TonnyG95/Simple-CSV-Filtering-App/assets/47572512/ba812baa-5c1e-4f91-a0c4-d914cf58f15b)

### Messages

Effective communication within an application enhances user experience by keeping them informed about the app's status and any actions required. The Simple CSV Filter app incorporates messaging in various scenarios to ensure users are well-informed throughout their interaction with the tool:

Operational Feedback: The app provides immediate feedback upon the successful export of a new CSV file, affirming that the user's data has been processed and saved as intended.

Error Handling: In the event of an error, such as a missing CSV file or other critical information, the app displays clear error messages. These alerts guide users to resolve the issue, ensuring that the app's functionality is not hindered by preventable mistakes.

Preventative Measures: Before initiating any operation, the app checks for the necessary conditions to be met (e.g., a CSV file must be uploaded). If any prerequisite is missing, the app informs the user of the specific action needed to proceed, preventing errors before they occur.

**Error Message**

![image](https://github.com/TonnyG95/Simple-CSV-Filtering-App/assets/47572512/2bfd8295-7df0-43c3-b579-c6b46019f5ba)

**Filtration Completed**

![alt text](image.png)

## Requirements
The Simple CSV Filter app is developed in Python and utilizes several essential packages to manage and process CSV files efficiently. Below is a list of required Python packages along with their specified versions to ensure the app runs smoothly:

- numpy==1.26.4
- pandas==2.2.1
- python-dateutil==2.8.2
- pytz==2024.1
- six==1.16.0
- tzdata==2024.1

## How to Run This App Locally in Your IDE

You can download this repo or you can clone it and open it in your IDE of choice. Before you try to run this app make sure that you have installed Python on your machine. To download Python visit this [Link](https://www.python.org/downloads/) after installed Python you can start installing requirements using commands below 

**Windows Users**

```
cd path/to/source-code
pip install -r requirements.txt
python main.py 

```
**Linux and macOS Users**

```
cd path/to/source-code
pip install -r requirements.txt
python3 main.py 

```

### Running the App in Visual Studio Code (VSCode)
If you are using VSCode, you can just right-click on the folder and select "Open with Code." you can run it from the terminal using the command below. In VSCode, in the top navigation bar (where you have File, Edit, etc.), you can click on the terminal and then "New Terminal." Or, when you open main.py in VSCode, on the tab where the file name main.py is displayed, you will have a play button. When you click that, the app will run.

## About the Code
When I was writing this code, I paid attention to code quality and tried to make it as readable as possible. I added a lot of comments to make it more understandable and tried to use variable names that are meaningful to make it more understandable for everyone. So, if anyone wants to jump into the code and make some changes, feel free to do so and make this app better. Like I said, I created this app to help me solve my problems with large CSV files, and I hope that this app will help anyone dealing with large datasets. For me, this worked perfectly.

## Download Link

[![Download](https://img.shields.io/badge/download-File-green.svg)](https://rendoms3.s3.eu-west-1.amazonaws.com/Simple+CSV+Filter.exe)
