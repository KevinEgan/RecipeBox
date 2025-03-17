# Recipe Box

A simple web app for storing and sharing your favorite recipes. Built with Flask and Vue.js.

## Getting Started

### Backend Setup

From the `backend` directory:

1. Set up your Python environment:
```bash
# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

2. Start the Flask server:
```bash
python app.py
```

The API will be running at `http://localhost:5000`

### Frontend Setup

From the `frontend` directory:

1. Install dependencies:
```bash
npm install
```

2. Start the development server:
```bash
npm run serve
```

Follow link in terminal, `http://localhost:8080` to start using Recipe Box

## What's Inside

- Add your favorite recipes with ingredients and instructions
- View all recipes in a clean, organized layout
- Simple, responsive design that works on mobile

## Tech Stack

- **Backend**: Flask + SQLite for a lightweight, easy-to-use database
- **Frontend**: Vue.js 3 for a smooth, modern user experience

## Want to Help?

Feel free to:
- Open an issue if you find a bug
- Submit a pull request if you've made an improvement
- Fork it to create your own version

## Next Steps

Some features I'm thinking about:
- Recipe categories
- Search functionality
- User accounts
- Recipe reviews and comments
- Recipe difficulty vs time matrix

Happy Cooking! 