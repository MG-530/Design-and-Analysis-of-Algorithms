use std::io;
use std::fs::File;
use std::io::BufRead;
use std::io::BufReader;

fn recursive_gcd(a: i32, b: i32) -> i32 {
    // Handle negative numbers
    let a = a.abs();
    let b = b.abs();
    
    // Base case
    if b == 0 {
        return a;
    }
    
    // Recursive case
    recursive_gcd(b, a % b)
}

fn main() -> io::Result<()> {
    // Read input from file
    let file = File::open("input.txt")?;
    let reader = BufReader::new(file);
    let mut lines = reader.lines();
    
    let a: i32 = lines.next().unwrap()?.trim().parse().unwrap();
    let b: i32 = lines.next().unwrap()?.trim().parse().unwrap();
    
    // Calculate result
    let result = recursive_gcd(a, b);
    
    // Write output
    std::fs::write("output.txt", result.to_string())?;
    
    Ok(())
} 