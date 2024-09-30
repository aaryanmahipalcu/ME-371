import csv
import json

def load_book_data(filename):
    """
    Read book data from a CSV file.
    Args:
        filename (str): Name of the CSV file
    Returns:
        list of dict: List of dictionaries containing book properties
    """
    # TODO: Implement CSV file reading
    # Creating a list called 'books'
    books = []
    # Open the csv file and read its contents
    with open(filename, mode='r', newline='', encoding='utf-8') as file:
        csv_reader = csv.DictReader(file)

        #Iterating over each row in the csv and appending it to the list
        for row in csv_reader:
            books.append({
                'title': row['title'],
                'author': row['author'],
                'year': int(row['year']), #Converting the year to an integer
                'genre': row['genre'],
                'price': float(row['price']) #Converting the price to a float
            })
    return books 

def calculate_discount_price(books, discount_rate):
    """
    Calculate and add discounted price for each book.
    Args:
        books (list of dict): List of book dictionaries
        discount_rate (float): Discount rate to apply
    Returns:
        list of dict: Updated list of book dictionaries with discounted price
    """
    # TODO: Implement discounted price calculation
    for book in books:
        # Calculating the discounted price
        discounted_price = book['price'] * (1 - discount_rate)

        # Adding the new key-value pair for the discounted price
        book['discounted_price'] = float(discounted_price)
    return books

def find_unique_genres(books):
    """
    Find unique genres from the data.
    Args:
        books (list of dict): List of book dictionaries
    Returns:
        set: Set of unique genres
    """
    # TODO: Implement unique genres extraction
    unique_genres = set()
    #Iterating over each book in the list
    for book in books:
        #Add genre of each book to the set
        unique_genres.add(book['genre'])
        # Since a set can only have unique values, when we return the set we will get a set of unique genres from the dataset
    return unique_genres 

def filter_books_by_year(books, start_year, end_year):
    """
    Filter books based on publication year range.
    Args:
        books (list of dict): List of book dictionaries
        start_year (int): Start year of the range
        end_year (int): End year of the range
    Returns:
        list of dict: Filtered list of book dictionaries
    """
    # TODO: Implement book filtering by year
    filtered_books = []
    # Iterate over each book in the list
    for book in books:
        # Checking if the book is published within a specified range
        if start_year <= book['year'] <= end_year:
            filtered_books.append(book)
    return filtered_books

def sort_books(books, sort_by, reverse=False):
    """
    Sort books based on a specified property.
    Args:
        books (list of dict): List of book dictionaries
        sort_by (str): Property to sort by
        reverse (bool): Sort in descending order if True
    Returns:
        list of dict: Sorted list of book dictionaries
    """
    # TODO: Implement book sorting
    books.sort(key=lambda book: book[sort_by], reverse=reverse)
    return books

def find_most_prolific_author(books):
    """
    Find the author with the most books in the dataset.
    Args:
        books (list of dict): List of book dictionaries
    Returns:
        str: Name of the most prolific author
    """
    # TODO: Implement finding the most prolific author
    author_count = {}
    # Counting the occurances of each author
    for book in books:
        author = book['author']
        if author in author_count:
            author_count[author] += 1
        else:
            author_count[author] = 1
    
    #Finding the most prolific author
    find_most_prolific_author = None
    max_books = 0

    for author, count in author_count.items():
        if count > max_books:
            find_most_prolific_author = author
            max_books = count
    return find_most_prolific_author

def calculate_average_price_by_genre(books):
    """
    Calculate average book price for each genre.
    Args:
        books (list of dict): List of book dictionaries
    Returns:
        dict: Dictionary of average prices by genre
    """
    # TODO: Implement average price calculation by genre
    # Dictionary to hold the total price and count of books for each genre
    genre_totals = {}

    # Iterate through each book in the dataset
    for book in books:
        genre = book['genre']
        price = book['price']
        # Initialize the genre entry in the dictionary if it doesn't exist
        if genre not in genre_totals:
            genre_totals[genre] = {'total_price': 0, 'count': 0}

        # Accumulate the total price and count for each genre
        genre_totals[genre]['total_price'] += price
        genre_totals[genre]['count'] += 1

    # Calculating the average price for each genre
    average_prices = {}
    for genre, totals in genre_totals.items():
        average_prices[genre] = totals['total_price'] / totals['count']
    return average_prices

def generate_book_report(books, output_filename):
    """
    Generate a formatted report of books and their properties.
    Args:
        books (list of dict): List of book dictionaries
        output_filename (str): Name of the output text file
    """
    # TODO: Implement report generation
    with open(output_filename, mode='w', encoding='utf-8') as file:
        # Write the header
        file.write("Book Report\n")
        file.write("=" * 40 + "\n")

        # Write each book's details
        for book in books:
            file.write(f"Title: {book['title']}\n")
            file.write(f"Author: {book['author']}\n")
            file.write(f"Year: {book['year']}\n")
            file.write(f"Genre: {book['genre']}\n")
            file.write(f"Price: ${book['price']:.2f}\n")
            file.write("-" * 40 + "\n")

    print(f"Report generated and saved to {output_filename}")

def update_book_properties(books, updates):
    """
    Update book properties based on provided updates.
    Args:
        books (list of dict): List of book dictionaries
        updates (dict): Dictionary of updates for books
    Returns:
        list of dict: Updated list of book dictionaries
    """
    # TODO: Implement book property updates with error handling
    for title, properties in updates.items():
        # Find the book by title
        for book in books:
            if book['title'] == title:
                # Update the book's properties
                for key, value in properties.items():
                    if key in book:
                        book[key] = value
                break # Exit loop after updating the book


def convert_currency(books, exchange_rate):
    """
    Convert book prices to a different currency.
    Args:
        books (list of dict): List of book dictionaries
        exchange_rate (float): Exchange rate to apply
    Returns:
        list of dict: Updated list of book dictionaries with converted prices
    """
    # TODO: Implement currency conversion with error handling
    # We must first check if the given exchange rate is valid
    if exchange_rate <= 0:
        raise ValueError("Exchange rate must be greater than zero.")
    
    for book in books:
        try:
            # Convert the price to the new currency
            original_price = book['price']
            book['price'] = round(original_price * exchange_rate, 2)
        except KeyError as e:
            print(f"Warning: Missing price key for book '{book.get('title', 'Unknown')}'.")
        except Exception as e:
            print(f"Error converting price for book '{book.get('title', 'Unknown')}': {e}")
        

def main():
    input_file = "Data Analysis and Processing\books.csv"
    output_file = "book_analysis_report.txt"
    
    try:
        # Load data
        books = load_book_data(input_file)
        
        # Process data
        books = calculate_discount_price(books, 0.1)  # 10% discount
        unique_genres = find_unique_genres(books)
        
        # Perform analysis
        recent_books = filter_books_by_year(books, 2000, 2023)
        sorted_books = sort_books(books, 'price', reverse=True)
        top_author = find_most_prolific_author(books)
        
        # Generate statistics
        avg_prices = calculate_average_price_by_genre(books)
        
        # Generate report
        generate_book_report(books, output_file)
        
        # Perform updates and conversions
        updates = {'Book 1': {'year': 1960}, 'Book 2': {'price': 12.99}}
        books = update_book_properties(books, updates)
        books = convert_currency(books, 0.85)  # Convert to GBP
        
        print(f"Analysis complete. Report generated: {output_file}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()