from fastapi import FastAPI
import random

app = FastAPI()

sideHustles = [
    "Freelancing (Upwork, Fiverr, Toptal)",
    "Web Development (Freelance websites ya client projects)",
    "Mobile App Development (React Native, Flutter)",
    "WordPress Customization aur Plugin Development",
    "Selling Digital Products (Scripts, Templates, Themes)",
    "YouTube Channel (Coding Tutorials, Tech Reviews)",
    "Blogging (Technical Articles, Monetization)",
    "Creating and Selling Online Courses (Udemy, Gumroad)",
    "Building and Monetizing SaaS Applications",
    "Stock Market & Crypto Trading Bots Development"
]

moneyQuotes = [
    "Don’t work for money, make money work for you. – Robert Kiyosaki",
    "Rich people have small TVs and big libraries, poor people have small libraries and big TVs. – Zig Ziglar",
    "The secret to getting ahead is getting started. – Mark Twain",
    "Opportunities don’t happen, you create them. – Chris Grosser",
    "Formal education will make you a living; self-education will make you a fortune. – Jim Rohn",
    "If you don’t find a way to make money while you sleep, you will work until you die. – Warren Buffett",
    "Do what you love and the money will follow. – Marsha Sinetar",
    "Success is not in what you have, but who you are. – Bo Bennett",
    "A wise person should have money in their head, but not in their heart. – Jonathan Swift",
    "Money grows on the tree of persistence. – Japanese Proverb"
]

@app.get("/side-husstles")
def getSideHusstles(apiKey: str):
    if apiKey != "123456789":
        return{"error": "Invalid Api Key"}
    """ Return a Random Side Husstle Idea """
    return{"side-husstles": random.choice(sideHustles)}

@app.get("money-quotes")
def getMoneyQuotes(apiKey: str):
    if apiKey != "123456789":
        return{"error": "Invalid Api Key"}
    """ Return a Random Money Quotes """
    return{"money-quotes": random.choice(moneyQuotes)}