use std::io::{self, Write};

const QUIT_SYMBOL: &str = "Q";

fn main() {
    print!("\nEnter a stock symbol, or {} to quit: ", QUIT_SYMBOL);
    io::stdout().flush().unwrap();

    let mut stock_symbol = String::new();

    while stock_symbol != QUIT_SYMBOL {
        stock_symbol.clear();
        io::stdin().read_line(&mut stock_symbol).unwrap();
        stock_symbol = stock_symbol.trim().to_uppercase();

        if stock_symbol == QUIT_SYMBOL {
            break;
        }

        println!("\nPerforming analysis on stock symbol: {}\n", stock_symbol);
    }

    println!("\nExiting program...");
}
