# Commerce Auction Website

Welcome to the **Commerce Auction Website** repository! This project is a full-fledged auction platform developed using **Python Django**, **HTML**, **CSS**, and **JavaScript**. It allows users to create accounts, list items for auction, bid on items, leave comments, and manage their watchlists. The website also features category-based sorting and supports item creators in closing auctions when they are ready.

## Features Overview

### 1. **Register Account**
   - Users can create an account to participate in auctions.
   - Registration requires basic details like username, email, and password.
   - Once registered, users can log in and enjoy the full functionality of the auction website.

### 2. **Active Listings**
   - Displays all active auction items that have been added by different users.
   - Users can browse through the list of active auctions and select an item for more details.
   - Listings include item name, description, current highest bid, and the auction creator's name.

### 3. **Category**
   - Users can sort auction items by category for easier navigation.
   - Categories help users find specific types of items quickly.

### 4. **Watchlists**
   - Users can save auction items to their watchlist to keep track of them easily.
   - Watchlists display all saved items, allowing users to monitor bids and make decisions quickly.

### 5. **Create Listings**
   - Authenticated users can create new auction listings by providing:
     - Item name, description, starting bid, image (optional), and category.
   - Listings are immediately added to the active auction pool once created.

### 6. **Item Page**
   - Detailed view of a specific auction item.
   - Users can perform the following actions:
     - **Save to Watchlist**: Add the item to their watchlist for later reference.
     - **Bid**: Place a bid on the item. Bids must be higher than the current highest bid.
     - **Comment**: Leave comments about the item, which are visible to other users.
   - If the creator decides to close the auction, the item will be marked as closed, and the highest bidder will be declared the winner. Once closed, the item will no longer accept new bids.

## Technologies Used

- **Python Django**: Framework used for building the web application, handling user authentication, and managing data models.
- **HTML**: Markup language used to structure the content of the web pages.
- **CSS**: Used for styling the web pages, ensuring a clean and visually appealing design.
- **JavaScript**: Adds interactivity to the website, such as updating watchlists and handling bid submissions.

## Getting Started

To set up the Commerce Auction Website locally, follow these instructions:

### Prerequisites

- **Python 3.x**: Make sure Python is installed on your system.
- **Django**: Install Django using `pip install django`.

### Steps to Run the Project

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/commerce_auction_website.git
   ```

2. **Navigate to the Project Directory**:
   ```bash
   cd commerce_auction_website
   ```

3. **Set Up Virtual Environment** (Optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`


4. **Run Migrations**:
   ```bash
   python manage.py migrate
   ```

5. **Start the Development Server**:
   ```bash
   python manage.py runserver
   ```

6. **Access the Website**:
   - Open your browser and go to `http://localhost:8000`


## Contributing

Contributions are welcome! If you'd like to improve the website or add new features, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Make your changes and test thoroughly.
4. Submit a pull request with a detailed explanation of your changes.

---

Enjoy bidding and managing your auction items with **Commerce Auction Website**!
