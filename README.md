# NBA Player Movements - Summer 2025

A comprehensive tracker of all NBA player transactions and team movements for the 2025-26 season.

## 📊 Features

- Complete list of player movements during the 2025 NBA offseason
- Clean, responsive web interface
- Data sourced from Wikipedia's NBA transactions page
- Automatic updates and tracking of player journeys

## 🚀 Live Site

View the live site at: [Your GitHub Pages URL]

## 📋 Data Source

All data is sourced from: [Wikipedia - List of 2025–26 NBA season transactions](https://en.wikipedia.org/wiki/List_of_2025%E2%80%9326_NBA_season_transactions)

## 🏗️ How It Works

1. Player movements are tracked from the start of the summer to their final destination
2. If a player changes teams multiple times, only the initial team and final team are shown
3. Players who end up on the same team they started with are excluded from the list
4. Data is presented in a clean, sortable table format

## 📝 Data Format

The trades data is stored in `trades.md` using Markdown table format:

```markdown
| Player Name | From Team | To Team |
|-------------|-----------|---------|
| Player A    | Team 1    | Team 3  |
```

## 🔧 Local Development

To run this site locally:

1. Clone the repository
2. Open `index.html` in your browser
3. Update `trades.md` with the latest NBA transactions

## 🤝 Contributing

To update the trades data:

1. Visit the Wikipedia page for NBA transactions
2. Extract player movements following the format above
3. Update `trades.md` with the new data
4. Commit and push your changes

## 📄 License

This project is open source and available under the MIT License.
