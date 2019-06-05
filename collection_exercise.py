def publ_dates(title, date):
    print(title + " was published in " + date + ".")

texts = {"Jane Eyre":"1847", "Cane":"1923", "Wide Sargasso Sea":"1966", "Citizen:An American Lyric":"2014"}

for title, date in texts.items():
    publ_dates(title, date)
    
