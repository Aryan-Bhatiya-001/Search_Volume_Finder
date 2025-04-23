# Search Volume Finder

A Python tool that estimates search volume for queries by combining Google search result counts with trend data.

## Description

This tool uses browser automation to:
1. Collect the total number of search results from Google for a given query
2. Gather trend data for the query from Google Trends
3. Calculate an estimated search volume based on this information

## Installation

### Prerequisites
- Python 3.10+
- pip
- C++ Build Tools (for Windows users)

### Setup

1. **Create a virtual environment**
   ```bash
   python -m venv venv
   ```

2. **Activate the virtual environment**
   
   On Windows:
   ```bash
   venv\Scripts\activate
   ```
   
   On macOS/Linux:
   ```bash
   source venv/bin/activate
   ```

3. **Install C++ Build Tools (Windows only)**
   
   Before installing the requirements, Windows users need to install C++ build tools to avoid errors with packages like `faust-cchardet`:
   
   **Option 1: Visual Studio Build Tools**
   - Download and install [Visual Studio Build Tools](https://visualstudio.microsoft.com/visual-cpp-build-tools/)
   - During installation, select "C++ build tools" workload
   - Make sure the following components are selected:
     - MSVC C++ build tools
     - Windows 10/11 SDK
   
   **Option 2: Using pip to install pre-built wheels**
   ```bash
   pip install --upgrade pip
   pip install wheel
   ```
   
   After installing build tools, restart your command prompt before continuing.

4. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

5. **Set up Crawl4AI**
   ```bash
   crawl4ai-setup
   ```

## Usage

Run the main script:
```bash
python src/main.py
```

You will be prompted to enter a search query. The program will then:
- Crawl Google search results to get the total result count
- Collect trend data from Google Trends
- Calculate and display the estimated search volume

## How It Works

The application uses:
- `playwright` for browser automation
- `crawl4ai` for web scraping
- Asynchronous processing to concurrently collect data from multiple sources

The search volume is calculated using the formula:
```
search_volume = (latest_trend_value / sum_of_trend_values) * total_search_results
```
