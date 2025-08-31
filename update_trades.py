#!/usr/bin/env python3
"""
NBA Trades Data Updater
This script helps update the trades.md file with NBA player movements data.
"""

import requests
from bs4 import BeautifulSoup
import re
import sys

def scrape_nba_trades():
    """
    Scrape NBA trades data from Wikipedia
    """
    url = "https://en.wikipedia.org/wiki/List_of_2025%E2%80%9326_NBA_season_transactions"

    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find the trades section (this might need adjustment based on Wikipedia structure)
        trades_data = []

        # Look for tables containing player transactions
        tables = soup.find_all('table', class_=re.compile(r'wikitable'))

        for table in tables:
            rows = table.find_all('tr')
            for row in rows:
                cells = row.find_all(['td', 'th'])
                if len(cells) >= 3:
                    # Extract player, from team, to team
                    cell_texts = [cell.get_text().strip() for cell in cells]
                    if len(cell_texts) >= 3:
                        player = cell_texts[0]
                        from_team = cell_texts[1] if len(cell_texts) > 1 else ""
                        to_team = cell_texts[2] if len(cell_texts) > 2 else ""

                        # Basic filtering - adjust as needed
                        if player and from_team and to_team and from_team != to_team:
                            trades_data.append({
                                'player': player,
                                'from_team': from_team,
                                'to_team': to_team
                            })

        return trades_data

    except Exception as e:
        print(f"Error scraping data: {e}")
        return []

def generate_markdown_table(trades_data):
    """
    Generate markdown table from trades data
    """
    if not trades_data:
        return "# NBA Player Movements - Summer 2025\n\nNo trades data available yet."

    # Group trades by player to handle multiple moves
    player_movements = {}

    for trade in trades_data:
        player = trade['player']
        if player not in player_movements:
            player_movements[player] = {
                'start_team': trade['from_team'],
                'end_team': trade['to_team'],
                'moves': [trade]
            }
        else:
            # Update end team for multiple moves
            player_movements[player]['end_team'] = trade['to_team']
            player_movements[player]['moves'].append(trade)

    # Generate markdown
    markdown = "# NBA Player Movements - Summer 2025\n\n"
    markdown += "| Player Name | From Team | To Team |\n"
    markdown += "|-------------|-----------|---------|\n"

    for player, data in player_movements.items():
        if data['start_team'] != data['end_team']:  # Only include if teams are different
            markdown += f"| {player} | {data['start_team']} | {data['end_team']} |\n"

    return markdown

def main():
    print("🔄 Scraping NBA trades data...")
    trades_data = scrape_nba_trades()

    if trades_data:
        print(f"✅ Found {len(trades_data)} trade entries")
        markdown_content = generate_markdown_table(trades_data)

        # Write to trades.md
        with open('trades.md', 'w', encoding='utf-8') as f:
            f.write(markdown_content)

        print("✅ Updated trades.md with latest data")
    else:
        print("❌ No trades data found. Check the Wikipedia page structure.")

if __name__ == "__main__":
    main()
