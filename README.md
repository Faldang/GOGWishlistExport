# GOGWishlistExport
Script to export discounted games from a GOG Wishlist to a CSV file. Useful when deciding what to buy during large sales

Wishlist must be viewable by everyone in order for the script to work. Only discounted items are exported, if at least one item is discounted. If no items are currently discounted, the script exports the whole wishlist

To use it, edit dudeId.txt: first line should be your GOG profile name, and the second line should be the folder path where you want the CSV saved.
After that, run WishlistExport.py

Bonus: Request.py is a script that scrapes the entire Store list of games on GOG, and saves it as a text file. The file path is currently hardcoded in the script. I use it weekly, to update a spreadsheet with a master list of GOG games.

