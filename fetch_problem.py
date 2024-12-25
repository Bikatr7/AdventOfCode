from aocd.models import Puzzle
import os
from bs4 import BeautifulSoup

def get_soup(html_content):
    return BeautifulSoup(html_content, 'html.parser')

def fetch_problem(day):
    try:
        puzzle = Puzzle(year=2024, day=day)
        
        dir_path = f"solutions/{puzzle.year}/{day}"
        if(not os.path.exists(dir_path)):
            os.makedirs(dir_path)
        
        md_path = f"{dir_path}/{day}.md"
        with open(md_path, "w", encoding='utf-8') as f:
            prose = puzzle._get_prose()
            soup = get_soup(prose)
            articles = soup.find_all('article', class_='day-desc')
            
            f.write(f"--- Day {day}: {puzzle.title} ---\n\n")
            f.write(articles[0].get_text())
            if(len(articles) > 1):
                f.write("\n\n-- Part Two ---\n\n")
                f.write(articles[1].get_text())
        
        txt_path = f"{dir_path}/{day}.txt"
        with open(txt_path, "w", encoding='utf-8') as f:
            f.write(puzzle.input_data)
        
        print(f"Successfully fetched problem and input for day {day}")
        return True
        
    except Exception as e:
        print(f"Error fetching problem for day {day}: {str(e)}")
        return False

if(__name__ == "__main__"):
    import sys
    if(len(sys.argv) > 1):
        day = int(sys.argv[1])
        if(not fetch_problem(day)):
            print(f"Failed to fetch problem for day {day}")
    else:
        print("Please provide a day number") 