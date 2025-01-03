# CricXpress - Real-Time Cricket Information Platform

CricXpress is a comprehensive cricket information platform built with Django that provides real-time cricket scores, player statistics, team information, and more using the Cricbuzz API.

## Features

### Live Cricket Information
- **Live Matches**: Real-time updates of ongoing cricket matches
- **Recent Matches**: Results and statistics of recently concluded matches
- **Upcoming Matches**: Schedule of upcoming cricket fixtures
- **Match Details**: Detailed match information including:
  - Ball-by-ball commentary
  - Full scorecard
  - Match facts and playing conditions

### Player Information
- **Player Profiles**: Detailed statistics and information about cricket players
- **Player Search**: Search functionality to find players
- **Career Statistics**: Comprehensive batting and bowling statistics

### Team Information
- **Teams List**: List of all cricket teams
- **player List**: List of players in a team
- **Team Schedule**: Upcoming matches and recent results

### Series


### News Section
- **News**: Latest cricket news and updates
- **News Details**: In-depth coverage of cricket stories

## Screenshots

### Homepage
![Homepage View 1](https://github.com/Himanshusingh-18/CricXpress/blob/main/Morax/screenshots/homepage1.png)
![Homepage View 2](https://github.com/Himanshusingh-18/CricXpress/blob/main/Morax/screenshots/homepage2.png)

### Live Matches & Scores
![Live Matches](https://github.com/Himanshusingh-18/CricXpress/blob/main/Morax/screenshots/live_matches.png)
![Match Scorecard](https://github.com/Himanshusingh-18/CricXpress/blob/main/Morax/screenshots/scorecard.png)
![Live Commentary](https://github.com/Himanshusingh-18/CricXpress/blob/main/Morax/screenshots/commentary.png)

### Schedule
![Match Schedule](https://github.com/Himanshusingh-18/CricXpress/blob/main/Morax/screenshots/schedule.png)
![Upcoming Matches](https://github.com/Himanshusingh-18/CricXpress/blob/main/Morax/screenshots/upcoming_matches.png)
![Recent Matches](https://github.com/Himanshusingh-18/CricXpress/blob/main/Morax/screenshots/recent_matches.png)

### News
![Cricket News](https://github.com/Himanshusingh-18/CricXpress/blob/main/Morax/screenshots/news.png)
![News Details](https://github.com/Himanshusingh-18/CricXpress/blob/main/Morax/screenshots/news_details.png)

### Players
![Players List](https://github.com/Himanshusingh-18/CricXpress/blob/main/Morax/screenshots/players.png)
![Player Information](https://github.com/Himanshusingh-18/CricXpress/blob/main/Morax/screenshots/player_info.png)

### Teams
![Teams List](https://github.com/Himanshusingh-18/CricXpress/blob/main/Morax/screenshots/teams.png)
![Squad List](https://github.com/Himanshusingh-18/CricXpress/blob/main/Morax/screenshots/squad_list.png)
![Detailed Squad](https://github.com/Himanshusingh-18/CricXpress/blob/main/Morax/screenshots/squad_list1.png)

### Series
![Series List](https://github.com/Himanshusingh-18/CricXpress/blob/main/Morax/screenshots/serieslist.png)
![Series Matches](https://github.com/Himanshusingh-18/CricXpress/blob/main/Morax/screenshots/matches_list.png)

## Technical Details

### Built With
- **Backend**: Django 4.2
- **Frontend**: HTML5, CSS3, JavaScript
- **API**: Cricbuzz Cricket API (from RapidAPI)
- **Database**: SQLite3
- **Authentication**: Django Authentication System

### Prerequisites
- Python 3.8+
- Django 4.2+
- Requests library
- RapidAPI Account and Cricbuzz API subscription

### Installation

1. Clone the repository
```bash
git clone https://github.com/yourusername/CricXpress.git
```

2. Create a virtual environment and activate it
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install required packages
```bash
pip install -r requirements.txt
```

4. Set up environment variables
```bash
# Add these to your settings.py or environment
RAPIDAPI_KEY=your_api_key_here  # Get this from RapidAPI
RAPIDAPI_HOST=cricbuzz-cricket.p.rapidapi.com
```

5. Run migrations
```bash
python manage.py migrate
```

6. Start the development server
```bash
python manage.py runserver
```

## API Integration

The project uses the [Cricbuzz Cricket API](https://rapidapi.com/cricketapilive/api/cricbuzz-cricket) from RapidAPI to fetch real-time data. The API provides:
- Live match scores and commentary
- Player and team statistics
- Cricket news and updates
- Series and tournament information

To use this project, you'll need to:
1. Sign up for a RapidAPI account
2. Subscribe to the Cricbuzz Cricket API
3. Get your API key from RapidAPI
4. Add the API key to your project settings

## Project Structure

```
CricXpress/
├── cricket/                 # Main application directory
│   ├── templates/          # HTML templates
│   │   ├── matches/       # Match-related templates
│   │   ├── players/       # Player-related templates
│   │   ├── teams/         # Team-related templates
│   │   └── series/        # Series-related templates
│   ├── static/            # Static files (CSS, JS, images)
│   ├── views.py           # View functions
│   ├── urls.py            # URL configurations
│   └── models.py          # Database models
├── static/                # Global static files
├── templates/            # Global templates
├── manage.py             # Django management script
└── requirements.txt      # Project dependencies
```


## Acknowledgments

- Cricbuzz API from RapidAPI for providing cricket data
- Django community for the excellent web framework

## Contact Me

Feel free to reach out if you have any questions or suggestions!

- **Email**: hs18173215@gmail.com
- **Telegram**: [Himanshu singh](https://t.me/flame_1817)
- **GitHub**: [Himanshu singh](https://github.com/Himanshusingh-18)
- **LinkedIn**: [Himanshu singh](https://www.linkedin.com/in/himanshu-singh-701343222)
