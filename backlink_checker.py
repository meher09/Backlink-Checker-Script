import pandas as pd
import aiohttp
import asyncio
from datetime import datetime

mysite = "thekitchn.com"  # Replace with your site URL
csv_file = 'mybacklink.csv'  # CSV file path

# Define the headers to avoid blocks
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3', 
    'Accept-Language': 'en-US,en;q=0.9',
    'Referer': 'https://www.google.com/',  # Simulate coming from Google
    'Connection': 'keep-alive'
}

async def check_backlink_status(url, domain, session):
    try:
        async with session.get(url, headers=HEADERS, timeout=10) as response:
            if response.status == 200:
                content = await response.text()
                if domain in content:
                    return "Present"
                else:
                    return "Absent"
            else:
                return "Absent"
    except asyncio.TimeoutError:
        return "Timeout"
    except Exception:
        return "Unable to Fetch"

async def check_backlinks(df, domain):
    async with aiohttp.ClientSession() as session:
        tasks = []
        for url in df['backlink_url']:
            task = check_backlink_status(url, domain, session)
            tasks.append(task)
        
        return await asyncio.gather(*tasks)

def update_csv_with_results(csv_file, domain):
    df = pd.read_csv(csv_file)
    current_date = datetime.now().strftime('%Y-%m-%d')  # Get current date as column name
    
    loop = asyncio.get_event_loop()
    results = loop.run_until_complete(check_backlinks(df, domain))
    
    df[current_date] = results
    df.to_csv(csv_file, index=False)
    print(f"Backlink check complete. Results saved in '{csv_file}'.")

# Run the backlink check
update_csv_with_results(csv_file, mysite)
